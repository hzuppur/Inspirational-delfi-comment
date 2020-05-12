import random
import konna_web.delfi_articles as da
import konna_web.delfi_comments as dc


def random_comment_with_replies():
  article_ids = da.get_top_n_article_ids(10)
  article_id = random.choice(article_ids)
  all_comments = dc.get_all_comments(article_id, True, [True])
  with_replies = [x for x in all_comments if x["replies"] and x["subject"] and x["content"]]
  return random.choice(with_replies)


def random_comment():

  article_ids = da.get_top_n_article_ids(10)
  article_id = random.choice(article_ids)
  all_comments = dc.get_all_comments(article_id, False, [True])
  filtered_comments = [i for i in all_comments if i["content"] is not None and 10 < len(i["content"]) < 200]
  return random.choice(filtered_comments)


if __name__ == '__main__':
  comment = random_comment()
