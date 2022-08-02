from flask import Flask, render_template
from post import Post
import requests

data = requests.get("https://api.npoint.io/2fba7f6009a9cfff9ae9").json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)
