from flask import Flask , render_template,url_for         # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return render_template("index.html")        # which returns "hello world"

# @app.route("/login")
# def login():
#     return "login page"
# @app.route("/register")
# def register():
#     return "register page"

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app