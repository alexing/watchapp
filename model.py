from flask import Flask
from flask import request
import pandas as pd
import numpy as np
import dill,json

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
    print (str(arg_dict))
    sentence = arg_dict['sentence']
    user = arg_dict['user']

    res = '<html><head>'
    clf = get_model()
    prediction = clf.predict(sentence)
    prob = str(clf.prob_to_bully)
    res += '<p>The sentence "' + \
           sentence.replace('_', ' ') + \
           '" is bully: ' +str(prediction) + \
    ' with prob: ' + prob + \
    '<br></>'
    res += '</><ERITY/: >'
    return json.dumps({"STATUS":str(prediction), "MSG":sentence, "USER":user, "SEVERITY": prob})

if __name__ == '__main__':
    app.run()


