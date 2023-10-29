"""
    Helper program to generate the Ted Talk, Speaker, & Celebrity talk video 
    qualitative data.
"""


# ----------------- Environment Setup ----------------- #
import json
import pandas as pd


# ----------------- Input Info ----------------- #
if __name__ == "__main__":
    # constants
    cols = [
        "video-name",
        "presenter-name",
        "trait-name",
        "is-trait-present"
    ]
    audience_emotional_categories = [
        "Appreciation",
        "Engagement",
        "Impact",
    ]
    speaker_emotional_categories = [
        "Confidence"
    ]

    with open("hume-expressions.json", "r") as f:
        hume_expressions = json.load(f)
    
    with open("grouped-expressions.json", "r") as f:
        grouped_expressions = json.load(f)

    # setup db
    df = pd.read_csv("quant-tracker.csv")

    # append to db
    while input("Add another video [y/n]: ") == 'y':
        # get info
        vid_name = str(input("video name: "))
        pres_name = str(input("presenter name: "))

        # traits info
        traits_dict = dict()
        for trait in hume_expressions:
            trait_val = str(input(f"is {trait} present in {vid_name} [y/n]: ")) == 'y'
            new_row = dict(zip(cols, [vid_name, pres_name, trait, trait_val]))
            traits_dict.update(new_row)

        # add to pandas dataframe
        df = df.append(traits_dict, ignore_index=True)
    
    # save to csv
    df.to_csv("quant-tracker.csv", index=False)

