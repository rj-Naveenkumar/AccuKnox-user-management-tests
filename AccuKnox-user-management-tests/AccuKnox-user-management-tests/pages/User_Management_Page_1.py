from playwright.sync_api import Page

class UserManagementPage:
    def __init__(self, page: Page):
        self.page = page
        #self.admin_tab = page.locator('a[href="/web/index.php/admin/viewAdminModule"]')
        self.admin_tab = page.locator('//a[@class="oxd-main-menu-item active"]')
        self.add_user_button = page.locator("xpath=//button[normalize-space()='Add']")

        # User Role Dropdown and Selection (e.g. ESS or Admin)
        self.user_role_dropdown = page.locator("//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][1]")
        self.ESS_option = page.locator("//div[@role='option']//span[text()='ESS']")
        self.admin_option = page.locator("//div[@role='option']//span[text()='Admin']")

        # Employee Name and Username
        self.employee_name_input = page.locator('input[placeholder="Type for hints..."]')
        self.username_input = page.locator('//div[@class="oxd-form-row"]//div[@class="oxd-grid-2 orangehrm-full-width-grid"]//div[@class="oxd-grid-item oxd-grid-item--gutters"]//div[@class="oxd-input-group oxd-input-field-bottom-space"]//div//input[@class="oxd-input oxd-input--active"]')

        # Status Dropdown and Selection
        self.status_dropdown = page.locator("//label[text()='Status']/following::div[contains(@class,'oxd-select-text')][1]")
        self.status_enabled_option = page.locator("//div[@role='option']//span[text()='Enabled']")
        self.status_disabled_option = page.locator("//div[@role='option']//span[text()='Disabled']")

        # Passwords
        self.password_input = page.locator('//div[@class="oxd-grid-item oxd-grid-item--gutters user-password-cell"]//div[@class="oxd-input-group oxd-input-field-bottom-space"]//div//input[@type="password"]')
        self.confirm_password_input = page.locator('div[class="oxd-grid-item oxd-grid-item--gutters"] div[class="oxd-input-group oxd-input-field-bottom-space"] div input[type="password"]')

        # Buttons
        self.save_button = page.locator('button:has-text("Save")')
        self.search_username_input = page.locator('//label[text()="Username"]/following::input[1]')
        self.search_button = page.locator('button:has-text("Search")')

        # User table and actions
        self.user_table_rows = page.locator('//div[@class="orangehrm-container"]')
        self.edit_button_selector = page.locator('button[title="Edit"]')
        self.delete_button_selector = page.locator('//button[contains(@class, "oxd-icon-button") and contains(@class, "oxd-table-cell-action-space")]//i[contains(@class, "bi-trash")]')
        self.confirm_delete_button = page.locator('//button[normalize-space()="Yes, Delete"]')

#1.Navigate to the Admin Module
    def navigate_to_admin(self):
        self.admin_tab.click()

#2.Add a New User
    def add_new_user(self, user_role, employee_name, username, status, password):
        self.add_user_button.click()

        # Select user role
        self.user_role_dropdown.click()
        if user_role.lower() == 'ess':
            self.ESS_option.click()
        else:
            self.admin_option.click()

        # Enter details
        self.employee_name_input.fill(employee_name)
        #self.username_input.fill(username)
        # Enter employee name and select from dropdown
        #self.employee_name_input.fill(employee_name)
        #self.page.locator(f"//div[@role='listbox']//span[text()='{employee_name}']").click()
# Type the employee name
        self.employee_name_input.fill(employee_name)

# Wait for suggestion list to appear
     #   self.page.wait_for_selector("//div[@role='listbox']//div[contains(text(), '" + employee_name + "')]")

# Press ArrowDown and Enter to select the first suggestion
      #  self.employee_name_input.press("ArrowDown")
      #  self.employee_name_input.press("Enter")



# Wait for suggestion list to appear
        self.page.wait_for_selector(f"//div[@role='listbox']//span[contains(text(), '{employee_name}')]")

# Click the first matching suggestion explicitly
        self.page.locator(f"//div[@role='listbox']//span[contains(text(), '{employee_name}')]").first.click()

        # Select status
        self.status_dropdown.click()
        if status.lower() == 'enabled':
            self.status_enabled_option.click()
        else:
            self.status_disabled_option.click()


# Fill username and passwords
            self.username_input.wait_for(state="visible")
            self.username_input.fill(username)
            self.password_input.fill(password)
            self.confirm_password_input.fill(password)

#  Save the new user
            self.save_button.click()
         #  Fill username and passwords
       # self.username_input.fill(username)
      #  self.password_input.fill(password)
      #  self.confirm_password_input.fill(password)

        # Fill passwords
      #  self.password_input.fill(password)
       # self.confirm_password_input.fill(password)

        # Save user
       # self.save_button.click() '''



# 3.Search User :
    def search_user_and_print_result(self, username):
        print(f"🔍 Searching for user: {username}")

        self.search_username_input.wait_for(state="visible", timeout=5000)
        self.search_username_input.fill(username)

        self.search_button.click()

    #  Fix this line: use self.page
        self.page.wait_for_timeout(3000)

        row_count = self.user_table_rows.count()

        if row_count == 0:
            print(" No user found with that username.")
        else:
            first_row = self.user_table_rows.nth(0)
            # Take a screenshot of the first row (the user found)
            first_row.screenshot(path=f"screenshots/user_{username}.png")
            row_text = first_row.inner_text()
            print(" User found:")
            print(f"Total rows found: {self.user_table_rows.count()}")

            print(" First row data -", row_text)

#4.Edit all the possible user details :
    def edit_user_details(self, username, new_user_role, new_employee_name, new_status, new_password):
        print(f" Searching for user to edit: {username}")

    # Search user
        self.search_username_input.fill(username)
        self.search_button.click()

        self.page.wait_for_timeout(3000)  # Wait for search results

        if self.user_table_rows.count() == 0:
            print(f" User '{username}' not found for editing.")
        return False

    # Click the edit button of the first matching row
        self.edit_button_selector.first.click()

        self.page.wait_for_timeout(2000)  # Wait for edit page/dialog to load

    # Edit User Role
        self.user_role_dropdown.click()
        if new_user_role.lower() == 'ess':
            self.ESS_option.click()
        else:
            self.admin_option.click()

    # Edit Employee Name
        self.employee_name_input.fill(new_employee_name)
        self.page.wait_for_selector(f"//div[@role='listbox']//span[contains(text(), '{new_employee_name}')]")
        self.page.locator(f"//div[@role='listbox']//span[contains(text(), '{new_employee_name}')]").first.click()

    # Edit Status
        self.status_dropdown.click()
        if new_status.lower() == 'enabled':
            self.status_enabled_option.click()
        else:
            self.status_disabled_option.click()

    # Edit Password & Confirm Password
        self.password_input.fill(new_password)
        self.confirm_password_input.fill(new_password)

    # Save changes
        self.save_button.click()
        first_row.screenshot(path=f"screenshots/EditChanges.png")

        print(f" User '{username}' details updated successfully.")
        return True


# 5.Validate Updated Details :
    def validate_updated_user_details(self, username, expected_role, expected_employee_name, expected_status):
    # Fill search input with username
        self.search_username_input.fill(username)
    
    # Click Search button
        self.search_button.click()
    
    # Wait for user rows to appear, assuming at least 1 row (excluding header)
        self.page.wait_for_timeout(2000)  # or better wait for some element specific to results
    
        row_count = self.user_table_rows.count()
    
        if row_count == 0:
            print(f"No user found with username: {username}") 
            return False
    
    # Assuming nth(1) is the first user row (not header)
            user_row = self.user_table_rows.nth(1)
    
    # Get text content of the row
            user_text = user_row.inner_text()
            print("User row found with details:")
            print(user_text)
    
    # Optional: Take screenshot
            user_row.screenshot(path=f"screenshots/updated_user_{username}.png")
    
    # Validate expected details (basic check with 'in')
            if (expected_role in user_text and expected_employee_name in user_text and expected_status in user_text):
                print(" Updated details validated successfully.")
                return True
            else:
                print(" Updated details validation failed.")
                return False

#6. delete User:
    def delete_user(self, username):
            print(f" Attempting to delete user: {username}")
    
    # Search for the user first
            self.search_username_input.fill(username)
            self.search_button.click()
            self.page.wait_for_timeout(2000)
    
            row_count = self.user_table_rows.count()
            print(f"🔍 Rows found before delete: {row_count}")
            if row_count == 0:
                print(" No user found to delete.")
                return False
    
    # Click the delete button for the first row
            self.delete_button_selector.first.click()
            self.page.wait_for_timeout(1000)
    
    # Confirm deletion
            self.confirm_delete_button.click()
            self.page.wait_for_timeout(2000)
    
    # Re-check if user still exists
            self.search_username_input.fill(username)
            self.search_button.click()
            self.page.wait_for_timeout(2000)
    
            post_delete_row_count = self.user_table_rows.count()
            
            if post_delete_row_count == 0:
                print(" User deleted successfully.")
                return True
            else:
                print(" User still present after deletion.")
                return False
