import time
from prefect import task, get_run_logger
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from utils import get_credentials


@task(name="start_browser")
def start_browser():
    ChromeDriverManager().install()
    driver = webdriver.Chrome()
    driver.get("https://instagram.com")
    return driver


@task(name="input_data_at_login")
def input_data_at_login(in_driver):
    user_id, user_password = get_credentials("gabrunberg-at-ig")

    # TypeInto - User field
    str_xpath_user_field = "//input[@name='username']"
    try:
        WebDriverWait(driver=in_driver, timeout=30).until(ec.presence_of_element_located((By.XPATH, str_xpath_user_field)))
    except TimeoutException:
        get_run_logger().warning("Falha ao abrir Instagram")
    input_user = in_driver.find_element(By.XPATH, str_xpath_user_field)
    input_user.send_keys(user_id)

    # TypeInto - User password
    str_xpath_password_field = "//input[@name='password']"
    input_password = in_driver.find_element(By.XPATH, str_xpath_password_field)
    input_password.send_keys(user_password)

    # Click - Submit button
    str_xpath_submit_btn = "//button[@type='submit' and .//div[contains(text(),'Entrar')]]"
    submit_btn = in_driver.find_element(By.XPATH, str_xpath_submit_btn)
    submit_btn.click()

    return in_driver


@task(name="keep_browser_running")
def keep_browser_open(in_driver):

    wait_time = 10

    while True:
        try:
            body_text = in_driver.find_element(By.TAG_NAME, 'body').text
            time.sleep(60)
            print("Still running.")
        except:
            get_run_logger().warning("Instance of browser is probably closed at this point, ending run...")
            break
        wait_time += 5
        if wait_time > 10000:
            break