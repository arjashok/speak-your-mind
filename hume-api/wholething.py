from hume import HumeBatchClient
from hume.models.config import FaceConfig
from hume.models.config import ProsodyConfig

client = HumeBatchClient("9BAoszAhvQSgWLIttRJHlBJRHavk4NWOzfZQUTrDSATB5RFu")
file = ["examplevideo.mp4"]
configs = [FaceConfig(fps_pred = 1, prob_threshold = 0.9, identify_faces=True,), ProsodyConfig()]
job = client.submit_job([],configs = configs, files=file)

job.await_complete()
job.download_predictions("predictions.json")