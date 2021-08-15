
import sys 
sys.path.append('.')
import flask
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
from cnag_list_to_go import main_endpoint

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
search_parser = reqparse.RequestParser()
search_parser.add_argument("gene_list")

@api.route("/geneontology/<significance>",  methods=['POST'])
# @api.expect(_genes, validate=True)
@api.param("significance", "P-value cutoff")
@api.response(404, 'Not found')
@api.response(200, 'OK')
class Collections(Resource):
    # @api.expect(_genes, validate=True)
    @api.response(200, "OK")
    @api.response(400, "Bad request")
    @api.doc()
    # @api.doc(params={"significance":"P-value cutoff"})
    def post(self, significance):
        """Enter CNAG IDs in one line separated by comma"""
        print("Significance", significance)
        req = request.get_json(force=True)
        # print("Req", req)
        try:
            req = req['gene_list']
        except:
            pass
        return flask.jsonify(main_endpoint(req, significance))
        
@api.route("/geneontology/testcontrol",  methods=['POST'])
@api.response(404, 'Not found')
@api.response(200, 'OK')
class TestControl(Resource):
    @api.response(200, "OK")
    @api.response(400, "Bad request")
    @api.doc()
    def post(self):
        req = request.get_json(force=True)
        # print("Req", req)
        # main_endpoint(req['test'], req['control'], req['significance'])
        return flask.jsonify(main_endpoint(req['test'], req['control'], req['significance']))
        # return []
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)







 


