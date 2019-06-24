from flask import Flask
from flask_cors import CORS
from contest import file_name, try_number, check_file, num_foll, render_template, main_site


def setup_app():
    app = Flask(__name__, template_folder='templates')
    CORS(app=app, supports_credentials=True)

    # SETUP URLS
    app.add_url_rule('/', methods=['GET'], view_func=main_site)
    app.add_url_rule('/followers', methods=['GET'], view_func=num_foll)
    app.add_url_rule('/api/try_number', methods=['POST'], view_func=try_number)

    return app


if __name__ == '__main__':
    app = setup_app()
    check_file()
    app.run(host='0.0.0.0', port=5000, threaded=True)

# python app.py
# curl -X GET -H http://localhost:5000/main
# curl -X POST -H 'Content-Type: application/json' -d '{"code": "hola120"}' http://localhost:5000/try_number
# curl -X GET -H -d http://localhost:5000/num_followers
