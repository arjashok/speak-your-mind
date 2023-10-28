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

    emotional_categories = ["Appreciation", "Engagement", "Impact", "Confidence"]
    grouped_expressions = {
        "Appreciation": [
            {"Admiration": 1},
            {"Adoration": 1},
            {"Aesthetic Appreciation": 1},
            {"Amusement": 1},
            {"Anger": 1},
            {"Annoyance": 1},
            {"Anxiety": 1},
            {"Awe": 1},
            {"Awkwardness": 1},
            {"Boredom": 1},
            {"Calmness": 1},
            {"Concentration": 1},
            {"Confusion": 1},
            {"Contemplation": 1},
            {"Contempt": 1},
            {"Contentment": 1},
            {"Craving": 1},
            {"Desire": 1},
            {"Determination": 1},
            {"Disappointment": 1},
            {"Disapproval": 1},
            {"Disgust": 1},
            {"Distress": 1},
            {"Doubt": 1},
            {"Ecstasy": 1},
            {"Embarrassment": 1},
            {"Empathic Pain": 1},
            {"Enthusiasm": 1},
            {"Entrancement": 1},
            {"Envy": 1},
            {"Excitement": 1},
            {"Fear": 1},
            {"Gratitude": 1},
            {"Guilt": 1},
            {"Horror": 1},
            {"Interest": 1},
            {"Joy": 1},
            {"Love": 1},
            {"Nostalgia": 1},
            {"Pain": 1},
            {"Pride": 1},
            {"Realization": 1},
            {"Relief": 1},
            {"Romance": 1},
            {"Sadness": 1},
            {"Sarcasm": 1},
            {"Satisfaction": 1},
            {"Shame": 1},
            {"Surprise (negative)": 1},
            {"Surprise (positive)": 1},
            {"Sympathy": 1},
            {"Tiredness": 1},
            {"Triumph": 1}
        ],
        "Engagement": 
    }
    hume_expressions = [
        "Admiration",
        "Adoration",
        "Aesthetic Appreciation",
        "Amusement",
        "Anger",
        "Annoyance",
        "Anxiety",
        "Awe",
        "Awkwardness",
        "Boredom",
        "Calmness",
        "Concentration",
        "Confusion",
        "Contemplation",
        "Contempt",
        "Contentment",
        "Craving",
        "Desire",
        "Determination",
        "Disappointment",
        "Disapproval",
        "Disgust",
        "Distress",
        "Doubt",
        "Ecstasy",
        "Embarrassment",
        "Empathic Pain",
        "Enthusiasm",
        "Entrancement",
        "Envy",
        "Excitement",
        "Fear",
        "Gratitude",
        "Guilt",
        "Horror",
        "Interest",
        "Joy",
        "Love",
        "Nostalgia",
        "Pain",
        "Pride",
        "Realization",
        "Relief",
        "Romance",
        "Sadness",
        "Sarcasm",
        "Satisfaction",
        "Shame",
        "Surprise (negative)",
        "Surprise (positive)",
        "Sympathy",
        "Tiredness",
        "Triumph"
    ]
    hume_expressions = [
["Engagement", "Appreciation"]
        "Anger",
        "Annoyance",
        "Contempt",
        
       "Nervousness": [
           "Anxiety",
           "Distress",
           "Awkwardness"
       ]
        
        "Fear",
        "Horror",
        "Pain",

        "Confusion",
        "Doubt",
        "Boredom",
        "Calmness",
        "Tiredness",
        
        "happiness": [
            "Amusement",
            "Contentment",
            "Ecstasy",
            "Enthusiasm",
            "Excitement",
            "Joy",
            "Love",
            "Nostalgia",
            "Surprise (positive)",
            "Realization",
        ]

        

        
        "Positive-Engagement": [
            "Concentration",
            "Contemplation",
            "Entrancement",
            "Interest",
            "Determination",
            "Empathic Pain",
        ]
        
        "Negative-Engagement"[
            "Disappointment",
            "Disapproval",
            "Disgust",
            "Embarrassment",
            "Surprise (negative)",
        ]
    
        

        "Envy",

        "Romance",
        "Guilt",

        "Gratitude",
        
        
        "Pride",
        
        "Relief",
        "Sadness",
        "Sarcasm",
        "Satisfaction",
        "Shame",
        
        "Sympathy",
        "Triumph"
    ]

    # setup db
    df = pd.DataFrame(columns=cols)

    # append to db
    while input("Add another video [y/n]: ") == 'y':
        # get info
        vid_name = str(input("video name: "))
        pres_name = str(input("presenter name: "))

        # traits info
        trait_dict = 
        for trait in hume_expressions:
            trait_val = str(input(f"is {trait} present in {vid_name} [y/n]: ")) == 'y'

        

