import unittest
from app import get_message

class TestStringMethod(unittest.TestCase):

    def test_message_for_low_temp(self):
        self.assertEqual(get_message(45), "Feel free to stay inside today. You have everyone's permission.")

    def test_message_for_mid_temp(self):
        self.assertEqual(get_message(60), "You're one of the lucky ones. Never forget that.")

    def test_message_for_high_temp(self):
        self.assertEqual(get_message(95), "Make posicle ice cream for all of your friends. You'll be the talk of the town.")

if __name__ == '__main__':
    unittest.main()
