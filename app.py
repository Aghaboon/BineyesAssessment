from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace "your_secret_key" with your actual secret key

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/greeting", methods=["POST"])
def greeting():
    name = request.form.get("name")

    # check if the field empty and send the notification message.
    if not name:
        flash("Please enter your name.")
        return redirect("/")

    # Check if the input is not a characters and send the notification message.
    if not name.isalpha():
        flash("Name should only contain letters.")
        return redirect("/")

    return render_template("greeting.html", name=name)

if __name__ == "__main__":
    app.run()
