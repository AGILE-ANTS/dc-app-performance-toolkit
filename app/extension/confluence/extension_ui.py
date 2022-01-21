import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates
from util.conf import CONFLUENCE_SETTINGS


def rip_view_page_with_macro(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_rip_view_page_with_macro")
    def measure():

        @print_timing("selenium_rip_view_page_with_macro:view_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/display/RIP/RIP")
            page.wait_until_visible((By.ID, "title-text"))
            page.wait_until_visible((By.XPATH, "//table[contains(@id,'rip-table')]"))
        sub_measure()
    measure()
