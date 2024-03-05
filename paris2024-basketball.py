import appdaemon.plugins.hass.hassapi as hass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HelloWorld(hass.Hass):

    def initialize(self):
        self.run_every(self.check_matches, "now", 60 * 15)

    def check_matches(self, kwargs):
        URL_TO_CHECK = "https://tickets.paris2024.org/en/event/basketball-arena-bercy-15782004/?affiliate=24R"
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

        driver = webdriver.Chrome(options=chrome_options)

        driver.get(URL_TO_CHECK)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tickets")))

        elements = driver.find_elements(By.CSS_SELECTOR, "#tickets .event-list .p-card")

        founded = False

        for element in elements:
            is_founded_non_availability = element.find_elements(By.CSS_SELECTOR, ".ticket-type-unavailable-sec")

            if not is_founded_non_availability:
                founded = True
                break

        if founded:
            self.call_service("notify/notify", message="BASKET PARIS2024 TICKETS AVAILABLE",
                              data={"url": URL_TO_CHECK,
                                    "push": {"sound": {"critical": 1, "name": "default", "volume": 0.8}}})
            print("Founded")
        else:
            print("Not founded")

        driver.quit()
