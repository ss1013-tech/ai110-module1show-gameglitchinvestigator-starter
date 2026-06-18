def get_range_for_difficulty(difficulty: str):
    """Resolve the valid guessing range for a selected difficulty.

    Args:
        difficulty: Difficulty label from the UI. Supported values are
            "Easy", "Normal", and "Hard".

    Returns:
        A 2-tuple ``(low, high)`` representing the inclusive bounds used for
        secret-number generation and guess validation.

    Notes:
        Unknown difficulty values fall back to the Normal range ``(1, 100)``
        to preserve a safe default behavior.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Parse raw user input into an integer guess.

    Args:
        raw: Raw text entered by the user.

    Returns:
        A tuple ``(ok, guess_int, error_message)`` where:
        - ``ok`` is ``True`` when parsing succeeds, otherwise ``False``.
        - ``guess_int`` is the parsed integer when ``ok`` is ``True``, else
          ``None``.
        - ``error_message`` is a user-facing validation message when parsing
          fails, else ``None``.

    Notes:
        Decimal-like strings (for example ``"49.9"``) are converted via
        ``float`` then ``int``, which truncates toward zero.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Compare a guess to the secret and produce game feedback.

    Args:
        guess: User guess value. Intended to be numeric after app-level input
            validation.
        secret: Secret target value for the active game.

    Returns:
        A tuple ``(outcome, message)`` where ``outcome`` is one of
        ``"Win"``, ``"Too High"``, or ``"Too Low"``, and ``message`` is the
        corresponding hint displayed in the UI.

    Notes:
        The function includes a string-based fallback path for mixed-type
        comparisons to avoid runtime errors if non-numeric inputs slip
        through unexpectedly.
    """
    # FIX: This comparator is intended for numeric inputs from app-level
    # validation and the corrected hint-direction logic.
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Compute the updated score after a guess outcome.

    Args:
        current_score: Score before applying the latest guess result.
        outcome: Result label from ``check_guess``.
        attempt_number: 1-based attempt index for the current game.

    Returns:
        Updated score as an integer.

    Notes:
        Winning guesses keep the existing score (capped at 100). Incorrect
        guesses apply a fixed 10-point penalty and clamp at zero. The
        ``attempt_number`` parameter is retained for API compatibility and
        future scoring variants.
    """
    if outcome == "Win":
        # FIX: Correct guesses keep score unchanged.
        return min(100, current_score)

    if outcome == "Too High":
        # FIX: Wrong guesses reduce score by 10 and never go below zero.
        return max(0, current_score - 10)

    if outcome == "Too Low":
        # FIX: Wrong guesses reduce score by 10 and never go below zero.
        return max(0, current_score - 10)

    return current_score
