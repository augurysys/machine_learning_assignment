import logging
import typing
from queue import Queue, Empty
from threading import Thread, Event
from enum import Enum

from ml_assignment_proto.prediction_pb2 import Prediction

log = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class Gender(Enum):
    MALE = 0
    FEMALE = 1


class PredictionConsumer(Thread):
    def __init__(self,
                 predictions_queue: Queue,      # The queue to read predictions from
                 finished_processing: Event,    # Signal to stop running
                 num_predictions_to_expect: typing.Optional[int] = None
                 ):
        super(PredictionConsumer, self).__init__()
        self.predictions_queue = predictions_queue
        self.finished_processing = finished_processing
        self.num_predictions_to_expect = None
        self.num_predictions_processed = 0
        self.predicted_genders = {
            Gender.MALE: 0,
            Gender.FEMALE: 0
        }

    @property
    def num_consumed(self):
        return self.num_predictions_processed

    def run(self) -> None:
        while not self.finished_processing.is_set() or not self.predictions_queue.empty():
            try:
                prediction = self.predictions_queue.get(timeout=5.0)
            except Empty:
                continue
            log.info(f"[ Consumer ] Acquired prediction (name = {prediction.user.name})")
            gender = prediction.predicted_gender
            self.num_predictions_processed += 1
            if gender == Prediction.Gender.Value("MALE"):
                self.predicted_genders[Gender.MALE] += 1
            else:
                self.predicted_genders[Gender.FEMALE] += 1
            log.info(f"[ Consumer ] Processed {self.num_predictions_processed} so far, "
                     f"{self.predicted_genders[Gender.MALE]} males and {self.predicted_genders[Gender.FEMALE]} females")
            self.predictions_queue.task_done()
