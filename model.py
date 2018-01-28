from flask import Flask
from flask import request
import pandas as pd
import numpy as np
import dill
from sklearn.metrics import roc_curve
app = Flask(__name__)


def get_model():
    model_file_path = r'model.pickle'
    with open(model_file_path, 'rb') as file:
        model = dill.load(file)
    return (model)


@app.route('/sentence/', methods=['GET'])
def bully_predictor():
    arg_dict = request.args.to_dict()
    sentence = arg_dict['sentence']
    res = '<html><head>'
    clf = get_model()
    prediction = clf.predict(sentence)
    res += '<p>The sentence "' + \
           sentence.replace('_', ' ') + \
           '" is bully: ' +str(prediction) + \
    ' with prob: ' + str(clf.prob_to_bully) + \
    '<br></>'
    res += '</></>'
    return res


