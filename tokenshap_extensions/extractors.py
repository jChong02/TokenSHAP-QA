# extractors.py

def qa_extractor(prompt: str) -> tuple[str, str]:
    """
    Extracts the question and static suffix from a structured QA prompt.
    
    Handles common cases such as:
        "Question: <text> Answer Choices: <options>"
        or just "Question: <text>"
        or even raw text without labels.
    
    Args:
        prompt: The full input text from a QA-style dataset.
    
    Returns:
        tuple[str, str]: (question_text, static_suffix)
            - question_text: the main, variable question portion
            - static_suffix: any fixed section (e.g., "Answer Choices: ...")
    """
    prompt = prompt.strip()
    question_text, static_suffix = prompt, ""

    # Split off suffix if present
    if "Answer Choices:" in prompt:
        parts = prompt.split("Answer Choices:", 1)
        question_text, static_suffix = parts[0], "Answer Choices:" + parts[1]

    # Remove leading label only if it exists
    if question_text.strip().startswith("Question:"):
        question_text = question_text.replace("Question:", "", 1).strip()

    return question_text.strip(), static_suffix.strip()
