# src/pubmed_paper_fetcher/fetcher.py

"""from typing import List, Dict, Optional
from Bio import Entrez
import re

Entrez.email = "test@example.com"  # Replace with your real email

def fetch_pubmed_ids(query: str, max_results: int = 20, debug: bool = False) -> List[str]:
    try:
        handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        record = Entrez.read(handle)
        if debug:
            print(f"[DEBUG] PubMed IDs fetched: {record['IdList']}")
        return record["IdList"]
    except Exception as e:
        print(f"Error while fetching PubMed IDs: {e}")
        return []

def fetch_pubmed_details(pubmed_ids: List[str], debug: bool = False) -> List[Dict]:
    try:
        ids_str = ",".join(pubmed_ids)
        handle = Entrez.efetch(db="pubmed", id=ids_str, rettype="medline", retmode="xml")
        records = Entrez.read(handle)
        if debug:
            print(f"[DEBUG] Number of articles fetched: {len(records['PubmedArticle'])}")
        return records["PubmedArticle"]
    except Exception as e:
        print(f"Error while fetching article details: {e}")
        return []

def is_pharma_biotech_affiliation(affiliation: str) -> bool:
    keywords = [
        "pharma", "pharmaceutical", "biotech", "biotechnology", "life sciences",
        "therapeutics", "biosciences", "labs", "laboratories", "inc", "ltd"
    ]
    return any(re.search(rf"\b{word}\b", affiliation.lower()) for word in keywords)

def filter_articles_by_affiliation(articles: List[Dict], debug: bool = False) -> List[Dict]:
    filtered = []
    for article in articles:
        try:
            affiliations = []
            authors = article["MedlineCitation"]["Article"].get("AuthorList", [])
            for author in authors:
                affs = author.get("AffiliationInfo", [])
                for aff in affs:
                    affiliations.append(aff.get("Affiliation", ""))
            if any(is_pharma_biotech_affiliation(aff) for aff in affiliations):
                filtered.append(article)
                if debug:
                    print(f"[DEBUG] Matched article: {article['MedlineCitation']['PMID']}")
        except Exception as e:
            if debug:
                print(f"[DEBUG] Error checking article: {e}")
    return filtered"""


    # src/pubmed_paper_fetcher/fetcher.py
from typing import List, Dict
from Bio import Entrez
import re

Entrez.email = "test@example.com"  # Replace with your real email

def fetch_pubmed_ids(query: str, max_results: int = 20, debug: bool = False) -> List[str]:
    """Fetches PubMed IDs based on the search query."""
    try:
        handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        result = Entrez.read(handle)
        ids = result["IdList"]
        if debug:
            print(f"Fetched IDs: {ids}")
        return ids
    except Exception as e:
        print("Error fetching PubMed IDs:", e)
        return []

def fetch_pubmed_details(pubmed_ids: List[str], debug: bool = False) -> List[Dict]:
    """Gets detailed info for each PubMed ID."""
    try:
        ids_str = ",".join(pubmed_ids)
        handle = Entrez.efetch(db="pubmed", id=ids_str, rettype="medline", retmode="xml")
        data = Entrez.read(handle)
        articles = data["PubmedArticle"]
        if debug:
            print(f"Total articles fetched: {len(articles)}")
        return articles
    except Exception as e:
        print("Error fetching article details:", e)
        return []

def is_pharma_biotech_affiliation(affiliation: str) -> bool:
    """Checks if an affiliation matches pharma/biotech keywords."""
    keywords = [
        "pharma", "pharmaceutical", "biotech", "biotechnology", "life sciences",
        "therapeutics", "biosciences", "labs", "laboratories", "inc", "ltd"
    ]
    for word in keywords:
        if re.search(rf"\b{word}\b", affiliation.lower()):
            return True
    return False

def filter_articles_by_affiliation(articles: List[Dict], debug: bool = False) -> List[Dict]:
    """Filters and extracts info from articles with at least one pharma/biotech affiliated author."""
    filtered = []

    for article in articles:
        try:
            citation = article.get("MedlineCitation", {})
            article_info = citation.get("Article", {})
            authors = article_info.get("AuthorList", [])

            pmid = citation.get("PMID", "")
            title = article_info.get("ArticleTitle", "")
            pub_date = ""
            try:
                pub_date_info = article_info.get("Journal", {}).get("JournalIssue", {}).get("PubDate", {})
                pub_date = pub_date_info.get("Year") or pub_date_info.get("MedlineDate") or ""
            except:
                pass

            non_academic_authors = []
            company_affiliations = set()
            corresponding_email = ""

            matched = False

            for author in authors:
                affs = author.get("AffiliationInfo", [])
                for aff in affs:
                    aff_text = aff.get("Affiliation", "")
                    if is_pharma_biotech_affiliation(aff_text):
                        matched = True
                        if aff_text not in company_affiliations:
                            company_affiliations.add(aff_text)

                        # Extract non-academic authors
                        name_parts = []
                        if "LastName" in author:
                            name_parts.append(author["LastName"])
                        if "ForeName" in author:
                            name_parts.append(author["ForeName"])
                        full_name = " ".join(name_parts)
                        if full_name:
                            non_academic_authors.append(full_name)

                        # Try to extract email from affiliation
                        email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", aff_text)
                        #if email_match:
                        if email_match and not corresponding_email:
                            corresponding_email = email_match.group()

               # if matched:
                    #break  # Stop checking after first pharma author match
                    # Don't break, keep looking for emails among all pharma-affiliated authors


            if matched:
                filtered.append({
                    "pmid": str(pmid),
                    "title": str(title),
                    "pub_date": str(pub_date),
                    "non_academic_authors": non_academic_authors,
                    "company_affiliations": list(company_affiliations),
                    "corresponding_email": corresponding_email
                })
                if debug:
                    print(f"[MATCHED] PMID: {pmid}, Company affiliations: {company_affiliations}")

        except Exception as e:
            if debug:
                print("Error parsing article:", e)

    return filtered

