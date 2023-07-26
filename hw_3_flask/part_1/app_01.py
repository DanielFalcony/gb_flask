from flask import Flask
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

# in terminal, type "flask init-db" for creating db from models
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('DB OK!')


if __name__ == '__main__':
    app.run(debug=True)
