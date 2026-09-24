def judge(question: str, expects: str, answer: str, results:str) -> bool:
    """
    Judge the answer of a question.

    :param question: The question to be judged.
    :param expects: The expected answer(s).
    :param answer: The actual answer provided.
    :param result: The result object to store the judgment outcome.
    """
    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()