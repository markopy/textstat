import pytest

@pytest.fixture
def short_text():
    return "Cool dogs wear da sunglasses."


@pytest.fixture
def easy_text():
    return (
            "Anna and her family love doing puzzles. Anna is best at "
            "little puzzles. Anna and her brother work on medium size "
            "puzzles together. Anna's Brother likes puzzles with cars "
            "in them. When the whole family does a puzzle, they do really "
            "big puzzles. It can take them a week to finish a really "
            "big puzzle. Last year they did a puzzle with 500 pieces! "
            "Anna tries to finish one small puzzle a day by her. "
            "Her puzzles have about 50 pieces. They all glue their "
            "favorite puzzles together and frame them. The puzzles look "
            "so nice on the wall."
        )

@pytest.fixture
def long_text():
    return (
        "Playing ... games has always been thought to be "
        "important to the development of well-balanced and "
        "creative children; however, what part, if any, "
        "they should play in the lives of adults has never "
        "been researched that deeply. I believe that "
        "playing games is every bit as important for adults "
        "as for children. Not only is taking time out to "
        "play games with our children and other adults "
        "valuable to building interpersonal relationships "
        "but is also a wonderful way to release built up "
        "tension.\n"
        "There's nothing my husband enjoys more after a "
        "hard day of work than to come home and play a game "
        "of Chess with someone. This enables him to unwind "
        "from the day's activities and to discuss the highs "
        "and lows of the day in a non-threatening, kick back "
        "environment. One of my most memorable wedding "
        "gifts, a Backgammon set, was received by a close "
        "friend. I asked him why in the world he had given "
        "us such a gift. He replied that he felt that an "
        "important aspect of marriage was for a couple to "
        "never quit playing games together. Over the years, "
        "as I have come to purchase and play, with other "
        "couples & coworkers, many games like: Monopoly, "
        "Chutes & Ladders, Mastermind, Dweebs, Geeks, & "
        "Weirdos, etc. I can reflect on the integral part "
        "they have played in our weekends and our "
        "\"shut-off the T.V. and do something more "
        "stimulating\" weeks. They have enriched my life and "
        "made it more interesting. Sadly, many adults "
        "forget that games even exist and have put them "
        "away in the cupboards, forgotten until the "
        "grandchildren come over.\n"
        "All too often, adults get so caught up in working "
        "to pay the bills and keeping up with the "
        "\"Joneses'\" that they neglect to harness the fun "
        "in life; the fun that can be the reward of "
        "enjoying a relaxing game with another person. It "
        "has been said that \"man is that he might have "
        "joy\" but all too often we skate through life "
        "without much of it. Playing games allows us to: "
        "relax, learn something new and stimulating, "
        "interact with people on a different more "
        "comfortable level, and to enjoy non-threatening "
        "competition. For these reasons, adults should "
        "place a higher priority on playing games in their "
        "lives"
    )