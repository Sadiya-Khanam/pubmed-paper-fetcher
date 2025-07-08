import argparse
import csv
import json
from .fetcher import (
    fetch_pubmed_ids,
    fetch_pubmed_details,
    filter_articles_by_affiliation,
)

from .writer import write_to_csv  

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers related to pharma/biotech authors.")
    parser.add_argument("query", help="PubMed search query")
    parser.add_argument("-f", "--file", help="Filename to save results (CSV). If not given, prints to console.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")

    args = parser.parse_args()

    if args.debug:
        print(f"[DEBUG] Query: {args.query}")
        print(f"[DEBUG] Output file: {args.file}")

    print(f"\n[INFO] Fetching articles for: {args.query}")
    pubmed_ids = fetch_pubmed_ids(args.query, max_results=20)

    if args.debug:
        print(f"[DEBUG] Found {len(pubmed_ids)} PubMed IDs")

    articles = fetch_pubmed_details(pubmed_ids)
    filtered_articles = filter_articles_by_affiliation(articles, debug=args.debug)

    if args.debug and filtered_articles:
        print("\n[DEBUG] Sample filtered article:")
        print(json.dumps(filtered_articles[0], indent=2))
        return

    print(f"[INFO] Found {len(filtered_articles)} article(s) from pharma/biotech affiliations.")

    if not filtered_articles:
        print("[INFO] No relevant articles found.")
        return

    if args.file:
        write_to_csv(filtered_articles, args.file)  
        print(f"[INFO] Results saved to {args.file}")
    else:
        for article in filtered_articles:
            print("-" * 80)
            print(f"PMID: {article.get('pmid', '')}")
            print(f"Title: {article.get('title', '')}")
            print(f"Publication Date: {article.get('pub_date', '')}")
            print(f"Non-academic Authors: {', '.join(article.get('non_academic_authors', []))}")
            print(f"Company Affiliations: {', '.join(article.get('company_affiliations', []))}")
            print(f"Corresponding Author Email: {article.get('corresponding_email', '')}")


if __name__ == "__main__":
    main()
