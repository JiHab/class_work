from wsgiref.simple_server import make_server

from flask import Flask, request, redirect
app = Flask(__name__)


@app.route("/")
def hello():
    return """
     <form action="/get-sum" method="post">
                        <p><summary>get sum</summary></p>
                        <p><b>a:</b>
                        <input name="a" ></p>
                        <b>b:</b>
                        <input name="b">
                        <p><button>submit</button></p>
                        </form>
    """
@app.route("/get-sum",  methods=['POST'])
def sum():
    print(str(request.form['b']))
    print(str(request.form['a']))
    ret = int(request.form['b']) + int(request.form['a'])
    print(str(ret))
    return str(ret)

if __name__ == "__main__":
    app.run()