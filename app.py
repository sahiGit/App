import platform
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = "Hello, World!\n"
    message += "Operating System: " + platform.system() + "\n"
    message += "Current Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return message

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
