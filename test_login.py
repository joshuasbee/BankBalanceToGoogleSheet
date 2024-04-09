from playwright.sync_api import sync_playwright
import data
from sheets import update_google_sheet

def login_with_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless to False to see the browser
        page = browser.new_page()
 
        # Replace 'your_website_url' with the URL of the website you want to login to
        page.goto('https://onlinebanking.becu.org/BECUBankingWeb/Login.aspx')

        # Replace 'username' and 'password' with your actual credentials
        username = data.BECU_USERNAME
        password = data.BECU_PASS

        # Replace 'username_selector' and 'password_selector' with the CSS selectors of the username and password fields
        username_selector = 'input[name="ctlSignon$txtUserID"]'
        password_selector = 'input[name="ctlSignon$txtPassword"]'

        page.fill(username_selector, username)
        page.fill(password_selector, password)

        # Replace 'login_button_selector' with the CSS selector of the login button
        login_button_selector = 'input[name="ctlSignon$btnLogin"]'
        page.click(login_button_selector)

        page.wait_for_selector('table.dataTableXtended')

        # Find the element containing the desired value
        value_element = page.query_selector('table.dataTableXtended tbody tr.footer td:nth-child(3)')

        # Extract the text content of the element
        if value_element:
            value = value_element.inner_text()
            print("Extracted value from the table:", value)
        else:
            print("Value not found")


        # Close the browser
        browser.close()
        return value

# Call the function to execute the login
balance = login_with_playwright()

# print(f'{balance[1:]}')
# balance = '$336.49'
update_google_sheet(balance, 'A1')