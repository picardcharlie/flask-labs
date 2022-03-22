from flask import Flask, render_template, redirect, url_for, session, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired
import zodiac_finder
import astrology
import datetime

# At this point, you have become familiar with defining, rendering, and adapting your view functions to forms and fields.
# To practice making more forms, you will create a new route that displays a form asking for date of birth.
# Upon submitting the form, you will flash a message to display their Zodiac sign or Chinese Zodiac animal.

# As you learned, you'll need a view function to create your form instance.
# Call your view function zodiac and make it a handler for the route '/zodiac'.

# use datetime.date to check data.


app = Flask(__name__)
app.config["SECRET_KEY"] = "dragondragondragon"
bootstrap = Bootstrap(app)

class BirthForm(FlaskForm):
    # How to force them to enter in a specific format?  Or do I make it cause errors until it's right format.
    #birthday = StringField("Enter birth year: ", validators = [DataRequired()])
    birthday = DateField("Enter your birthday", validators = [DataRequired()])
    submit = SubmitField("Enter")


@app.route("/zodiac", methods=["GET", "POST"])
def zodiac():
    form = BirthForm()
    if form.validate_on_submit():
        #session['year'] = form.birthday.data
        session['date'] = form.birthday.data
        # How do I use the form data here?  I want to run it in from the other py file.
        form_data = session['date']
        zodiac_sign = zodiac_finder.chinese_zodiac(form_data)
        astrology_sign = astrology.astro(form_data)
        flash("Your astrology sign is the " + astrology_sign)
        flash("Your Chinese Zodiac animal is the " + zodiac_sign)
        return redirect(url_for("zodiac"))
    return render_template("zodiac.html", form = form, year = session.get('year'))
