from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Feedback
from forms import AddRegistrationForm, LoginForm, FeedbackForm

# app created 
app = Flask(__name__)

# specify that youre using postgres and a specific database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretsecret1282021"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#call connect_db from models
connect_db(app)
db.create_all()

@app.route('/')
def homepage():
    """show homepage"""

    return redirect('/login')

@app.route('/register', methods=["GET","POST"])
def register():
    """Registeration form for new user"""
    form = AddRegistrationForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data

        user = User.register(username, password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        db.session.add(user)
        db.session.commit()

        # set user to session
        session['curr_user'] = user.username

        return redirect('/secret')
    else:
        return render_template('register.html', form=form)

@app.route('/secret')
def show_secret_pg():
    """Secret page for logged-in users only """
    if "curr_user" not in session:
        return redirect('/login')
         
    else:
        return render_template('secret.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            session['curr_user'] = user.username

            return redirect(f"/users/{user.username}")
        else:
            form.username.errors = ['invalid username or password!']

    return render_template('login.html',  form=form)

@app.route('/users/<curr_user>')
def display_user_info(curr_user):
    """Display user information"""

    form = FeedbackForm()
    if 'curr_user' in session:
        user = User.query.get_or_404(curr_user)

        return render_template('user_info.html', user=user, form=form)

    else:
        return redirect('/login')

@app.route('/users/<curr_user>/delete', methods=["POST"])
def delete_user(curr_user):
    """Delete user"""
    
    user = User.query.get_or_404(curr_user)
    if 'curr_user' in session and session['curr_user'] == user.username:
        user.delete()
        db.session.commit()

    return redirect('/')

@app.route('/users/<curr_user>/feedback/add', methods=["GET", "POST"])
def add_feedback(curr_user):
    """check for curr user and display feedback form"""
    user = User.query.get_or_404(curr_user)
    if 'curr_user' not in session:
        return redirect('/login')

    else:
        form = FeedbackForm()
        if form.validate_on_submit():
            title = form.title.data
            content = form.feedback.data

            # create new instance of feedback
            feedback = Feedback(title=title, content=content, username=user.username)
            db.session.add(feedback)
            db.session.commit()

    return render_template('feedback_form.html', form=form, user=user)
    
@app.route('/feedback/<int:feedback_id>/update', methods=["GET","POST"])
def edit_feedback(feedback_id):
    f = Feedback.query.get_or_404(feedback_id)
    
    if 'curr_user' in session:
        s = session['curr_user']
        if s == f.username:
            form = FeedbackForm(obj=f)
            if form.validate_on_submit():
                f.title = form.title.data
                f.content = form.feedback.data
                db.session.commit()
    return render_template('edit_feedback.html',form=form,f=f)


# feedback post delete route
# fix user delete
# add btns for delete

@app.route('/logout')
def logout_user():
    session.pop('curr_user')
    return redirect('/login')