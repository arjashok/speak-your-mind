"""
    Functionality for processing the HUME response.
"""

# ----------------- Environment Setup ----------------- #
import json
import pandas as pd


# ----------------- Processing Functionality ----------------- #
"""
    Wraps the entire functionality for processing the response from Hume into 
    human-readable metrics.

    This will return a dictionary of the metrics to graph, plus the extracted 
    information from raw as a dictionary
"""
def process_hume_response(hume_response_raw: str) -> tuple:
    # convert raw
    hume_response = json.loads(hume_response_raw)

    # generate data for graphs
    metrics_df = gen_df(hume_response)


"""
    Generates the metrics for displaying graphs and prompt engineering for the 
    user feedback.
"""
def gen_metrics()


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
            narrowed_model_expression = hume_response[0]["results"]["predictions"][0]["models"][model_name]["grouped_predictions"][0]["predictions"][0][expression_name]
            narrowed_dict[model_name][expression_name] = narrowed_model_expression

            # unpack data
            emotion_names = [d["name"] for d in narrowed_model_expression]
            emotion_scores = [d["score"] for d in narrowed_model_expression]
            col_length = len(emotion_scores)

            narrowed_data = hume_response[0]["results"]["predictions"][0]["models"][model_name]["grouped_predictions"][0]["predictions"][0]
            timestamp = [gen_timestamp(narrowed_data["time"])] * col_length
            
            try:
                confidence = [hume_response[0]["results"]["predictions"][0]["models"][model_name]["metadata"]["confidence"]] * col_length
            except:
                confidence = ["NA"] * col_length

            # add to df
            df = pd.concat([df, pd.DataFrame({
                "timestamp": timestamp,
                "model": [model_name] * col_length,
                "confidence": confidence,
                "expression-set": [expression_name] * col_length,
                "raw-media": [narrowed_data["text"] if model_name != "face" else "NA"] * col_length,
                "emotion": emotion_names,
                "score": emotion_scores
            })], ignore_index=True)

    # cache df
    return df
    

"""
    Converts a given time dictionary.
"""
def gen_timestamp(time_dict: dict) -> str:
    return "00:00:00"

