import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates
from util.conf import CONFLUENCE_SETTINGS


def badges_view_badges(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_badges_view_badges")
    def measure():

        @print_timing("selenium_badges_view_badges:view_profile_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/users/viewmyprofile.action")
            page.wait_until_visible((By.ID, "title-text"))
            page.wait_until_visible((By.ID, "my-badges-panel"))
            page.wait_until_visible((By.ID, "my-badges-panel-table-recent-badges"))
            page.wait_until_visible((By.ID, "my-badges-panel-table-badges"))
        sub_measure()
    measure()

def badges_view_ranking(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_badges_view_ranking")
    def measure():

        @print_timing("selenium_badges_view_ranking:view_ranking_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/badge/viewUserRanking.action")
            page.wait_until_visible((By.ID, "rank"))
            page.wait_until_visible((By.ID, "username"))
            page.wait_until_visible((By.ID, "goldBadges"))
            page.wait_until_visible((By.ID, "silverBadges"))
            page.wait_until_visible((By.ID, "bronzeBadges"))
            page.wait_until_visible((By.ID, "total"))
            page.wait_until_visible((By.ID, "points"))
        sub_measure()
    measure()
