'''
PhD.:Eddy Giusepe Chirinos Isidro
'''
from flask import Flask, request
from flask_cors import CORS # Para poder fazer conexão desde qualquer parte do mundo
import torch
import numpy as np
from PIL import Image


app = Flask(__name__)
CORS(app) # para a conexão desde qualquer lugar do mundo

model = torch.jit.load('model.zip')

# Aqui a rota por DEFAULT é GET
@app.route('/')
def hello_world():
    return 'Hello, world!'


# Podemos fazer outra rota, assim:
@app.route("/predict", methods=["POST"])
def predict():
    
    # load image
    img = Image.open(request.files['file'].stream).convert('RGB').resize((224, 224)) # Mesmo tamanho 224x224 como foi treinado a Rede Neural 
    img = np.array(img)
    img = torch.FloatTensor(img.transpose((2, 0, 1)) / 255)

    # get predictions
    preds = model(img.unsqueeze(0)).squeeze()
    probas = torch.softmax(preds, axis=0)
    ix = torch.argmax(probas, axis=0)

    return {
        'label': model.labels[ix],
        'score': probas[ix].item()
    }

# Podemos fazer na terminal, também, assim:
# ...$ curl http://127.0.0.1:5000/ 

if __name__ == '__main__':
    app.run() 

