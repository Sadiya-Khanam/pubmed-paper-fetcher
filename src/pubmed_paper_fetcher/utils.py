import csv
def save_to_csv(articles: list[dict], output_file: str):
    if not articles:
        print("⚠️ No articles to save.")
        return
    # Get all unique keys across all articles
    all_keys = set()
    for article in articles:
        all_keys.update(article.keys())
    fieldnames = sorted(all_keys)

    with open(output_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for article in articles:
            writer.writerow(article)
