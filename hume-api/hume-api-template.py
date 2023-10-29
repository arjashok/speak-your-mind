import requests

url = "https://api.hume.ai/v0/batch/jobs"

files = { "file": ("How%20Wind%20Energy%20Could%20Power%20Earth%20...%2018%20Times%20Over%20_%20Dan%20J%C3%B8rgensen%20_%20TED%20Countdown.mp4", open("How%20Wind%20Energy%20Could%20Power%20Earth%20...%2018%20Times%20Over%20_%20Dan%20J%C3%B8rgensen%20_%20TED%20Countdown.mp4", "rb"), "video/mp4") }
payload = { "json": "{\"models\":{\"face\":{\"fps_pred\":1,\"prob_threshold\":0.9,\"identify_faces\":false,\"min_face_size\":60,\"facs\":{},\"descriptions\":{},\"save_faces\":false},\"burst\":{},\"prosody\":{\"granularity\":\"utterance\",\"window\":{\"length\":4,\"step\":1}},\"language\":{\"granularity\":\"word\"}},\"transcription\":{\"language\":null,\"identify_speakers\":false,\"confidence_threshold\":0.5},\"notify\":false}" }
headers = {"accept": "application/json"}

response = requests.post(url, data=payload, files=files, headers=headers)

print(response.text)


{"models":{"face":{"fps_pred":1,"prob_threshold":0.9,"identify_faces":false,"min_face_size":60,"facs":{},"descriptions":{},"save_faces":false},"burst":{},"prosody":{"granularity":"utterance","window":{"length":4,"step":1}},"language":{"granularity":"word"}},"transcription":{"language":null,"identify_speakers":false,"confidence_threshold":0.5},"notify":false}