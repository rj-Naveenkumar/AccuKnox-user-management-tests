# AccuKnox-user-management-tests
### User Management E2E Flow (Manual + Automation)**
This project contains end-to-end test cases for automating the User Management functionality of the OrangeHRM demo application using **Playwright (Python)**.
**---
##  Project Setup 
Automated test suite for validating the User Management module of OrangeHRM using **Playwright** with **Python**.  
The tests cover login, user creation, user editing, validation, and deletion.
---
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
│   ├── DataProviders.java    # to support Data-Driven Testing (DDT) in TestNG by supplying  external test data from an Excel file to test methods.
│   ├── ExtentReportManager.java   #To generate a professional Extent HTML report that tracks the status of each test case run during the automation execution.
│   └──  XLUtility.java      # To provide reusable methods for reading and writing Excel data so that test cases can be executed with dynamic input from an Excel file
```
