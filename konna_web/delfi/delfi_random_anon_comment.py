import random
import konna_web.delfi.delfi_articles as da
import konna_web.delfi.delfi_comments as dc


def _random_article() -> da.Article:
    articles = da.get_top_front_page_articles(10)
    return random.choice(articles)


"""
def random_comment_with_replies():
    article = _random_article()
    all_comments = dc.get_all_comments(article["id"], True, [True])
    with_replies = [x for x in all_comments if x["replies"] and x["subject"] and x["content"]]
    return random.choice(with_replies)
"""


def random_comment() -> (dc.Comment, str):
    article = _random_article()
    all_comments = dc.get_all_comments(article["id"], False, [True])
    filtered_comments = [comment for comment in all_comments if
                         comment["content"] is not None and 2 < len(comment["content"]) < 200]
    return random.choice(filtered_comments), article["name"], article["url"]


if __name__ == '__main__':
    print(random_comment())
