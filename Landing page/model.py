# from flask import Flask
# from flask import request
from bottle import route, template, static_file, run, request
from sys import argv
import pandas as pd
import numpy as np
import dill, json
import time

from sklearn.metrics import roc_curve
# app = Flask(__name__)


dic = {[]}

model = None
with open(r'model.pickle', 'rb') as file:
    model = dill.load(file)


def get_model():
    return model


@route('/', method='GET')
def index():
    return template("watchApp_index.html")

@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')

@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


@route('/sentence_get/', methods=['GET'])
def send_dict_to_front_end():
    content = dic[0]
    dic = {[]}
    return json.dumps(content)


@route('/sentence/', methods=['GET'])
def bully_predictor():
    # arg_dict = request.args.to_dict()
    arg_dict = request.query.dict
    print (str(arg_dict))
    sentence = arg_dict['sentence'][0]
    user = arg_dict['user'][0]

    clf = get_model()
    prediction = clf.predict(sentence)[0]
    prob = clf.prob_to_bully[0]
    if prediction:
        dic[0].append({'prediction': prediction, 'prob': prob})


def main(host="0.0.0.0", port=None):
    if not port:
        port = argv[1]
    run(host=host, port=port)

    while True:
        time.sleep(0.5)
        bully_predictor()

if __name__ == '__main__':
    main(host="localhost", port=7000)  # run on localhost
    #main()