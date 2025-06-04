# AccuKnox-user-management-tests
### User Management E2E Flow (Manual + Automation)**
This project contains end-to-end test cases for automating the User Management functionality of the OrangeHRM demo application using **Playwright (Python)**.

##  Project Setup 
Automated test suite for validating the User Management module of OrangeHRM using **Playwright** with **Python**.  
The tests cover login, user creation, user editing, validation, and deletion.

**Tools used** - VS Code + Python

### 📁 Project Folder Structure
```
src/test/java
│
├── pages         # Page Object Model (POM) classes
│   ├── Login_Page.py               
│   └── User_Management_Page           
├── tests
│   ├── Test_Login                     
│   └──  delete_test 
├── myenv    # virtual environment
└── screenshots
```
### Create Virtual Environment
```
python -m venv myenv
```
### Activate the Virtual Environment
```
.\myenv\Scripts\activate
```
### Install Playwright and required dependencies
```
pip install playwright
```
```
playwright install
```
### The test uses the official OrangeHRM demo site: 
```
https://opensource-demo.orangehrmlive.com/
```

## How to run the test cases
#### Run All Tests (Login + Add + Edit + Validate)
```
python tests/Test_Login.py
```
#### Run Only the Delete Test
```
python tests/delete_test.py
```

## Playwright version used
Tested on Playwright version: 1.52.0

