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
        print("Login successful ..............")
        page.wait_for_timeout(2000)

        # 1. Navigate to Admin Module
        user_mgmt = UserManagementPage(page)
        user_mgmt.navigate_to_admin()
        print(" Navigated to Admin Module................")
        page.wait_for_timeout(2000)

        # 2. Add New User
        user_role = "1"  # 1 = Admin
        employee_name = "Shekar  Babu"
        username = "testuserR12784635115862"  #  Use this consistently
        status = "1"  # 1 = Enabled
        password = "Password@1289"
        user_mgmt.add_new_user(user_role, employee_name, username, status, password)
        print(" New user added successfully .............")

        # 3. Search User (now includes wait before clicking Search button)
        user_mgmt.search_user_and_print_result(username)

        # 4. Edit User Details
        edit_result = user_mgmt.edit_user_details(
            username=username,                          # Use the same username
            new_user_role="ESS",                        # Update to ESS
            new_employee_name="Linda  Anderson",        # New name
            new_status="Enabled",
            new_password="NewPass@1234"
        )

        if edit_result:
            print("User edit test case passed.")
        else:
            print("User edit test case failed.")

        # 5. Validate Updated Details
        is_valid = user_mgmt.validate_updated_user_details(
            username=username,
            expected_role="ESS",                         # Changed to match new role
            expected_employee_name="Linda  Anderson",    # Match what we updated
            expected_status="Enabled"
        )

        if is_valid:
            print("Test passed: Updated details are correct.")
        else:
            print("Test failed: Updated details do not match.")

        # 6. Delete the User
        was_deleted = user_mgmt.delete_user(username)

        if was_deleted:
            print(" Test passed: User was deleted.")
        else:
            print(" Test failed: User was not deleted.")

if __name__ == "__main__":
    run_all()
