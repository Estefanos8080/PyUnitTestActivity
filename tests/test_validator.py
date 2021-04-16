import unittest

from classes.validator import Validator


class TestValidator(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_it_will_reject_username_if_too_long(self):
        # Assume
        username = 'InvalidTooLong'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)

    def test_it_will_reject_username_if_white_space_present(self):
        # Assume
        username = 'Rev al'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)

    def test_it_will_reject_username_if_there_is_no_uppercase_characters(self):
        # Assume
        username = 'reval'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)

    def test_it_will_accept_a_valid_username(self):
        # Assume
        username = 'Reval'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertTrue(result)
