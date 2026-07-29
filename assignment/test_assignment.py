from gradescope_utils.autograder_utils.decorators import weight
import unittest

from assignment.infrastructure_intro import hello_world


class TestHelloWorld(unittest.TestCase):
    @weight(5)
    def test_hello_world(self):
        """Test the hello world function"""
        self.assertEqual(hello_world(), "hello world")
