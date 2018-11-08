from flask import Flask, url_for

app = Flask(__name__)

@app.route('/index', endpoint = 'xxx')
def index():
    v = url_for("xxx")
    print(v)
    return 'Hello world'

@app.route('/zzz/<int:nid>', endpoint = "aaa")
def zzz(nid):
    v = url_for("aaa", nid = nid)
    print(v)
    return 'index'

if __name__ == '__main__':
    app.run()