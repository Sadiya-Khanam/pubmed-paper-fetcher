import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import argparse
from pubmed_paper_fetcher.fetcher import (
    fetch_pubmed_ids,
    fetch_pubmed_details,
    filter_articles_by_affiliation
)
from pubmed_paper_fetcher.writer import save_to_csv


def main():
    parser = argparse.ArgumentParser(description="PubMed Pharma/Biotech Paper Fetcher")
    parser.add_argument("--query", required=True, help="PubMed query string")
    parser.add_argument("--max-results", type=int, default=20, help="Maximum number of results to fetch")
    parser.add_argument("--output", type=str, default="results.csv", help="Output CSV file path")
    parser.add_argument("--debug", action="store_true", help="Print debug information")

    args = parser.parse_args()

    if args.debug:
        print(f"🔍 Query: {args.query}")
        print(f"🔢 Max Results: {args.max_results}")
        print(f"📁 Output Path: {args.output}")

    ids = fetch_pubmed_ids(args.query, args.max_results, args.debug)
    articles = fetch_pubmed_details(ids, args.debug)
    filtered = filter_articles_by_affiliation(articles, args.debug)

    save_to_csv(filtered, args.output)
    print(f"✅ Saved {len(filtered)} filtered papers to {args.output}")


if __name__ == "__main__":
    main()
