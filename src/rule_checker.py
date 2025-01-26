import spacy


from logger_config import logger


class RuleChecker:
    """
    A class to check sentences against predefined grammatical and procedural rules.
    """

    def __init__(self):
        """
        Initializes the RuleChecker with the SpaCy language model.
        """
        try:
            logger.info("Loading SpaCy language model.")
            self.nlp = spacy.load("en_core_web_sm")
            logger.info("SpaCy language model loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading SpaCy language model: {e}")
            raise

    def check_rules(self, text):
        """
        Analyzes the input text and identifies issues in each sentence based on predefined rules.

        Args:
            text (str): The input text to analyze.

        Returns:
            list[dict]: A list of dictionaries, each containing a sentence and its identified issues.
        """
        try:
            logger.info("Analyzing text for rule violations.")
            doc = self.nlp(text)
            results = []
            for sent in doc.sents:
                issues = self.check_sentence_rules(sent)
                results.append({"sentence": sent.text.strip(), "issues": issues})
            return results
        except Exception as e:
            logger.error(f"Error analyzing text: {e}")
            raise

    def check_sentence_rules(self, sent):
        """
        Checks a single sentence against predefined rules.

        Args:
            sent (spacy.tokens.span.Span): The sentence to analyze.

        Returns:
            list[str]: A list of identified issues in the sentence.
        """
        issues = []
        try:
            if not self.has_article_or_demonstrative(sent):
                issues.append("Missing article or demonstrative adjective.")
            if not self.is_active_voice(sent):
                issues.append("Not in active voice.")
            if self.has_multiple_instructions(sent):
                issues.append("Contains multiple instructions.")
            if not self.is_imperative(sent) and not self.should_remain_declarative(sent):
                issues.append("Not in imperative form.")
            if len(sent.text.split()) > 20:
                issues.append("Sentence exceeds 20-word limit.")
        except Exception as e:
            logger.error(f"Error checking sentence rules for '{sent.text}': {e}")
            raise
        return issues

    def has_article_or_demonstrative(self, sent):
        """
        Checks if the sentence contains an article or demonstrative adjective.

        Args:
            sent (spacy.tokens.span.Span): The sentence to analyze.

        Returns:
            bool: True if an article or demonstrative adjective is present, False otherwise.
        """
        return any(token.tag_ == "DT" for token in sent)

    def is_active_voice(self, sent):
        """
        Checks if the sentence is written in active voice.

        Args:
            sent (spacy.tokens.span.Span): The sentence to analyze.

        Returns:
            bool: True if the sentence is in active voice, False otherwise.
        """
        return not any(token.dep_ == "nsubjpass" for token in sent)

    def has_multiple_instructions(self, sent):
        """
        Checks if the sentence contains multiple instructions.

        Args:
            sent (spacy.tokens.span.Span): The sentence to analyze.

        Returns:
            bool: True if the sentence contains multiple instructions, False otherwise.
        """
        verbs = [token for token in sent if token.pos_ == "VERB"]
        return len(verbs) > 1

    def is_imperative(self, sent):
        """
        Checks if the sentence is written in imperative form.

        Args:
            sent (spacy.tokens.span.Span): The sentence to analyze.

        Returns:
            bool: True if the sentence is in imperative form, False otherwise.
        """
        return sent[0].tag_ == "VB"

    def should_remain_declarative(self, sent):
        """
        Checks if the sentence should remain declarative.

        Args:
            sent (spacy.tokens.span.Span): The sentence to analyze.

        Returns:
            bool: True if the sentence should remain declarative, False otherwise.
        """
        return any(token.text.lower() in {"is", "are"} for token in sent)
