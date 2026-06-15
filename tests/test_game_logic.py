from pathlib import Path
import sys
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# FIX: Added broader guess checks across multiple values to catch direction regressions.
@pytest.mark.parametrize(
    "guess, secret, expected_outcome",
    [
        (1, 50, "Too Low"),
        (49, 50, "Too Low"),
        (50, 50, "Win"),
        (51, 50, "Too High"),
        (100, 50, "Too High"),
    ],
)
def test_check_guess_multiple_values(guess, secret, expected_outcome):
    outcome, _ = check_guess(guess, secret)
    assert outcome == expected_outcome

# FIX: Added regression test to verify Easy mode range mapping.
def test_range_for_easy_mode():
    assert get_range_for_difficulty("Easy") == (1, 20)


# FIX: Added regression test to verify Normal mode range mapping.
def test_range_for_normal_mode():
    assert get_range_for_difficulty("Normal") == (1, 100)


# FIX: Added regression test to verify Hard mode range mapping.
def test_range_for_hard_mode():
    assert get_range_for_difficulty("Hard") == (1, 50)
