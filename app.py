from flask import Flask
import os
from flask import request

app = Flask(__name__)

@app.route('/hello')
def index():
    args=request.args
    param1=args["name"] 
    return "Hello, ESTO ES UNA PRUEBA PARA DSSD DE: "+ param1

port = int(os.environ.get("PORT", 8000)) 
app.run(host='0.0.0.0', port=port) 
