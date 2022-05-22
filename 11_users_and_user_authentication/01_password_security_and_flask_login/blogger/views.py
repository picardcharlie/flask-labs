from flask import Flask, request, session, redirect, url_for, render_template, flash, jsonify

from . models import User, Post, db
from . forms import AddPostForm, SignUpForm, SignInForm, AboutUserForm
from flask_login import login_required, logout_user, login_user, current_user
from blogger import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def show_posts():
    if current_user.is_authenticated:
        posts = Post.query.all()
        user = User.query.all()
        return render_template('posts.html', posts=posts, user=user)
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if current_user.is_authenticated:
        blogpost = AddPostForm()
        us = User.query.filter_by(email=current_user.email).first()
        if request.method == 'POST':
            bp = Post(blogpost.title.data, blogpost.description.data, us.id)
            db.session.add(bp)
            db.session.commit()
            return redirect(url_for('show_posts'))
        return render_template('add.html', blogpost=blogpost)
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/delete/<pid>/<post_owner>', methods=('GET', 'POST'))
def delete_post(pid, post_owner):
    if session['current_user'] == post_owner:
        me = Post.query.get(pid)
        db.session.delete(me)
        db.session.commit()
        return redirect(url_for('show_posts'))
    flash('You are not a valid user to Delete this Post')
    return redirect(url_for('show_posts'))


@app.route('/update/<pid>/<post_owner>', methods=('GET', 'POST'))
def update_post(pid, post_owner):
    if current_user.is_authenticated:
        me = Post.query.get(pid)
        blogpost = AddPostForm(obj=me)
        if request.method == 'POST':
            bpost = Post.query.get(pid)
            bpost.title = blogpost.title.data
            bpost.description = blogpost.description.data
            db.session.commit()
            return redirect(url_for('show_posts'))
        return render_template('update.html', blogpost=blogpost)
    flash('You are not a valid user to Edit this Post')
    return redirect(url_for('show_posts'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signupform = SignUpForm()
    if signupform.validate_on_submit():
        reg = User(signupform.firstname.data, signupform.lastname.data, signupform.username.data, signupform.password.data, signupform.email.data)
        db.session.add(reg)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', signupform=signupform)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    signinform = SignInForm()
    if signinform.validate_on_submit():
        login_username = signinform.email.data
        login_password = signinform.password.data
        check_login_user = User.query.filter_by(email=login_username).first()
        if check_login_user is not None:
            if check_login_user.email == login_username and check_login_user.verify_password(login_password) == True:
                login_user(check_login_user, remember=signinform.remember_me.data)
                next = request.args.get("next")
                if next is None or not next.startswith("/"):
                    next = url_for("show_posts")
                return redirect(next)
            else:
                flash("username and password don't match.")
        else:
            flash("username not found.")
    return render_template('signin.html', signinform=signinform)


@app.route('/about_user')
@login_required
def about_user():
    aboutuserform = AboutUserForm()
    return render_template('about_user.html', user=user, aboutuserform=aboutuserform)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
