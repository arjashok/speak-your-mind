from hume import HumeBatchClient
from hume.models.config import FaceConfig
from hume.models.config import ProsodyConfig

client = HumeBatchClient("9BAoszAhvQSgWLIttRJHlBJRHavk4NWOzfZQUTrDSATB5RFu")
file = ["examplevideo.mp4"]
configs = [FaceConfig(identify_faces=True)]
job = client.submit_job([],configs = configs, files=file)

job.await_complete()
job.download_predictions("predictions.json")