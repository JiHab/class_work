import sqlite3
from flask import Flask, request, redirect
#from classwork_02022016 import init_db
app = Flask(__name__)
db_name = "my_lib.db"


@app.route("/")
def hello():
    return """
    <a href="http://127.0.0.1:5000/show_all_authors">Всех посмотреть</a>
    """

def show_all_ath(i, strAth):
    return '<a href="/ath' + str(i) + '">' + strAth + "</a><br>"


@app.route("/ath<ath_id>")
def ath(ath_id):
    return str(ath_id)

@app.route("/show_all_authors")
def all_authors():
    ret = ''
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM author')
#print("Authors:")
        rows = cur.fetchall()
#print(rows)
        for row in rows:
            i = 0
            ret += show_all_ath(row[0],row[1])
            i += 1

            #print(row[1])
    #
    ret += """          <form action="/new_auth" method="post">
                        <p><details><summary>Add new author</summary></p>
                        <p><b>Name:</b>
                        <input name="surname_ath" атрибуты></p>
                        <b>Surname:</b>
                        <input name="name_ath"атрибуты>
                        <p><button>submit</button></p>
                        </details></form>
            """
    #print(ret)
    return ret

@app.route("/new_auth", methods=['POST'])
def new_author():
    str_name = ('\n' + request.form['name_ath'])
    #str_surname = ('\n' + request.form['surname_ath'])
    #print(str_name)
    print(request.form['name_ath'])
    return 'ololol'

if __name__ == "__main__":
    #init_db(db_name)
    app.run()
#init_db("my_lib.db")
    #print("started")