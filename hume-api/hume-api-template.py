import requests

url = "https://api.hume.ai/v0/batch/jobs"
vidUrl = ""
files = { "file": (vidUrl, open(vidUrl, "rb"), "video/mp4") }
payload = { "json": "{\"models\":{\"face\":{\"fps_pred\":1,\"prob_threshold\":0.9,\"identify_faces\":false,\"min_face_size\":60,\"facs\":{},\"descriptions\":{},\"save_faces\":false},\"burst\":{},\"prosody\":{\"granularity\":\"utterance\",\"window\":{\"length\":4,\"step\":1}},\"language\":{\"granularity\":\"word\"}},\"transcription\":{\"language\":null,\"identify_speakers\":false,\"confidence_threshold\":0.5},\"notify\":false}" }
headers = {"accept": "application/json"}

response = requests.post(url, data=payload, files=files, headers=headers)

print(response.text)


{"models":{"face":{"fps_pred":1,"prob_threshold":0.9,"identify_faces":false,"min_face_size":60,"facs":{},"descriptions":{},"save_faces":false},"burst":{},"prosody":{"granularity":"utterance","window":{"length":4,"step":1}},"language":{"granularity":"word"}},"transcription":{"language":null,"identify_speakers":false,"confidence_threshold":0.5},"notify":false,"callback_url":"https://google.com"}