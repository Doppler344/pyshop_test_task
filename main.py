from pprint import pprint
import random
import math
import time

DESIRED_OFFSET = 498

TIMESTAMPS_COUNT = 500  # 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3  # 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
                             PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

pprint(game_stamps)


# -----------------------------------TASK-----------------------------------

def bench(func):
    def wrapper(game_stamps, offset):
        start = time.time()
        func(game_stamps, offset)
        end = time.time()
        print('{}'.format(end - start))

    return wrapper


# @bench
def get_score(game_stamps, offset):  # O(n)
    """
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    """

    if type(offset) is not int:
        raise TypeError(f'offset must be integer, not {type(offset)}')
    if offset < 0:
        raise ValueError(f'offset must be positive: 0 > {offset}')
    if type(game_stamps) is not list:
        raise TypeError(f'game_stamps must be list of dict, not {type(game_stamps)}')

    for stamp in game_stamps:
        if offset in stamp.values():
            return stamp['score']['home'], stamp['score']['away']
    raise ValueError('offset value not included')


# score = get_score(game_stamps, DESIRED_OFFSET)
# print(score)


# @bench
def get_score_performance(game_stamps, offset):  # O(log(n)) // can use it because the list was created sorted
    """
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    """

    if type(offset) is not int:
        raise TypeError(f'offset must be integer, not {type(offset)}')
    if offset < 0:
        raise ValueError(f'offset must be positive: 0 > {offset}')
    if type(game_stamps) is not list:
        raise TypeError(f'game_stamps must be list of dict, not {type(game_stamps)}')

    low = 0
    high = len(game_stamps) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = game_stamps[mid]['offset']
        if guess == offset:
            return game_stamps[mid]['score']['home'], game_stamps[mid]['score']['away']
        elif guess > offset:
            high = mid - 1
        else:
            low = mid + 1

    raise ValueError('list doesnt contain score')

# score = get_score_performance(game_stamps, DESIRED_OFFSET)
# print(score)
