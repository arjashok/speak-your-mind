"""
    Generates feedback using the prompt engineering as specified by the metrics 
    we generate.
"""



"""
    Functionality for processing the HUME response.
"""

# ----------------- Environment Setup ----------------- #
import json
import openai
openai.key = "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"


# ----------------- Processing Functionality ----------------- #
"""
    Wraps the entire functionality for generating feedback from a key set of 
    metrics.
"""
def gen_llm_feedback(metrics: dict, prompt: str):
    # load prompt
    with open("prompt-template.txt", "r") as f:
        guidelines_prompt = f.read()
    
    # generate prompt
    prompt = guidelines_prompt.format(
        metrics_to_string(metrics),
        prompt
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )


"""
    Generates a string representation of the metrics.
"""
def metrics_to_string(metrics: dict) -> str:
    final_output = ""

    for metric, value in metrics.items():
        final_output += f"a final score of {value} for {metric}, "
    
    return final_output
