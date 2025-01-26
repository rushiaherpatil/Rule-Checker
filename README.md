# Rule Checker Application

## Overview
The Rule Checker application is designed to analyze and correct sentences based on predefined grammatical and procedural rules. It identifies issues in sentences such as missing articles, passive voice, multiple instructions, non-imperative forms, and excessive word count.

Logs are saved centrally in a `logs` folder for better traceability, and sensitive configurations like API keys are managed using a `config.py` file in the `src/` directory.

---

## Directory Structure
```
├── logs/                  # Centralized logs folder
│   ├── application.log    # Logs from all modules
├── src/                   # Source files
│   ├── config.py          # Configuration file for sensitive data (e.g., API keys)
│   ├── logger_config.py   # Centralized logging configuration
│   ├── main.py            # Main application
│   ├── rule_checker.py    # RuleChecker logic
│   ├── groq_chain.py      # GroqChain logic
├── tests/                 # Test files
│   ├── test_rule_checker.py  # Unit tests for RuleChecker
```

---

## Installation

### Prerequisites
- Python 3.8 or later
- Pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Rule_Checker
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download the SpaCy model en_core_web_sm
   ```bash
   python -m spacy download en_core_web_sm
   ```
5. Set up the `logs` directory:
   ```bash
   mkdir logs
   ```

6. Configure your API key in `src/config.py`:
   ```python
   GROQ_API_KEY = "your_api_key_here"  # Replace with your actual API key
   ```

---

## Usage

### Running the Application
To run the main application, execute:
```bash
python src/main.py
```
Follow the prompts to input text for analysis.

### Running Tests
To execute the unit tests, run:
```bash
python tests/test_rule_checker.py
```

---

## Features
- **Rule-Based Sentence Analysis**:
  - Detects issues like missing articles, passive voice, multiple instructions, and more.
- **Sentence Correction**:
  - Uses the Groq language model to correct sentences while preserving intent.
- **Centralized Logging**:
  - Logs from all modules are saved in the `logs/application.log` file.
- **Configuration Management**:
  - API keys and sensitive data are stored in `src/config.py`.

---

## Logging
Logs from the application are saved in a centralized `logs/application.log` file. Each module writes logs to this file with relevant details, including timestamps and filenames.

---

## Configuration Management
Sensitive configurations, such as API keys, are stored in `src/config.py`. To avoid committing sensitive data to version control, ensure the file is added to `.gitignore`:
```bash
src/config.py
```

For additional security, consider using environment variables instead of hardcoding sensitive information.

---

## Limitations

1. **Model Dependency**:
   - The application relies on the Groq language model and SpaCy's `en_core_web_sm`. The overall accuracy of sentence correction depends on these models' performance and their ability to interpret text as intended. Any changes in the API or updates to the models may affect functionality.

2. **Language Support**:
   - Currently, the application only supports English sentences. Expanding to other languages would require additional NLP models and rules.

3. **Rule Generalization**:
   - The predefined rules may not cover all grammatical or procedural issues, leading to incomplete or incorrect corrections in certain cases.

4. **Performance**:
   - Processing long texts or running multiple analyses simultaneously may affect performance, depending on the system resources and the API response times.

5. **Error Handling**:
   - While exceptions are logged, unexpected errors (e.g., network issues) may still interrupt execution.

---

## Troubleshooting

1. **ModuleNotFoundError**:
   - Ensure the `src` directory is in the Python path when running tests. You can add it dynamically in test scripts:
     ```python
     import sys
     import os
     sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
     ```

2. **Logs Not Being Saved**:
   - Ensure the `logs` directory exists. If not, create it manually or programmatically as shown above.

3. **API Key Issues**:
   - Verify that the API key in `src/config.py` is correct and has access to the Groq API.

---

## Future Enhancements
- **Multi-language Support**:
  - Extend functionality to analyze and correct sentences in multiple languages.
- **Enhanced Rule Set**:
  - Add more rules for advanced grammatical constructs.
- **Web Interface**:
  - Develop a web-based UI for improved user interaction.
- **Large Language Models**:
  - Replace the small language model with a large language model (e.g., GPT-4 or similar) if a paid model API key is available for improved accuracy and broader functionality.

---

## License
[MIT License](LICENSE)

---

## Contact
For questions or issues, please contact me at rushiaherpatil@gmail.com.
