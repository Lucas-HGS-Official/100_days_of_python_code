from flask import Flask, render_template

app = Flask(__name__)


def main():
    if __name__ == "__main__":
        app.run(debug=True)


@app.route("/")
def hello():
    return render_template("index.html")


main()
