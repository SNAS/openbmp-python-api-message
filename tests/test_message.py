from FixturesBasedTestCase import FixturesBasedTestCase

from openbmp.api.parsed.message import Message


class MessageTest(FixturesBasedTestCase):

    def test_headers_parsing(self):
        """
        Test default Message headers parsing
        """
        message = Message(self.unicast_prefix_message)

        self.assertEqual(1.5, message.version)
        self.assertEqual("9ae8148974c9ca01ec9271753426d214", message.collector_hash_id)
        self.assertEqual(290976, message.length)
        self.assertEqual(2, message.records)

    def test_disabled_headers_parsing(self):
        """
        Test disabled Message headers parsing
        """
        message = Message(self.unicast_prefix_message, parse_headers=False)

        self.assertEqual(0.0, message.version)
        self.assertEqual("", message.collector_hash_id)
        self.assertEqual(0, message.length)
        self.assertEqual(0, message.records)
