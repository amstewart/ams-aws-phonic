#! /usr/bin/env python3

from flask import Flask, make_response
from flask_restful import Resource, Api

# Flask Initialization
app = Flask(__name__)
api = Api(app, default_mediatype='application/xml')

@api.representation('application/xml')
def output_xml(data, code, headers=None):
    resp = make_response(data, code)
    resp.headers.extend(headers or {})
    return resp

#################
# API Resources #
#################

class Voice(Resource):
    def get(self):
        with open('twiml/reject-voice.xml', 'r') as fp_response:
            return fp_response.read()

################
# Flask Routes #
################

api.add_resource(Voice, '/voice')


if __name__ == "__main__":
    app.run(debug=True)
