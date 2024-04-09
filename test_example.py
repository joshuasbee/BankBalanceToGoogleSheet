import re
from playwright.sync_api import Page, expect

# def test_has_title(page: Page):
    # page.goto("https://playwright.dev/")

    # # Expect a title "to contain" a substring.
    # expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://onlinebanking.becu.org/BECUBankingWeb/Login.aspx?_gl=1*9ydu48*_ga*MjAzMDg4MTk4NC4xNzEyMTU5MDE3*_ga_0XYDH30BG5*MTcxMjY4OTE2NS43LjAuMTcxMjY4OTE2NS42MC4wLjA.&_ga=2.264657231.1976481819.1712689166-2030881984.1712159017")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    
    # TO run this:
    # pytest 
    # in terminal 
    
    # TO run with head (browser): pytest --headed
    
    # https://playwright.dev/python/docs/running-tests
    