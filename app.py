from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_home():
    return """
        <h1>Kam ki baat</h1>
        <a href="/youtube">Go to YouTube</a><br>
        <a href="/home">Go to Home Page</a><br>
        <a href="/about">Go to About Page</a><br>
        <a href="/login">Go to Login Page</a><br>
        <a href="/contact">Go to Contact Page</a>
    """


@app.route("/youtube")
def youtube():
    return """
        <a href="https://www.youtube.com/" target="_blank">Jau ta YouTube</a>
    """


@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
