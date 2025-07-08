"""import csv
from typing import List, Dict

def write_to_csv(articles: List[Dict[str, str]], filename: str) -> None:
    if not articles:
        print("No articles to write.")
        return

    fieldnames = [
        "PubmedID",
        "Title",
        "Publication Date",
        "Non-academic Author(s)",
        "Company Affiliation(s)",
        "Corresponding Author Email",
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for article in articles:
            writer.writerow(article)"""


import csv
from typing import List, Dict
def save_to_csv(articles: list[dict], filename: str):
    if not articles:
        print("[INFO] No articles to write.")
        return

    fieldnames = [
        "PubmedID",
        "Title",
        "Publication Date",
        "Non-academic Author(s)",
        "Company Affiliation(s)",
        "Corresponding Author Email"
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for article in articles:
            writer.writerow({
                "PubmedID": article["pmid"],
                "Title": article["title"],
                "Publication Date": article["pub_date"],
                "Non-academic Author(s)": ", ".join(article["non_academic_authors"]),
                "Company Affiliation(s)": ", ".join(article["company_affiliations"]),
                "Corresponding Author Email": article["corresponding_email"]
            })

    print(f"[INFO] Results written to {filename}")

