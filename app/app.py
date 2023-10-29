"""
    Defines the functionality for the backend [namely the endpoints being 
    called in the front-end].
"""


# ----------------- Environment Setup ----------------- #
import json
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)


# ----------------- Endpoint Wrappers ----------------- #
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
    def post_video(self):
        


api.add_resource(SYM_Processor, "./sym-processor")


# ----------------- Feature Iteration & Testing ----------------- #
if __name__ == "__main__":
    # run app
    app.run()

