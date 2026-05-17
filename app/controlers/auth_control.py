from flask import render_template, request


class AuthController:
    def login(self):
        if request.method == "POST":
            print(request.form)
        return render_template("login.html")

    def register(self):
        return render_template("register.html")

    def niggas(self):
        return render_template("niggas.html")

    def home(self):
        return render_template("home.html")

    def contact_us(self):
        return render_template("contact_us.html")
