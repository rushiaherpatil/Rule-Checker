import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from rule_checker import RuleChecker

class TestRuleChecker(unittest.TestCase):
    """
    Unit test class for the RuleChecker module.
    """

    def setUp(self):
        """
        Initializes a RuleChecker instance for testing.
        """
        self.checker = RuleChecker()

    def test_check_rules(self):
        """
        Tests the check_rules method for identifying issues in sentences.
        """
        text = "Turn shaft assembly. Set the TEST switch to the middle position and release the SHORT-CIRCUIT TEST switch."
        results = self.checker.check_rules(text)

        # Ensure the correct number of results are returned
        self.assertEqual(len(results), 2)

        # Verify issues in the first sentence
        self.assertIn("Missing article or demonstrative adjective.", results[0]["issues"])

        # Verify issues in the second sentence
        self.assertIn("Contains multiple instructions.", results[1]["issues"])

    def test_no_issues(self):
        """
        Tests the check_rules method for a sentence with no issues.
        """
        text = "Turn the shaft assembly."
        results = self.checker.check_rules(text)

        # Ensure only one sentence is analyzed
        self.assertEqual(len(results), 1)

        # Verify no issues are identified
        self.assertEqual(results[0]["issues"], [])

    def test_multiple_issues(self):
        """
        Tests the check_rules method for a sentence with multiple issues.
        """
        text = "The main gear leg is held by the side stay."
        results = self.checker.check_rules(text)

        # Ensure only one sentence is analyzed
        self.assertEqual(len(results), 1)

        # Verify all applicable issues are identified
        self.assertIn("Not in active voice.", results[0]["issues"])

if __name__ == "__main__":
    unittest.main()
