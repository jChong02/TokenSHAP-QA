# extractors.py

def qa_extractor(prompt: str) -> tuple[str, str]:
    """
    Default extractor for structured QA prompts.
    Splits a prompt into a variable question segment and a fixed suffix.
    
    Args:
        prompt: Full prompt text (e.g., "Question: ... Answer Choices: ...")
    
    Returns:
        tuple[str, str]: (question_text, static_suffix)
    """
    if "Answer Choices:" in prompt:
        parts = prompt.split("Answer Choices:", 1)
        question_text = parts[0].replace("Question:", "").strip()
        static_suffix = "Answer Choices:" + parts[1]
    else:
        question_text = prompt.strip()
        static_suffix = ""
    return question_text, static_suffix
