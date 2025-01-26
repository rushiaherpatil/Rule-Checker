from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableSequence, RunnableLambda

import sys
import os

# Add the root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from config import GROQ_API_KEY

# Configure logging
from logger_config import logger

class GroqChain:
    """
    A class to handle interaction with the Groq language model for sentence correction based on specified rules.
    """

    def __init__(self):
        """
        Initializes the GroqChain with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the Groq model.
        """
        try:
            logger.info("Initializing GroqChain with provided API key.")
            self.llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name='llama-3.3-70b-versatile')
            
            self.template = """
You are a Rule Checker that corrects sentences based on these rules:
1. Use articles/demonstratives properly before nouns (e.g., \"the,\" \"this,\" \"a\").
2. Rewrite sentences in active voice while preserving their original intent (declarative or imperative).
3. If a sentence contains multiple instructions, split them into separate steps and use proper formatting (e.g., A., B.).
4. Write procedural instructions in imperative form (e.g., \"Turn the switch.\").
5. Limit each sentence to 20 words or fewer without altering its meaning.

Below are examples of how to apply these rules:

### Example 1
Input Sentence: Tighten bolt assembly.
Issues: Missing article or demonstrative adjective.
Corrected Sentence: Tighten the bolt assembly.

### Example 2
Input Sentence: The fuel tank is inspected by the technician.
Issues: Not in active voice.
Corrected Sentence: The technician inspects the fuel tank.

### Example 3
Input Sentence: The wires are connected by the terminal block.
Issues: Not in active voice.
Corrected Sentence: The terminal block connects the wires.

### Example 4
Input Sentence: User manual describes how to configure system.
Issues: Missing article or demonstrative adjective.
Corrected Sentence: The user manual describes how to configure the system.

### Example 5
Input Sentence: Dust and debris should be removed using a vacuum cleaner.
Issues: Not in imperative form.
Corrected Sentence: Remove dust and debris using a vacuum cleaner.

### Example 6
Input Sentence: Align the control panel and tighten the screws.
Issues: Contains multiple instructions.
Corrected Sentence:
A. Align the control panel.
B. Tighten the screws.


Now, use the above examples as a guide to correct the following sentence based on the identified issues.

Input Sentence: {sentence}
Issues: {issues}

Corrected Sentence:
            """

            self.prompt = PromptTemplate(input_variables=["sentence", "issues"], template=self.template)
            
            # Wrap the prompt template with RunnableLambda
            prompt_runnable = RunnableLambda(lambda inputs: self.prompt.format(**inputs))

            # Combine the prompt and the LLM into a single sequence using the pipe operator
            self.chain = prompt_runnable | self.llm
            
            logger.info("GroqChain initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing GroqChain: {e}")
            raise

    def correct_sentence(self, sentence, issues):
        """
        Corrects a sentence based on the specified issues using the Groq language model.

        Args:
            sentence (str): The sentence to be corrected.
            issues (str): The identified issues with the sentence.

        Returns:
            str: The corrected sentence.
        """
        try:
            logger.info(f"Correcting sentence: '{sentence}' with issues: '{issues}'")
            # Use the chain to generate corrections for the sentence
            input_data = {"sentence": sentence, "issues": issues}

            # Generate corrections using the chain
            ai_message = self.chain.invoke(input_data)

            # Extract the content and strip whitespace
            corrected_sentence = ai_message.content.strip()
            
            # Post-process to remove unwanted artifacts
            corrected_sentence = corrected_sentence.replace("### Corrected Sentence:", "").strip()
            logger.info(f"Corrected sentence: '{corrected_sentence}'")
            return corrected_sentence
        except Exception as e:
            logger.error(f"Error correcting sentence: {e}")
            raise
