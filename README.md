# Automated Testing Project using POM Framework

This project is an automated testing suite using the Page Object Model (POM) framework for testing a web application.

## Prerequisites

- Python 3.12.0
- Selenium
- Pytest
- Requests
- BeautifulSoup

You can install the required packages using:
pip install selenium pytest requests beautifulsoup4


## Running the Tests

1. **Activate the virtual environment if you have one:**

   ```bash
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


Run the tests using pytest:
pytest

## Configurations

- **config.py**: Contains the base URL and other configurations.
- **conftest.py**: Includes the pytest fixture for setting up and tearing down the WebDriver instance.

## Logging

Logs are written to `mylog.log` to provide detailed information about the test execution.

## Example Test Case

The test case `test_1.py` demonstrates:

1. Navigating to the home page.
2. Performing a search.
3. Filtering search results by brand and price.

## Adding New Tests

To add new tests:

1. Create a new file in the `Tests` directory.
2. Import the necessary Page Objects and write your test cases using the pytest framework.

## Authors

- Lusine
- Shushan
- Raya