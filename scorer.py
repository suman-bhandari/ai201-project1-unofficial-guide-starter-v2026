import re

def normalize_text(text: str) -> str:
    """
    Normalizes text for robust string matching by:
    1. Converting to lowercase.
    2. Replacing punctuation with spaces (preserving alphanumeric characters and spaces).
    3. Collapsing multiple spaces into a single space.
    """
    if not text:
        return ""
    # Lowercase
    text = text.lower()
    # Replace non-alphanumeric characters with spaces
    text = re.sub(r"[^\w\s]", " ", text)
    # Collapse multiple whitespaces
    text = re.sub(r"\s+", " ", text).strip()
    return text

def judge(question: str, expects: str, answer: str, results:str) -> bool:
    """
    Evaluates whether the expected substring is contained within the generated answer.
    Uses normalized matching to prevent false negatives caused by punctuation or formatting.
    """
    normalized_expects = normalize_text(expects)
    normalized_answer = normalize_text(answer)
    
    if not normalized_expects:
        return True
        
    return normalized_expects in normalized_answer