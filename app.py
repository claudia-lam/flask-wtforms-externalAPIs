"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet

from forms import PetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get("/")
def show_homepage():
    """Show list of all pets."""

    pets = Pet.query.all()
    return render_template('pets/homepage.html', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = PetForm()

    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data or None,
            age=form.age.data,
            notes=form.notes.data
        )

        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template("pets/add.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Display pet details; Pet edit form; handle editing. """

    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)
    return render_template('pets/details.html', pet=pet, form=form)
    # if validate on submit
    # add to db
    # otherwise
    # get pet from db
    # render the form
