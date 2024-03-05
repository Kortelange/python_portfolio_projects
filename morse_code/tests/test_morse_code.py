import unittest
from main import text_to_morse


class TestMorseCodeTranslation(unittest.TestCase):
    def test_sos_translation(self):
        self.assertEqual(text_to_morse("sos"), "... --- ...")

    def test_hello_world_translation(self):
        hello_world = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        self.assertEqual(text_to_morse("hello world"), hello_world)
        self.assertEqual(text_to_morse("Hello world!"), hello_world + " -.-.--")


if __name__ == '__main__':
    unittest.main()
