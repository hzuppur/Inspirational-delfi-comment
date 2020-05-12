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
        "link": link,
      })

  return ids


def get_top_n_article_ids(n=5):
  comment_counts_ids = get_article_comment_counts_ids()
  comment_counts_ids.sort(key=lambda x: x["count"], reverse=True)
  return [x["id"] for x in comment_counts_ids[:n]]


def get_top_n_article_ids_link(n=5):
  comment_counts_ids = get_article_comment_counts_ids()
  comment_counts_ids.sort(key=lambda x: x["count"], reverse=True)
  return [(x["id"], x["link"]) for x in comment_counts_ids[:n]]


def get_article_name(article_url):
  page = requests.get(article_url)
  soup = BeautifulSoup(page.text, "html.parser")
  article_name = soup.find("h1", {"class": "article-title"})
  return article_name.text


if __name__ == '__main__':
  get_article_name("https://sport.delfi.ee/news/ekstreemsport/kellysildaru/sildarude-tuli-kelly-ja-tonis-jagasid-asju-kohtus-edasi-kaib-vaidlus-suusaliidust-saadava-raha-ule?id=89830575&com=1")
