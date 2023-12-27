import os
from flask import Flask, render_template, redirect
from flask_mysqldb import MySQL
from slugify import slugify

# pylint: disable=C0103
app = Flask(__name__)

@app.route('/')
def hello():
    message = "It's running!"

    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    return render_template('index.html',
        message=message,
        Service=service,
        Revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')

@app.route('/nosotros')
def nosotros():
    return 'Nosotros'
