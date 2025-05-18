from flask import Flask, request, Response
from token_gen import generate_token
import pyfiglet

secret_key = "placeholder"

app = Flask(__name__)

@app.route('/template_easter_egg', methods=['GET'])
def hello_user():
    name = request.args.get('name')
    key = request.args.get('key')
    ascii_name = pyfiglet.figlet_format(name)
    user_key = name + key
    print(user_key)
    token = generate_token(user_key, secret_key) 
    response = f"Hello,\n{ascii_name}\nYou were here, this is your token: {token}\n"
    return Response(response, content_type='text/plain')
