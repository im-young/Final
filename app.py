from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)


@app.route('/')
def memory():
    return render_template('home2.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)