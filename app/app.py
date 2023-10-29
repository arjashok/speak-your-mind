"""
    Defines the functionality for the backend [namely the endpoints being 
    called in the front-end].
"""


# ----------------- Environment Setup ----------------- #
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir + "/hume-api/")
sys.path.append(parent_dir + "/facial-recog/")
sys.path.append(parent_dir + "/gen-feedback/")
sys.path.append(parent_dir + "/app/")

import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
# import pandas as pd
import ast
from enum import Enum
app = Flask(__name__)
CORS(app)
api = Api(app)

# from hume-api import *


# ----------------- Endpoint Wrappers ----------------- #
"""
    Classes for interpreting inputs & outputs.
"""
class Content_Type(Enum):
    SPEAKER = 0
    AUDIENCE = 1
    SPEAKERAUDIENCE = 2


"""
    Class to wrap all methods.
"""
class SYM_Processor(Resource):

    """
        Receives POST response, wraps all necessary calls:

        Dispatcher :: handles the full API request, will return the full text 
                    analysis + pointers, and a JSON with timestamps of each 
                    event/emotion/pointer
        
                :: We’ll obtain input from the web app in the form of a video, 
                    string prompt, and analysis type [speaker, audience, speaker 
                    + audience] ⇒ JSON
                
                        :: This analysis type can later be inferred from number of 
                        faces, lighting, etc. but for simplicity and iteration 
                        sake we can do this for now
        
                :: Throughout this process, we’ll be generating a dictionary of 
                    timestamps [int]: sentiment-analysis [dictionary] that’ll 
                    later be a key output point
                    
                :: We’ll dispatch the facial recognition, gather results, and 
                    separate the input into audience and speaker frames
                        :: For each one of those frames, we’ll dispatch the given 
                        Hume Analysis wrapper that then provides the final 
                        verdicts for each frame
                        :: This will be a JSON/dictionary that associates key 
                        emotions/thoughts with the frame
    """
    def post(self) -> dict:
        request_data = request.json
        if not request_data or 'request_content' not in request_data or 'target' not in request_data:
            return jsonify({
                "status": "error",
                "message": "Invalid request data. Please provide 'request_content' and 'target'."
            }), 400
        request_content = request_data["request_content"]
        target = request_data["target"]
        print(request_content + "\n")
        print(target + "\n")

        # dispatcher
        # dispatch_params = {
        #    "API-KEY": "9BAoszAhvQSgWLIttRJHlBJRHavk4NWOzfZQUTrDSATB5RFu",
        #    "CONTENT-TYPE": request_params["content-type"]
        #}
        
        # hume_response = gen_hume_analysis()
        return {
            "appreciation": "5",
            "impact": "67",
            "confidence": "43",
            "engagement": "21",
            "feedback": "Hello There, this is the analysis of your speech. It does quite well for itself"
        }, 200



api.add_resource(SYM_Processor, "/sym-processor")


# ----------------- Feature Iteration & Testing ----------------- #
if __name__ == "__main__":
    # run app
    app.run()

