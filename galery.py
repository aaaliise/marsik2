from flask import Flask, render_template, request, url_for
import json
from random import choice

app = Flask(__name__)


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    data = ['static/img/doc1.jpeg', 'static/img/doc2.jpeg', 'static/img/doc3.jpeg',
            'static/img/doc4.jpeg']
    if request.method == 'POST':
        f = request.files['File']
        f.save(f"static/img/{f.filename}")
        data.append(f"static/img/{f.filename}")
        data = list(set(data))
    return render_template('carousel2.html', images=data, range=list(range(len(data))))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')