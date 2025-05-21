from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector("I'm glad this happened.")
        result_2 = emotion_detector("I'm really angry about this")
        result_3 = emotion_detector("I feel disgusted just hearing about this.")
        result_4 = emotion_detector("I'm so sad about this")
        result_5 = emotion_detector("I'm very afraid that this will happen.")

        self.assertEqual(result_1["dominant_emotion"], "joy")
        self.assertEqual(result_2["dominant_emotion"], "anger")
        self.assertEqual(result_3["dominant_emotion"], "disgust")
        self.assertEqual(result_4["dominant_emotion"], "sadness")
        self.assertEqual(result_5["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()
