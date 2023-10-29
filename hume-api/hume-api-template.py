import requests

url = "https://api.hume.ai/v0/batch/jobs"
vidUrl = "PASTE HERE"
files = { "file": (vidUrl, open(vidUrl, "rb"), "video/mp4") }
payload = { "json": "{\"models\":{\"face\":{\"fps_pred\":1,\"prob_threshold\":0.9,\"identify_faces\":false,\"min_face_size\":60,\"descriptions\":{},\"save_faces\":false},\"burst\":{},\"prosody\":{\"granularity\":\"utterance\",\"window\":{\"length\":4,\"step\":1}},\"language\":{\"granularity\":\"word\"}},\"transcription\":{\"language\":null,\"identify_speakers\":false,\"confidence_threshold\":0.5},\"notify\":false}" }
headers = {
    "accept": "application/json",
    "X-Hume-Api-Key": "9BAoszAhvQSgWLIttRJHlBJRHavk4NWOzfZQUTrDSATB5RFu"
}

response = requests.post(url, data=payload, files=files, headers=headers)

print(response.text)

{"models":{"face":{"fps_pred":1,"prob_threshold":0.9,"identify_faces":false,"min_face_size":60,"descriptions":{},"save_faces":false},"burst":{},"prosody":{"granularity":"utterance","window":{"length":4,"step":1}},"language":{"granularity":"word"}},"transcription":{"language":null,"identify_speakers":false,"confidence_threshold":0.5},"notify":false}


6cd600da-70b8-400f-a055-664579c7536e

ccc87a05-6480-4c4e-ba68-f3ab95e4c547