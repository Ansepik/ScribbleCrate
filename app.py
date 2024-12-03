from flask import Flask, render_template
from models import db
from auth import auth  # подключение Blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scribblecrate.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)
app.register_blueprint(auth)

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
