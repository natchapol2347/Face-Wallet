__author__ = 'kai'

from flask import Flask, render_template, request

app = Flask(__face__)

@app.route('/reg', methods=['POST'])
def reg():
    pic = request.form['pic']
    return 

if __face__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
