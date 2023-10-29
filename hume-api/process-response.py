"""
    Functionality for processing the HUME response.
"""

# ----------------- Environment Setup ----------------- #
import json
import pandas as pd


# ----------------- Processing Functionality ----------------- #
"""
    Generates a database for displaying graphs, running metrics, etc.
"""
def gen_df(hume_response: dict) -> pd.DataFrame:
    # setup
    expression_set = {"emotions"}               # "facs", "descriptions" will be added later
    model_set = {"face", "language", "prosody"} # "burst", etc. may be added later
    narrowed_dict = dict()

    # check errors
    if len(hume_response[0]["results"]["errors"]) > 0:
        raise Exception("Oops! The underlying process [powered by Hume AI] ran "
                        "into some issues while processing your data. Sorry for "
                        "the inconvenience, we'll try fixing this ASAP!")

    # setup db
    df = pd.DataFrame(columns=[
        "timestamp",
        "model",
        "confidence",
        "expression-set",
        "raw-media",
        "emotion",
        "score"
    ])

    # generate narrowed data & dataframe
    for model_name in model_set:
        for expression_name in expression_set:
            # grab data
            if model_name not in narrowed_dict:
                narrowed_dict[model_name] = dict()
            narrowed_model_expression = hume_response[0]["results"]["predictions"][0]["models"][model_name]["grouped_predictions"][0]["predictions"][0]["emotions"]
            narrowed_dict[model_name][expression_name] = narrowed_model_expression

            # unpack data
            emotion_names = [d["name"] for d in narrowed_model_expression]
            emotion_scores = [d["score"] for d in narrowed_model_expression]

            # add rows
            model_name_col = [model_name] * len(emotion_names)
            expression_name_col = [expression_name] * len(emotion_names)
            timestamp_col = [hume_response[hume_response[0]["results"]["predictions"][0]["models"][model_name]["grouped_predictions"][0]["predictions"][0]["time"]]]

            # 
    

"""
    Converts a given time dictionary.
"""
def conv_time(time_dict: dict) -> str:
    return 

