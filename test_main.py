# TODO Have questions about the context of usage. Want to discuss at the interview


import unittest

from main import get_score, get_score_performance, game_stamps, DESIRED_OFFSET

FUNCTION = get_score  # get_score / get_score_performance

TEST_GAME_STAMP = [{'offset': 824, 'score': {'away': 0, 'home': 0}},
                   {'offset': 827, 'score': {'away': 0, 'home': 0}},
                   {'offset': 828, 'score': {'away': 0, 'home': 0}},
                   {'offset': 829, 'score': {'away': 0, 'home': 0}}, ]

TEST_RIGHT_OFFSET = 827
TEST_NON_EXISTENT_OFFSET = 826
NEGATIVE_OFFSET = -3


class TestGetScore(unittest.TestCase):
    def test_input_types(self):
        self.assertRaises(TypeError, FUNCTION, game_stamps, "STrING")
        self.assertRaises(TypeError, FUNCTION, "STrING", DESIRED_OFFSET)

    def test_valid_offset(self):
        with self.assertRaises(ValueError) as e:
            FUNCTION(game_stamps, NEGATIVE_OFFSET)
        self.assertEqual(f'offset must be positive: 0 > {NEGATIVE_OFFSET}', e.exception.args[0])

    def test_search_offset(self):
        self.assertEqual(FUNCTION(TEST_GAME_STAMP, TEST_RIGHT_OFFSET), (0, 0))
        self.assertRaises(ValueError, FUNCTION, TEST_GAME_STAMP, TEST_NON_EXISTENT_OFFSET)


if __name__ == '__main__':
    unittest.main()
