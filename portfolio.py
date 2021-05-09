from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
curr_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(curr_dir, 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<page>')
def pages(page):
    return render_template(page)


def write_file(data):
    with open('F:\\database.txt', 'a') as database_txt:
        e_mail = data['email']
        sub_ject = data['subject']
        msg = data['message']
        info = "Email : {}\nSubject : {}\nMessage : {}\n\n".format(e_mail, sub_ject, msg)
        database_txt.writelines(info)


@app.route('/submitted', methods=['GET', 'POST'])
def form_submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_file(data)
        em = str(data['email'])
        name = em.split('@')[0]
        return render_template('thanks.html', user=name)


if __name__ == '__main__':
    app.run(debug=True)
