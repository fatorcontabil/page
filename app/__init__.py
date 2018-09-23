from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def index():
    return render_template("home.html")

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# from app.mod_cad.controllers import mod_cad as cad_module
# from app.mod_home.controllers import mod_home as home_module

# app.register_blueprint(cad_module)
# app.register_blueprint(home_module)
