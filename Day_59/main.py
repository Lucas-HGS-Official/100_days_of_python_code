import requests
from flask import Flask, render_template

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
app = Flask(__name__)


def main():
    if __name__ == "__main__":
        app.run(debug=True)


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


# @app.route("/index.html")
# def index():
#     return render_template("index.html", all_posts=posts)


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/post.html")
def post():
    # index = 1
    # requested_post = None
    # for blog_post in posts:
    #     if blog_post["id"] == index:
    #         requested_post = blog_post
    return render_template("post.html", post=posts[0])


@app.route("/post/<int:index>")
def requested_post(index: int):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


main()
