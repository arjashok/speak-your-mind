"""
    Functionality for wrapping the hume-api calls in an easy & modularized way.
"""

# ----------------- Environment Setup ----------------- #
import requests
import json
import asyncio
from hume import HumeBatchClient
from hume.models.config import FaceConfig
from hume.models.config import ProsodyConfig

# ----------------- API Functionality ----------------- #
# """
#     Sets the default payload characteristics for the function.
# """
# def default_payload() -> dict:
#     # default params
#     params_to_define = [
#         "models",
#         "transcription",
#         "notify"
#     ]
#     param_values = [
#         {
#             "face": {
#                 "fps_pred": 1,
#                 "prob_threshold": 0.9,
#                 "identify_faces": False,
#                 "min_face_size": 60,
#                 "facs": {},
#                 "descriptions": {},
#                 "save_faces": False
#             }
#             "burst": {},
#             "prosody": {
#                 "granularity": "utterance",
#                 "window": {
#                     "length": 4,
#                     "step": 1
#                 }
#             },
#             "language": {
#                 "granularity": "word"
#             }
#         },
#         {
#             "language": null,
#             "identify_speakers": false,
#             "confidence_threshold": 0.5
#         },
#         False
        
#     ]
    
#     return dict(zip(params_to_define, param_values))



"""
    Pushes the request to HUME and returns the [processed] output.
"""
async def gen_hume_analysis(params: dict):
    client = HumeBatchClient(f"{params[API_KEY]}")
    urls = [f"{params[VIDEO_URL]}"]
    configs = [FaceConfig(fps_pred=1, prob_threshold = 0.9, identify_faces=False), ProsodyConfig()]
    job = client.submit_job(urls, configs)

    job.await_complete()
    job.download_predictions("predictions.json")

