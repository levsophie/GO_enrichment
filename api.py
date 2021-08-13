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

class TextDto:
    text = api.model(
        "text",
        {
            "text_title": fields.String(required=True, description="text title"),
            "text_body": fields.String(required=True, description="text body"),
        },
    )
_text = TextDto.text
parser = reqparse.RequestParser()
parser.add_argument("words")

@api.response(404, 'Not found')
@api.response(200, 'OK')
@api.route('/genes',  methods=['POST'])
# @api.expect(parser, validate=True)
@api.expect(_text, validate=True)
class Collections(Resource):
    @api.response(200, "OK")
    @api.response(400, "Bad request")
    @api.expect(_text, validate=True)
    # @api.marshal_with(_text, envelope="data")
    @api.doc()
    def post(self):
        search_string = request.args.get("words")
        words = parser.parse_args()
       
        # req = request.get_json(force=True)
        # genes = req.get('genes', None)
        print(words)
        # data = request.json
        # print(request.args.keys())
        # return save_new_user(data=data)

if __name__ == '__main__':
    # run the application
    _text = TextDto.text
    app.run(debug=True)







 


