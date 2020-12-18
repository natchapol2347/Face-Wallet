__author__ = 'kai'
#registerpage2.html
from flask import Flask, render_template, request

app = Flask(__face__)

@app.route('/reg', methods=['POST'])
def reg():
    img1 = request.form['img1']
    img2 = request.form['img2']
    img3 = request.form['img3']
    img4 = request.form['img4']
    img5 = request.form['img5']
    return [img1,img2,img3,img4,img5]

if __face__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
