from flask import Flask, render_template, send_from_directory


app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', as_attachment=True)


@app.route('/')
def index():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True)
