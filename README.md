Selenium Test Parser

This project is a Python script that uses Selenium WebDriver to automate the parsing of test questions and answers from a specific website. It is designed to extract data from an online test platform and store it in a JSON file for further analysis or usage.

Features:
- Automatically navigates to the test URL and switches the language to English (can be customized).
- Iterates through a series of questions and extracts the question text, image (if any), available answers, and the correct answer.
- Generates a unique question ID for each question.
- Stores the collected data in a JSON file.
- Supports parsing multiple tests in a single run.

Requirements:
- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (compatible with your Chrome browser version)
- JSON module

How to use:
1. Install Python and the required dependencies.
2. Download the Chrome WebDriver and make sure it is accessible to the script.
3. Customize the URL, language settings, and any other necessary configurations in the code.
4. Run the script and enter the number of tests you want to parse when prompted.
5. The script will automate the process, navigate through the tests, extract the data, and store it in a JSON file named 'data.json'.

Note: This script is specific to the target website structure and may require modifications if the website layout or elements change. It is recommended to consult the official Selenium documentation for more information on customization and adapting the code to different scenarios.

Feel free to contribute, modify, or enhance this script according to your needs. If you encounter any issues or have suggestions, please open an issue in the repository.

Happy parsing!
