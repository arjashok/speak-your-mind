


import requests

    
def getJobPrediction(jobKey){
    url = "https://api.hume.ai/v0/batch/jobs/%s/predictions" % jobKey
    headers = {
        
        "accept": "application/json; charset=utf-8",
        "X-Hume-Api-Key": "9BAoszAhvQSgWLIttRJHlBJRHavk4NWOzfZQUTrDSATB5RFu"
    }

    response = requests.get(url, headers=headers)
}