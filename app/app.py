from flask import Flask
from flask_openid import OpenID

app = Flask(__name__)

oid = OpenID(app);


@app.route('/', methods=['GET'])
def index():
    isAuth = True;

    user_info = "default"

    # authenticate ??


    # respond

    if(isAuth):
        return "current user: " + user_info
    else:
        abort(401)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="80")
