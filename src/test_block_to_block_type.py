import unittest
from block_to_block_type import is_ordered_list

class TestIsOrderedList(unittest.TestCase):
    def test_valid_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertTrue(is_ordered_list(block))

    def test_valid_ordered_list_single_item(self):
        block = "1. Only item"
        self.assertTrue(is_ordered_list(block))

    def test_invalid_starting_number(self):
        block = "2. First item\n3. Second item"
        self.assertFalse(is_ordered_list(block))

    def test_invalid_non_sequential(self):
        block = "1. First item\n3. Third item"
        self.assertFalse(is_ordered_list(block))

    def test_invalid_no_period(self):
        block = "1 First item\n2 Second item"
        self.assertFalse(is_ordered_list(block))

    def test_invalid_no_space_after_period(self):
        block = "1.First item\n2.Second item"
        self.assertFalse(is_ordered_list(block))

    def test_empty_block(self):
        block = ""
        self.assertFalse(is_ordered_list(block))

    def test_only_whitespace(self):
        block = "   \n  \n   "
        self.assertFalse(is_ordered_list(block))

    def test_with_empty_lines_between(self):
        block = "1. First item\n\n2. Second item"
        self.assertFalse(is_ordered_list(block))

    def test_unordered_list_format(self):
        block = "- First item\n- Second item"
        self.assertFalse(is_ordered_list(block))


if __name__ == "__main__":
    unittest.main()