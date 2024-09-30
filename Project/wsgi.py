import time
from Files import create_app, db

app = create_app()

time.sleep(5)

with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run()