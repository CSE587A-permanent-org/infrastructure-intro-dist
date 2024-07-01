from gradescope_utils.autograder_utils.decorators import weight
from infrastructure_intro.assignment import hello_world
import unittest


class TestHelloWorld(unittest.TestCase):
    @weight(5)
    def test_hello_world(self):
        """Test the hello world function"""
        self.assertEqual(hello_world(), "hello world")
