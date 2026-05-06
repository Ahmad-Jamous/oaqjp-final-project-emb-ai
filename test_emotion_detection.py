import unittest
from EmotionDetection.emotion_detection import emotion_detector

class EmotionDetectionUnittest(unittest.TestCase):
    def test_emotion_detector(self):
        for_joy = emotion_detector("I am glad this happened")['dominant_emotion']
        for_anger = emotion_detector("I am really mad about this")['dominant_emotion']
        for_disgust = emotion_detector("I feel disgusted just hearing about this")['dominant_emotion']
        for_sadness = emotion_detector("I am so sad about this")['dominant_emotion']
        for_fear = emotion_detector("I am really afraid that this will happen")['dominant_emotion']
        self.assertEqual(for_joy,'joy')
        self.assertEqual(for_anger,'anger')
        self.assertEqual(for_disgust,'disgust')
        self.assertEqual(for_sadness,'sadness')
        self.assertEqual(for_fear,'fear')
    
if __name__ == "__main__":
    unittest.main()