import os.path

from flask import jsonify, request

file_name = 'saved_number'
num = 0
followers = 0
password = 'hola'


def try_number():
    if not request.json:
        return jsonify({'message': 'todo mal'}), 400

    code = request.json.get('code', None)

    if not code:
        return jsonify({'message': 'send any code'}), 400

    ok, number = get_number(code)
    if not ok:
        return jsonify({'message': 'is not correct'}), 200

    global num
    global followers
    num = num + number
    followers = followers + 1

    update_file()

    if not number_check(num, 11):
        return jsonify({'message': 'prueba otra vez'}), 200

    return jsonify({'message': 'has ganado'}), 200


def check_file():

    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            # 3,129 --> 3 followers, 129 num
            global num
            global followers
            followers, num = f.readline().split(',')
            num = int(num)
            followers = int(followers)

    else:
        with open(file_name, 'w') as f:
            f.write('0,0')


def update_file():
    with open(file_name, 'w') as f:
        f.write('{},{}'.format(followers, num))


def get_number(code):
    code = code.lower()
    if code.startswith(password):
        _, number = code[0:len(password)], code[len(password):]
        try:
            number = int(number)
            if number >= 100 and number < 1000:
                return True, number
            return False, None
        except:
            return False, None

    return False, None


def number_check(follower_number, number):
    if follower_number % number == 0:
        return True
    else:
        return False

def num_followers():
    return jsonify({'message': str(followers)}), 200
    
