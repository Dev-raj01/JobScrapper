from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL
URL = "https://www.meesho.io/jobs"

# Set up Chrome options for headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (if needed)
chrome_options.add_argument("--window-size=1920x1080")  # Set a default window size

# Initialize the WebDriver with the options
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(URL)
    print(driver.title)

    # Wait for the button to be clickable
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[role='switch']"))
    )

    # Check if the button is already enabled
    if button.get_attribute("aria-checked") == "false":
        # Click the button to enable it
        button.click()
        print("Button enabled")
    else:
        print("Button was already enabled")

    # Wait for the job listings to load after enabling the button
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".grid.grid-cols-12.px-5"))
    )

    # Keep the window open for inspection
    time.sleep(30)
finally:
    driver.quit()
