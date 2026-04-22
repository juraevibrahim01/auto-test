from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def test_humo(driver):
    element = wait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[class*="FluidContainer_fluid_container"]')))
    driver.execute_script("arguments[0].scrollIntoView();", element[1])
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView();", element[2])
    time.sleep(4)