# AccuKnox-user-management-tests
### User Management E2E Flow (Manual + Automation)**
This project contains end-to-end test cases for automating the User Management functionality of the OrangeHRM demo application using **Playwright (Python)** using VS Code.

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

---

# Problem Statement 2:
### File name - System-App-Health Checker 
This project also includes implementations for the following objectives:

## 1. System Health Monitoring Script:
Developed a Python script that monitors the health of a Linux system by checking CPU usage, memory usage, disk space, and running processes. It logs alerts when any metric exceeds predefined thresholds.

## 4. Application Health Checker:
Developed a Python script that checks the uptime and status of an application by sending HTTP requests and validating the response status codes. The script logs whether the application is 'UP' or 'DOWN' based on the response.
