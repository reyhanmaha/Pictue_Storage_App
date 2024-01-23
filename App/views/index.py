from flask import render_template, Blueprint

home_views=Blueprint("home_views",__name__,template_folder='../templates')

@home_views.route("/",methods=['GET'])
def home():
    return render_template("index.html")