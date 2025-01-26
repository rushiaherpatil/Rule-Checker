import logging
from rule_checker import RuleChecker
from groq_chain import GroqChain
import sys
import os

# Add the root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now import the config module
from config import GROQ_API_KEY

from logger_config import logger

def main():
    """
    Main function to run the Rule Checker application.

    This function initializes the RuleChecker and GroqChain classes, takes user input for text analysis,
    identifies issues in the input text, and provides corrected sentences based on predefined rules.
    """
    try:
        logger.info("Starting the Rule Checker application.")
        # Initialize the RuleChecker and GroqChain
        checker = RuleChecker()
        groq = GroqChain()

        # Prompt user for input text
        print("Welcome to Rule Checker!")
        text = input("Enter text to analyze: ")

        # Step 1: Check rules on the provided text
        results = checker.check_rules(text)
        
        # Step 2: Display issues and corrections for each sentence
        for result in results:
            sentence = result["sentence"]
            issues = ", ".join(result["issues"])
            print(f"\nOriginal Sentence: {sentence}")
            print(f"Issues: {issues if issues else 'None'}")

            if issues:
                # Correct the flagged sentence using GroqChain
                corrected_sentence = groq.correct_sentence(sentence=sentence, issues=issues)
                print(f"Corrected Sentence: {corrected_sentence}")
            else:
                print("No correction needed.")

    except Exception as e:
        logger.error(f"An error occurred in the application: {e}")
        raise

if __name__ == "__main__":
    main()
