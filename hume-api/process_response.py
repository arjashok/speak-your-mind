"""
    Functionality for processing the HUME response.
"""

# ----------------- Environment Setup ----------------- #
import json
import pandas as pd
import matplotlib.pyplot as plt


# ----------------- Processing Functionality ----------------- #
"""
    Wraps the entire functionality for processing the response from Hume into 
    human-readable metrics.

    This will return a dictionary of the metrics to graph, plus the extracted 
    information from raw as a dictionary
"""
def process_hume_response(hume_response) -> tuple:
    # parameter setup
    expression_set = {"emotions"}               # "facs", "descriptions" will be added later
    model_set = {"face", "prosody"}             # "language", "burst", etc. may be added later

    # convert raw
    if isinstance(hume_response, str):
        hume_response = json.loads(hume_response)

    # generate data for graphs & visuals
    metrics_df = gen_df(hume_response, model_set, expression_set)
    return gen_metrics(metrics_df)


"""
    Generates the metrics for displaying graphs and prompt engineering for the 
    user feedback.
"""
def gen_metrics(df: pd.DataFrame):
    # process pre-processed data
    processed_df = transform_metrics(df)
    processed_df = processed_df[["emotion-group", "abs-score"]]
    return processed_df.to_dict()


"""
    Transforms the pre-processed data into format that's easier to work with for 
    plotting & metrics calculation.

    timestamp vs aggregated metrics
"""
def transform_metrics(df: pd.DataFrame):
    # setup metrics by grouping
    with open("grouped-expressions.json", "r") as f:
        grouped_metrics = json.load(f)
    
    unique_times = list(df["timestamp"].unique())

    # for each unique time, we'll generate the aggregate of each group 
    # expression that we have qualitatively determined to be useful to the user 
    # and most indicative of speech performance
    # df.groupby("timestamp")["emotion"].mean().reset_index()

    # for timestamp in unique_times:
    #     # narrow data
    #     narrow_df = df[df["timestamp"] == timestamp]

    #     # for each row, we want the net and abs sum of the thing
    #     # 
    #     row_data = dict.fromkeys(grouped_expressions)

    #     # aggregate metrics
    #     for grouped_expression, expression_weights in grouped_expressions.items():
    #         for expression_info in expression_weights:
    #             for expression_name, expression_weight in expression_info:
    #                 row_data[narrow_df[narrow_df["emotion"] == expression_name]["score"]
    
    return timeslice_metrics(df, grouped_metrics)


"""
    Generates the time-slice performance, allowing for more modularity and 
    future feature inclusion.
"""
def timeslice_metrics(narrow_df: pd.DataFrame, grouped_metrics: dict) -> pd.DataFrame:
    # setup
    grouped_expressions = list(grouped_metrics.keys())

    # we'll generate the aggregate of each group expression that we have 
    # qualitatively determined to be useful to the user and most indicative of 
    # speech performance
    narrow_df = narrow_df.groupby("emotion")["score"].mean().reset_index()

    # generate accumulated metrics
    cols = [
        "emotion-group",
        "net-score",
        "abs-score"
    ]
    processed_metrics = pd.DataFrame(columns=cols)                          # each timestamp is a unique entry w/ agg metrics
    
    for grouped_expression in grouped_expressions:
        # track aggregates
        net_sum = 0
        abs_sum = 0

        # sum for each expression
        for pairwise_weight in grouped_metrics[grouped_expression]:
            for expression in pairwise_weight:
                weight = pairwise_weight[expression]
                net_sum += weight
                abs_sum += abs(weight)
        
        # add to tracker
        processed_metrics = pd.concat([
            processed_metrics,
            pd.DataFrame(dict(zip(cols, [[grouped_expression], [net_sum * 1.5], [abs_sum * 1.5]])))
        ])

    # export
    return processed_metrics



"""
    Generates a database for displaying graphs, running metrics, etc.
"""
def gen_df(hume_response: dict, model_set: list, expression_set: list) -> pd.DataFrame:
    # setup
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
        # for each frame
        for frame_num in range(len(hume_response[0]["results"]["predictions"][0]["models"][model_name]["grouped_predictions"][0]["predictions"])):
            # for every hume output generated
            for expression_name in expression_set:
                # grab data
                if model_name not in narrowed_dict:
                    narrowed_dict[model_name] = dict()
                narrowed_model_expression = hume_response[0]["results"]["predictions"][0]["models"][model_name]["grouped_predictions"][0]["predictions"][frame_num][expression_name]
                narrowed_dict[model_name][expression_name] = narrowed_model_expression

                # unpack data
                emotion_names = [d["name"] for d in narrowed_model_expression]
                emotion_scores = [d["score"] for d in narrowed_model_expression]
                col_length = len(emotion_scores)

                narrowed_data = hume_response[0]["results"]["predictions"][0]["models"][model_name]["grouped_predictions"][0]["predictions"][frame_num]
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
    Converts a given time dictionary or raw time.
"""
def gen_timestamp(time_raw) -> str:
    # convert if dict
    if isinstance(time_raw, dict):
        time_raw = time_raw["begin"]

    # convert format
    hours = int(time_raw // 3600)
    minutes = int((time_raw % 3600) // 60)
    seconds = float(time_raw % 60)

    # Format the result as "hh:mm:ss"
    return f"{hours:02d}:{minutes:02d}:{seconds:0.2f}"


# ----------------- Processing Functionality ----------------- #
if __name__ == "__main__":
    with open("predictions.json", "r") as f:
        hr = json.load(f)

    process_hume_response(hr)
