from getpass import getpass
import sys


from webapp import create_app
from webapp.db import db
from webapp.news.models import User

app = create_app()

with app.app_context():
    username = input('Enter name:')

    if User.query.filter(User.username == username).count():
        print('The user hve already exist')
        sys.exit(0)

    password1 = getpass('Enter password:')
    password2 = getpass('Repeat password:')

    if not password1 == password2:
        print('passwords dont the same')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('Created new user with id={}'.format(new_user.id))
