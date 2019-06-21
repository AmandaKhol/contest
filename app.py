from flask import Flask
from flask_cors import CORS
from contest import file_name, try_number, check_file, num_foll, render_template


def setup_app():
    app = Flask(__name__)
    CORS(app=app, supports_credentials=True)

    # SETUP URLS
    app.add_url_rule('/try_number', methods=['POST'], view_func=try_number)
    app.add_url_rule('/followers', methods=['GET'], view_func=num_foll)

    return app


if __name__ == '__main__':
    app = setup_app()
    check_file()
    app.run(host='0.0.0.0', port=5000, threaded=True)

# python app.py
# curl -X POST -H 'Content-Type: application/json' -d '{"code": "hola120"}' http://localhost:5000/try_number
# curl -X GET -H -d http://localhost:5000/num_followers
