
import pandas as pd
from flask import Flask, Response, request
from flask import request as req
from flask_restplus import Resource, Api
import logging
import urllib.request
import urllib, json
import requests
import sqlite3
from pandas.io import sql
import ast
import os.path
from os import path
from datetime import datetime
from flask_restplus import reqparse
from pprint import pprint
from flask import abort, make_response, jsonify
from flask_restx import Namespace, fields
import flask_cors

app = Flask(__name__)
cors = flask_cors.CORS()
cors.init_app(app)
api = Api(app)


session = requests.Session()

class GenesDto:
    genes = api.model(
        "genes",
        {
            "gene_list": fields.String,
        },
    )
_genes = GenesDto.genes


@api.response(404, 'Not found')
@api.response(200, 'OK')
@api.route('/genes',  methods=['POST'])
@api.expect(_genes, validate=True)
class Collections(Resource):
    @api.response(200, "OK")
    @api.response(400, "Bad request")
    # @api.expect(_genes, validate=True)
    # @api.marshal_with(_text, envelope="data")
    @api.doc()
    def post(self):
        req = request.get_json(force=True)
        print(req)
        return [
      {
        "id": 1,
        "pvalue": 0.0004,
        "test": 10,
        "control": 10,
        "description": "very interesting GO group",
      },
    ]

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)







 


