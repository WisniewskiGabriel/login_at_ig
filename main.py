from browser_activities import *


def main_fn():
    driver = start_browser()
    driver = input_data_at_login(in_driver=driver)
    driver = keep_browser_open(in_driver=driver)


if __name__ == "__main__":
    main_fn()
