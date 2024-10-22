**DLai Application Automation Testing**

**1. Project Overview:** 
This repository contains the automation testing scripts for the DLai application. The automated tests are developed using Selenium WebDriver for browser interactions, and Pytest for test case management and execution. The tests validate the core features of the application, including login.

**2. Features Tested**
The following key features of the DLai application are tested:
**User Login:** Testing valid and invalid login scenarios.
**Field Validations:** Checking required fields for username and password.
**Error Messages:** Verifying error messages for invalid login attempts.


**3. Technology Stack**
**Python:** Language used for scripting.
**Selenium WebDriver:** For browser automation.
**Pytest:** Framework used for writing and running test cases.
**GitHub:** For version control and continuous integration.

**4. Setup and Installation**
Follow these steps to set up and run the automation tests on your local machine:

  **Clone the Repository:**
      git clone [https:://github.com/cclchd-rahil/dlai_automation_script.git]

  **Set up a Python Virtual Environment:**
      python -m venv venv
      source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

  **Install the Required Dependencies:**  
      pip install -r requirements.txt

  **Download and Set Up ChromeDriver:**
      Download ChromeDriver.
      Place the chromedriver in your project folder or set the path to ChromeDriver in the environment variables.

**5. Running all the Tests**
    1. Open the pycharm terminal.
    2. Type pytest 
    3. Click enter to run the test casees

  **Note:** To run the spefic Test Case just type pytest -k "function name" **EX:** pytest -k test_valid_login

**6. To generate an HTML test report:**
     Type pytest --html=report.html

**7. Contributing:** To contribute to this project:

  1. Fork the repository.
  2. Create a new feature branch: git checkout -b feature-branch
  3. Make your changes
  4. commit: git commit -m "Add new feature"
  5. Push the branch to your forked repository: git push origin feature-branch
  6. Create a pull request for review.


