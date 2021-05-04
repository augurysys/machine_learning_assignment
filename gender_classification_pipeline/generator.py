import base64
import logging
import random
import time
import typing
from queue import Queue
from threading import Thread

from gender_classification_pipeline.ml_assignment_proto.features_pb2 import Features

log = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class SampleGenerator(Thread):
    def __init__(self,
                 samples_queue: Queue,  # The queue to push the samples into
                 path_to_data: str,     # Where data files are stored locally
                 num_samples_to_generate: typing.Optional[int] = None
                 ):
        super(SampleGenerator, self).__init__()
        self.samples_queue = samples_queue
        self.path_to_data = path_to_data
        self.num_examples_to_generate = num_samples_to_generate
        self.num_examples_generated = 0
        self.examples = []
        try:
            with open(self.path_to_data, 'rb') as f_features:
                lines = f_features.readlines()
            for line in lines:
                features = Features().FromString(base64.b64decode(line))

                self.examples.append(features)
        except (IOError, Exception) as e:
            log.error(f"[ Generator ] Couldn't read data from {self.path_to_data} - aborting ({type(e)} - {e})")
            raise e

    def run(self) -> None:
        while self.num_examples_to_generate is not None and \
                self.num_examples_generated < self.num_examples_to_generate:
            example_index = random.randint(0, len(self.examples)-1)
            example = self.examples[example_index]
            self.samples_queue.put(example)
            self.num_examples_generated += 1
            log.info(f"[ Generator ] Successfully generated example (name: {example.user.name}), "
                     f"total generated so far: {self.num_examples_generated}")
            time.sleep(random.random()/20.0)
