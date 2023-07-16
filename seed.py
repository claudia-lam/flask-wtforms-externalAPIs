from app import app
from models import db, Pet

db.drop_all()
db.create_all()

pet_no_image_avail = Pet(
    name="jakers",
    species="dog",
    photo_url=None,
    age=10,
    available=True
)

pet_image = Pet(
    name="tabby",
    species="cat",
    photo_url="https://www.thesprucepets.com/thmb/uQnGtOt9VQiML2oG2YzAmPErrHo=/5441x0/filters:no_upscale():strip_icc()/all-about-tabby-cats-552489-hero-a23a9118af8c477b914a0a1570d4f787.jpg",
    age=1,
    available=True
)

db.session.add_all([pet_no_image_avail, pet_image])
db.session.commit()
