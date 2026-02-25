import os
import zipfile
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        singer = request.form["singer"]
        number = request.form["number"]
        duration = request.form["duration"]
        email = request.form["email"]

        output = "mashup.mp3"

        command = (
            f'python "../Program 1/102497014.py" '
            f'"{singer}" {number} {duration} {output}'
        )

        subprocess.call(command, shell=True)

        zip_name = "mashup.zip"

        with zipfile.ZipFile(zip_name, "w") as zipf:
            zipf.write(output)

        return "Mashup created successfully. ZIP file created."

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)