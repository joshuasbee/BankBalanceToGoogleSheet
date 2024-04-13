from playwright.sync_api import sync_playwright
import data
import threading

class BECU (threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)  # Set headless to False to see the browser
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
            checking_element = page.query_selector('table.dataTableXtended tbody tr.footer td:nth-child(3)')        
            # Extract the text content of the element
            if checking_element:
                checking = checking_element.inner_text()
                print(f'{checking=}')
            else:
                print("Checking not found")
                checking = -999 # Error getting value, write bank balance as -999

            # Close the browser
            browser.close()
            self.result = checking