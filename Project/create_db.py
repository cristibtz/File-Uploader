import time
from Files import db, create_app

app = create_app()

time.sleep(5)

with app.app_context():
    db.create_all()