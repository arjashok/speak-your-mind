import requests

url = "https://api.hume.ai/v0/batch/jobs"

payload = "{\"models\":{\"face\":{\"fps_pred\":1,\"prob_threshold\":0.9,\"identify_faces\":false,\"min_face_size\":60,\"facs\":{},\"descriptions\":{},\"save_faces\":false},\"burst\":{},\"prosody\":{\"granularity\":\"utterance\",\"window\":{\"length\":4,\"step\":1}},\"language\":{\"granularity\":\"word\"}},\"transcription\":{\"language\":null,\"identify_speakers\":false,\"confidence_threshold\":0.5},\"urls\":[\"https://www.youtube.com/watch?v=adJnm7Yopdo&t=92s\"],\"notify\":false}"
headers = {
    "accept": "application/json; charset=utf-8",
    "content-type": "application/json; charset=utf-8",
    "X-Hume-Api-Key": "9BAoszAhvQSgWLIttRJHlBJRHavk4NWOzfZQUTrDSATB5RFu"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)
