from ctypes import sizeof

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    response = requests.get("https://news.ycombinator.com/news")
    response.raise_for_status()
    yc_web_page = response.text

    soup = BeautifulSoup(yc_web_page, "html.parser")

    article_texts = []
    article_links = []
    parent_tags = soup.find_all(name="span", class_="titleline")
    for tag in parent_tags:
        articles = tag.find_all(name="a")[0]
        article_text = articles.getText()
        # print(article_text)
        article_texts.append(article_text)

        article_link = articles.get("href")
        # print(article_link)
        article_links.append(article_link)
        # print("")

    article_scores = [
        int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")
    ]

    # print(article_links)
    # print(article_texts)
    print(article_scores)

    # high_score = 0
    # high_score_index = 0
    # for score in range(len(article_scores)):
    #     if article_scores[score] > high_score:
    #         high_score = article_scores[score]
    #         high_score_index = score
    largest_num = max(article_scores)
    high_score_index = article_scores.index(largest_num)

    print(article_links[high_score_index + 1])
    print(article_texts[high_score_index + 1])
    print(article_scores[high_score_index])
    print(high_score_index)


#     with open("website.html") as file:
#         site_contents = file.read()

# soup = BeautifulSoup(site_contents, "html.parser")
# print(soup.title)
