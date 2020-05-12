import requests
from bs4 import BeautifulSoup

ARTICLES_URL = "https://www.delfi.ee/"


def get_article_comment_counts_ids():
    page = requests.get(ARTICLES_URL)
    soup = BeautifulSoup(page.text, "html.parser")
    articles_with_comments = soup.findAll("a", {"class": "headline__comments"})

    ids = []
    for article in articles_with_comments:
        comments = int(article.text.replace("(", "").replace(")", ""))
        link = article["href"]
        if len(link.split("?id=")) > 1:
            ids.append({
                "id": int(link.split("?id=")[1].replace("&com=1", "")),
                "count": comments,
            })

    return ids


def get_top_n_article_ids(n=5):
    comment_counts_ids = get_article_comment_counts_ids();
    comment_counts_ids.sort(key=lambda x: x["count"], reverse=True)
    return [x["id"] for x in comment_counts_ids[:n]]


if __name__ == '__main__':
    print(get_top_n_article_ids())
