from flask import Flask, render_template, request
import smtplib
import requests

data = requests.get("https://api.npoint.io/2fba7f6009a9cfff9ae9").json()
OWN_EMAIL = ""
OWN_PASSWORD = ""

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data_f = request.form
        data_f = request.form
        send_email(data_f["name"], data_f["email"], data_f["phone"], data_f["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)
