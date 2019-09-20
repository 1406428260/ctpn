import unittest,logging
from main.early_stop import EarlyStop
import tensorflow as tf
FLAGS = tf.app.flags.FLAGS

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()])

'''
    BEST = 0
    CONTINUE = 1
    LEARNING_RATE_DECAY = 2
    STOP = 3
'''
class TestEarlyStop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tf.app.flags.DEFINE_float('max_lr_decay', 3, '')
        tf.app.flags.DEFINE_integer('early_stop', 3, '')
        print("initializing tensorflow flags...")

    def setUp(self):
        self.es = EarlyStop(FLAGS.early_stop,FLAGS.max_lr_decay)
        print("Test initializing...")

    def test_zero(self):
        decision = self.es.decide(0)
        self.assertEqual(EarlyStop.ZERO,decision)

    def test_best_and_continue(self):
        decision = self.es.decide(0.12)
        self.assertEqual(EarlyStop.BEST,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.CONTINUE,decision)
        decision = self.es.decide(0.121)
        self.assertEqual(EarlyStop.BEST,decision)

    def test_lr_decay(self):
        decision = self.es.decide(0.12)
        self.assertEqual(EarlyStop.BEST,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.CONTINUE,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.CONTINUE,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.LEARNING_RATE_DECAY,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.CONTINUE,decision)

    def test_stop(self):
        decision = self.es.decide(0.12)
        self.assertEqual(EarlyStop.BEST,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.CONTINUE,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.CONTINUE,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.LEARNING_RATE_DECAY,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.CONTINUE,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.CONTINUE,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.LEARNING_RATE_DECAY,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.CONTINUE,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.CONTINUE,decision)
        decision = self.es.decide(0.11)
        self.assertEqual(EarlyStop.STOP,decision)


if __name__ == '__main__':
    unittest.main()
