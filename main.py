from browser_activities import *
from prefect import flow, get_run_logger


@flow(name="login_ig", log_prints=True)
def main_fn():
    driver = start_browser()
    driver = input_data_at_login(in_driver=driver)
    driver = keep_browser_open(in_driver=driver)
    try:
        driver.quit()
    except AttributeError:
        get_run_logger().error("Browser already killed... Ending run")


if __name__ == "__main__":
    main_fn()
