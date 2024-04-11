import time
from playwright.sync_api import sync_playwright
import data
import threading

def handle_2fa(page):
    # Prompt the user to input the 2FA code
        code = input("Enter your 2FA code: ")

        # Fill in the 2FA code field
        page.fill('input[name="2fa-code"]', code)

        # Submit the 2FA code
        page.click('button[type="submit"]')

class CHASE(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)  # Set headless to False to see the browser
            page = browser.new_page()
    
            # Replace 'your_website_url' with the URL of the website you want to login to
            page.goto('https://secure.chase.com/web/auth/#/logon/logon/chaseOnline?treatment=chase&lang=en')

            # Replace 'username' and 'password' with your actual credentials
            username = data.CHASE_U
            password = data.CHASE_P

            # Replace 'username_selector' and 'password_selector' with the CSS selectors of the username and password fields
            username_selector = 'input[id="userId-text-input-field"]'
            password_selector = 'input[id="password-text-input-field"]'

            page.fill(username_selector, username)
            page.fill(password_selector, password)

            # Replace 'login_button_selector' with the CSS selector of the login button
            login_button_selector = 'button[id="signin-button"]'
            page.wait_for_timeout(1000)
            page.click(login_button_selector)
            page.wait_for_timeout(10 * 1000)
            print(f'Page title: {page.title}')
            # if page.title() == 'Two-Factor Authentication':
                # Handle 2FA
                # handle_2fa(page)

            page.wait_for_load_state()

            # Find the element containing the desired value
            checking_element = page.query_selector('div.primary-value.text-primary.flex-order-first[data-testid="dataItem-value"]')        
            # Extract the text content of the element
            if checking_element:
                checking = checking_element.inner_text()
                print(f'{checking=}')
            else:
                print("Checking not found")
                checking = -999

            time.sleep(10)
            # Close the browser
            browser.close()
            self.result = checking

# Call the function to execute the login
chase = CHASE()
chase.start()
chase.join()
print(f'{chase.result=}')