from flask import Flask,request,render_template,url_for,jsonify,redirect,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_username = 'db_user'
db_password = 'db_password'
db_database = 'db_test'

app.config['SECRET_KEY'] = 'dAUjXbnib6L70U2UWm8y9m+SjCG8KlU6PY/87fDre/o='
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_username}:{db_password}@pgsql_test:5432/{db_database}"

db = SQLAlchemy(app)

class FirstTable(db.Model):
    __tablename__ = 'firsttable'
    id = db.Column(db.Integer, primary_key=True)
    ft_title = db.Column(db.String(1000))
    ft_description = db.Column(db.String(6000))

@app.route('/',methods=['GET'])
def index():
    posts = FirstTable.query.all()
    return render_template("index.html",posts=posts)

@app.route('/posts',methods=['GET','POST'])
def add_posts():
    if request.method == 'POST':
        new_title  = request.form['blog_title']
        new_description  = request.form['blog_description']
        new_post = FirstTable(ft_title=new_title,ft_description=new_description)
        db.session.add(new_post)
        db.session.commit()
        flash("Post Added")
    return redirect(url_for('index'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all() # <--- create db object.
    app.run(host='0.0.0.0', port=5050, debug=True)