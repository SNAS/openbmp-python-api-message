from FixturesBasedTestCase import FixturesBasedTestCase

from openbmp.api.parsed.message import Message, UnicastPrefix


class UnicastPrefixTest(FixturesBasedTestCase):

    def test_default_parsing(self):
        """
        Test default UnicastPrefix parsing
        """
        message = Message(self.unicast_prefix_message)
        unicast_prefixes = UnicastPrefix(message)
        row_map = unicast_prefixes.get_row_map()

        self.assertEqual(2, len(row_map))

        self.assertEqual("12.12.12.0", row_map[0]['prefix'])
        self.assertEqual(20, row_map[0]['prefix_len'])

        self.assertEqual("12.12.123.0", row_map[1]['prefix'])
        self.assertEqual(22, row_map[1]['prefix_len'])

    def test_parsing_without_validation(self):
        """
        If disable validation, it should still produce the same output but
        numerical fields should be serializes as String
        """
        message = Message(self.unicast_prefix_message)
        unicast_prefixes = UnicastPrefix(message, validate=False)
        row_map = unicast_prefixes.get_row_map()

        self.assertEqual("20", row_map[0]['prefix_len'])

    def test_parsing_with_required_fields(self):
        """
        Test how UnicastPrefix works with custom required_fields parameter
        """
        message = Message(self.unicast_prefix_message)

        # Without validation
        unicast_prefixes = UnicastPrefix(message, validate=False, required_fields={11: "my_custom_prefix_name"})
        row_map = unicast_prefixes.get_row_map()

        self.assertEqual('20', row_map[0]['my_custom_prefix_name'])

        # With validation
        unicast_prefixes = UnicastPrefix(message, validate=True, required_fields={11: "my_custom_prefix_name"})
        row_map = unicast_prefixes.get_row_map()

        self.assertEqual(20, row_map[0]['my_custom_prefix_name'])
