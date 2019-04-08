from flask import Flask

from routes import init_api_routes

app = Flask(__name__)

init_api_routes(app)

if __name__ == '__main__':
    app.run(debug=True)