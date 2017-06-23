import unittest


class FixturesBasedTestCase(unittest.TestCase):

    def setUp(self):
        with open('fixtures/unicast_prefixes_message', 'r') as unicast_prefix_message_file:
            self.unicast_prefix_message = unicast_prefix_message_file.read()
