from flask import Flask, render_template, request, make_response, g, redirect
from models import User, Article
import hashlib
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# before_request nostrādā PIRMS KATRA PIEPRASĪJUMA
# pārbaudam vai lietotājs ir ielogojies
@app.before_request
def before_request():
    session_cookie = request.cookies.get("session")
    if session_cookie:
        g.active_session = session_cookie
        user = User.fetch_one(query=['session_token', '==', session_cookie])
        g.user_name = user.name


@app.route('/logout')
def logout():
    user = User.fetch_one(query=['session_token', '==', g.active_session])
    user.edit(user.id, session_token='-')  # reset session token
    response = make_response(redirect('/'))
    response.set_cookie('session', '', expires=0)  # izdzesam cookie
    return response


@app.route("/")
def index():
    personname = 'Andis'
    cookie_name = request.cookies.get("user_name")
    return render_template('index.html', name=personname, login_name=cookie_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    status = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = User.fetch_one(query1=["password", "==", hashed_password], query2=['email', '==', email])
        if user:  # successful login
            session_token = str(uuid.uuid4())
            user.edit(user.id, session_token=session_token)
            set_cookie = session_token
            response = make_response(redirect('/'))
            response.set_cookie('session', session_token)
            return response
        else:
            status = 'Nepareizs epasts vai parole!'
    return render_template('login.html', status=status)


@app.route("/about", methods=['GET', 'POST'])
def about():
    l = ['abols', 'bumbieris', 'apelsīns', 'citrons']
    return render_template('about.html', saraksts=l)


@app.route("/contacts", methods=['GET', 'POST'], defaults={'contact_id': None})
@app.route("/contacts/<contact_id>", methods=['GET', 'POST'])
def contacts(contact_id):
    result = None
    if request.method == 'POST':
        contact_name = request.form.get("name")
        contact_email = request.form.get("email")
        contact_password = request.form.get("password")
        if contact_id:
            user = User.get(obj_id=contact_id)
            user.edit(contact_id, name=contact_name, email=contact_email)
            return redirect('/contacts')
            # result = "{} successfully updated!".format(contact_name.upper())
            # TODO: password currently unchanged, must regenerate hash
        else:
            h_passwd = hashlib.sha256(contact_password.encode()).hexdigest()
            user = User(name=contact_name, email=contact_email, password=h_passwd)
            user.create()  # save the object into a database
            result = "{} successfully saved to db!".format(contact_name.upper())
    if contact_id:
        user = User.get(obj_id=contact_id)
    else:
        user = None
    all_contacts = User.fetch()
    return render_template('contacts.html', result=result, all_contacts=all_contacts, user=user)


@app.route('/deletecontact/<contact_id>', methods=['GET'])
def deletecontact(contact_id):
    User.delete(contact_id)
    return redirect('/contacts')


@app.route('/editor', methods=['GET', 'POST'], defaults={'article_id': None})
@app.route('/editor/<article_id>', methods=['GET', 'POST'])
def editor(article_id):
    if request.method == 'POST':
        title = request.form.get("title")
        content = request.form.get("content")
        filename = None
        if 'main_image' in request.files:
            file = request.files['main_image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if article_id:
            article = Article.get(article_id)
            if filename: #change filename only if new file uploaded
                article.edit(article_id, title=title, content=content, main_image=filename)
            else:
                article.edit(article_id, title=title, content=content)
            return redirect('/editor')
        else:
            article = Article(title=title, content=content, main_image=filename)
            article.create()
            return redirect('/editor')
    articles = Article.fetch()
    if article_id:
        article = Article.get(article_id)
    else:
        article = None
    return render_template('editor.html', articles=articles, article=article)


@app.route('/viewer/<article_id>')
def viewer(article_id):
    article = Article.get(article_id)
    return render_template('viewer.html', article=article)

# ir ļoti svarīgi validēt failus pēc iespējas kārtīgāk, jo tas ir #1 problēmu cēlonis vēlāk
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run()
