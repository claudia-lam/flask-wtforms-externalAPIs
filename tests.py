from models import Pet
from app import app, db
from unittest import TestCase
import os

os.environ["DATABASE_URL"] = "postgresql:///adoption_test"


# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

# Disable CSRF
app.config['WTF_CSRF_ENABLED'] = False

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()


class PetViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        # As you add more models later in the exercise, you'll want to delete
        # all of their records before each test just as we're doing with the
        # User model below.

        Pet.query.delete()

        self.client = app.test_client()

        test_pet = Pet(
            name="test_pet",
            species="test_species",
            photo_url=None,
            age="young",
            available=False
        )

        db.session.add(test_pet)
        db.session.commit()

        # We can hold onto our test_user's id by attaching it to self (which is
        # accessible throughout this test class). This way, we'll be able to
        # rely on this user in our tests without needing to know the numeric
        # value of their id, since it will change each time our tests are run.
        self.pet_id = test_pet.id
        # print("test-1-user-id", self.user_id)

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()

    def test_show_homepage(self):
        with self.client as c:
            resp = c.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("test_pet", html)
            self.assertIn(f"is not available", html)
            self.assertIn("Add Pet", html)

    def test_show_add_pet_form(self):
        with self.client as c:
            resp = c.get("/add")
            html = resp.text

            self.assertEqual(resp.status_code, 200)
            self.assertIn("""<form id="pet-add-form" method="POST">""", html)
            self.assertIn("porcupine", html)

    def test_add_pet(self):
        with self.client as c:
            resp = c.post("/add", data={
                "name": "test_pet_2",
                "species": "dog",
                "photo_url": "",
                "age": "baby"
            }, follow_redirects=True)

            html = resp.text

            self.assertEqual(resp.status_code, 200)
            self.assertIn("test_pet_2", html)
