import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.avito.ru/avito-care/eco-impact"
OUTPUT_DIR = "D:\avito_test\output"

def take_screenshot(page, selector, screenshot_name):
    element = page.query_selector(selector)
    element.screenshot(path=f"{OUTPUT_DIR}{screenshot_name}")

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    page.goto(BASE_URL)
    yield page
    page.close()

def test_water_saved_counter(page):
    take_screenshot(page, ".water-counter", "water_saved_counter.png")

def test_co2_emissions_prevented_counter(page):
    take_screenshot(page, ".co2-counter", "co2_emissions_prevented_counter.png")

def test_energy_saved_counter(page):
    take_screenshot(page, ".energy-counter", "energy_saved_counter.png")