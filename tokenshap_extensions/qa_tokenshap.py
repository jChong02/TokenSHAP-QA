# qa_tokenshap.py

from typing import Optional, Callable, List, Dict
from token_shap.base import ModelBase, TextVectorizer
from token_shap.token_shap import TokenSHAP
from .extractors import qa_extractor

class QATokenSHAP(TokenSHAP):
    """
    Extension of TokenSHAP for structured question-answering prompts.
    Only the question segment is perturbed during Monte Carlo sampling,
    while the answer segment remains fixed.
    """
    def __init__(
        self,
        model: ModelBase,
        splitter,
        vectorizer: Optional[TextVectorizer] = None,
        debug: bool = False,
        section_extractor: Optional[Callable[[str], tuple[str, str]]] = None,
    ):
        """
        Initialize QATokenSHAP
        
        Args:
            model: Model to analyze
            splitter: Text splitter implementation
            vectorizer: Text vectorizer for calculating similarities
            debug: Enable debug output
            section_extractor: Function that splits a prompt into
                (variable_question, static_suffix). Defaults to qa_extractor.
        """
        super().__init__(model=model, splitter=splitter, vectorizer=vectorizer, debug=debug)

        if section_extractor is not None and not callable(section_extractor):
            raise TypeError("section_extractor must be callable.")
        
        self.section_extractor = section_extractor or qa_extractor
        self.static_suffix = ""
    
    def _get_samples(self, content: str) -> List[str]:
        """Get question tokens from structured prompt"""
        question_text, self.static_suffix = self.section_extractor(content)
        return self.splitter.split(question_text)

    def _prepare_combination_args(self, combination: List[str], original_content: str) -> Dict:
        """Prepare model input by reattaching the fixed suffix"""
        prompt = self.splitter.join(combination)
        if self.static_suffix:
            prompt = f"{prompt}\n\n{self.static_suffix}"
        return {"prompt": prompt}
    