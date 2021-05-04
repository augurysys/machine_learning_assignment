import logging
import time
from queue import Queue
import os

from gender_classification_pipeline.consumer import PredictionConsumer
from gender_classification_pipeline.generator import SampleGenerator
from threading import Event

log = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class GenderClassificationPipeline(object):
    data_path = os.path.join(os.path.dirname(__file__), "data/features.dat")

    def __init__(self, predictor_class, num_samples_to_generate=100):
        self.num_samples_to_generate = num_samples_to_generate
        self.finished_processing = Event()

        self.samples_queue = Queue()
        self.predictions_queue = Queue()

        self.predictor = predictor_class(self.samples_queue, self.predictions_queue, self.finished_processing)
        self.generator = SampleGenerator(self.samples_queue, GenderClassificationPipeline.data_path,
                                         num_samples_to_generate=num_samples_to_generate)
        self.consumer = PredictionConsumer(self.predictions_queue, self.finished_processing)

    def run(self):
        log.info(f"[ Pipeline ] Starting execution - processing {self.num_samples_to_generate} examples.")
        self.generator.start()
        self.predictor.start()
        self.consumer.start()

        while self.consumer.num_consumed < self.num_samples_to_generate:
            time.sleep(1)

        self.finished_processing.set()

        self.generator.join()
        self.predictor.join()
        self.consumer.join()
        log.info(f"[ Pipeline ] Finished processing data")
