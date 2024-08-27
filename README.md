# J2Store Automation

### Overview
J2Store is a flexible shopping cart and ecommerce solution for Joomla. This project leverages Selenium WebDriver and Pytest to ensure the seamless UI functionality J2Store.


### Motivation
This project was created to automate the UI functionality of the J2Store interface, ensuring that all features work as expected. 
It also serves as a showcase of my skills in automating and testing web-based applications.

### Features
-  Cross-Browser Testing: Ensures compatibility with major browsers like Chrome, Firefox, and Edge.
-  Custom Logger Integration: Captures detailed logs for every test run.

### Tech Stack
- Programming Language: Python 3.12
- Frameworks: Selenium WebDriver, Pytest
- Reporting: Allure, HTML Reports
- CI/CD: Jenkins, GitHub Actions

### Architecture/Structure
The project follows a modular structure with Page Object Model (POM) to separate test scripts from web element locators, ensuring easy maintenance and scalability. 

The key components include:

-  Page Objects: Separate classes for each page of the J2Store admin panel.
-  Test Cases: Pytest scripts that execute the test scenarios.
-  Utilities: Custom logging and helper functions for enhanced test management.

### Installation
To set up the project locally:
-  Clone the repository:
    -  git clone https://github.com/AvinashCodeForge/J2Store.git
-  Navigate to the project directory:
    -  cd J2Store-Automation
-  Install the required dependencies
    -  pip install -r requirements.txt

### Usage
Run the test suite with the following command:
  -  pytest --html=reports/report.html --self-contained-html

For a specific test case:
  -  pytest -k "test_login"


