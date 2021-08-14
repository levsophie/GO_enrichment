# import pandas as pd
# from flask import Flask, Response
# from flask import request as req
# from flask_restplus import Resource, Api
# import logging
# import urllib.request
# import urllib, json
# import requests
# import sqlite3
# from pandas.io import sql
# import ast
# import os.path
# from os import path
# from datetime import datetime
# from flask_restplus import reqparse
# from pprint import pprint
# from flask import abort, make_response, jsonify
# from flask import request

# app = Flask(__name__)
# api = Api(app)


# session = requests.Session()

# @api.response(200, "OK")
# @api.response(400, "Bad request")
# @app.route('/go', methods=['POST'])
# class AnalyseGeneList(Resource):

#     @api.doc("provide a list of genes")
#     def post(self):
#         """Analyse list of CNAG IDs"""
#         req = request.get_json(force=True)
#         genes = req.get('genes', None)
#         print(genes)
    
    
# if __name__ == '__main__':
#    app.run(host='127.0.0.1', port=5194)

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

app = Flask(__name__)
api = Api(app)


session = requests.Session()

class GenesDto:
    genes = api.model(
        "text",
        {
            "text_title": fields.List(fields.String),
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
    @api.expect(_genes, validate=True)
    # @api.marshal_with(_text, envelope="data")
    @api.doc()
    def post(self):
        req = request.get_json(force=True)
        print(req)
 

if __name__ == '__main__':
    app.run(debug=True)







 


