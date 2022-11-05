'''
PhD.:Eddy Giusepe Chirinos Isidro
'''

from flask import Flask
from flask_cors import CORS # Para poder fazer conexão desde qualquer parte do mundo

app = Flask(__name__)
CORS(app) # para a conexão desde qualquer lugar do mundo


@app.route('/')
def hello_world():
    return 'Hello, world!'


# Podemos fazer outra rota, assim:
@app.route("/predict")
def predict():
    return 'predições'


    

if __name__ == '__main__':
    app.run() 

