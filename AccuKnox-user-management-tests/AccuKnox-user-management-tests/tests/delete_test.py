import sys
import os

# Add the parent directory to sys.path so Python can find the 'pages' package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright
from pages.Login_Page import LoginPage
from pages.User_Management_Page_1 import UserManagementPage

def run_all():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        login.navigate()
        login.login("Admin", "admin123")
        print("Login successful..........")

        user_mgmt = UserManagementPage(page)
        user_mgmt.navigate_to_admin()
        print(" Navigated to Admin Module .............")

        # Add New User
        user_role = "1"  # 1 = Admin
        employee_name = "Laxmi  Reddy"
        username = "testuserR127846351154858622"  #  Use this consistently
        status = "1"  # 1 = Enabled
        password = "Password@1289"
        user_mgmt.add_new_user(user_role, employee_name, username, status, password)
        print(" New user added successfully .............")

        # Search and capture user
        user_mgmt.search_user_and_print_result(username)

        #  Delete User (keep inside the function)
        was_deleted = user_mgmt.delete_user(username)

        if was_deleted:
            print(" Test passed: User was deleted.")
        else:
            print(" Test failed: User was not deleted.")

if __name__ == "__main__":
    run_all()
