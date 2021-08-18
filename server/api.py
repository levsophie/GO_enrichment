
import sys 
sys.path.append('.')
import flask
from flask import Flask, request
from flask_restplus import Resource, Api
import requests
import flask_cors
from cnag_list_to_go import main_endpoint, more_GO_info

app = Flask(__name__)
cors = flask_cors.CORS()
cors.init_app(app)
api = Api(app)
session = requests.Session()

@api.route("/geneontology/<significance>",  methods=['POST'])
@api.param("significance", "P-value cutoff")
@api.response(404, 'Not found')
@api.response(200, 'OK')
class GoEnrichment(Resource):
    @api.response(200, "OK")
    @api.response(400, "Bad request")
    def post(self, significance):
        """CNAG IDs in a list"""
        print("Significance", significance)
        req = request.get_json(force=True)
        return flask.jsonify(main_endpoint(req, [], significance))
        
        
@api.route("/geneontology/terms",  methods=['POST'])
@api.response(404, 'Not found')
@api.response(200, 'OK')
class GoDetails(Resource):
    @api.response(200, "OK")
    @api.response(400, "Bad request")
    def post(self):
        """Get details for test and control samples for the specific GO term"""
        req = request.get_json(force=True)
        print("Term", req['term'])
        return flask.jsonify(more_GO_info(req['gene_list'], req['term']))

        
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)







 


