# test_predict.py

import unittest
from predict import predict_rainfall

class TestRainfallPrediction(unittest.TestCase):
    def test_rain_likely(self):
        self.assertEqual(predict_rainfall(18, 80), "Rain Likely")

    def test_no_rain(self):
        self.assertEqual(predict_rainfall(25, 60), "No Rain")

if __name__ == '__main__':
    unittest.main()
