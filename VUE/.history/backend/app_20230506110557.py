from flask import Flask, render_template, request, Response, redirect, url_for, session
import json

app = Flask(__name__,
            static_folder='../frontend/dist',
            template_folder="../frontend/dist",
            static_url_path="")


@app.route('/test', methods=['GET'])
def test():
    return json.dumps('hello world!')


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
