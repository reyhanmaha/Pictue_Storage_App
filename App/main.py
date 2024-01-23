from flask import Flask
from views import webViews

app= Flask(__name__)
for view in webViews:
    app.register_blueprint(view)
    
#app.register_blueprint(home_views)

if __name__=="__main__":
    app.run(debug=True)