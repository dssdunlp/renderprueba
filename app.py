from flask import Flask
import os
from flask import request

app = Flask(__name__)

@app.route('/hello')
def index():
    args=request.args
    param1=args["nombre"] 
    return "Hello, is this a "+ param1

if __name__ == '__main__':
    # gets Heroku's suggested port out of the environment dictionary if exists:
    port = int(os.environ.get('PORT', 8080))
    # this is the wsgi hook:
    app.run(host='0.0.0.0', port=port)
