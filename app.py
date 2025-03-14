from flask import Flask, render_template
from config import config 
# from flask_sqlalchemy import SQLAlchemy


    
app = Flask(__name__)

def create_app(config_class=config):
    app.config.from_object(config_class)



@app.route('/index')
def index():
    return render_template ('index.html')

@app.route('/about')
def about():
    return render_template ('about.html')   

@app.route('/elementary')
@app.route('/')
def elementary():
    return render_template ('elementary.html')





if __name__ == '__main__':
    app.run(debug=True)
    