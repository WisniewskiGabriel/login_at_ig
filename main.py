from browser_activities import *

if __name__ == "__main__":
    driver = start_browser()
    driver = input_data_at_login(in_driver=driver)
    driver = keep_browser_open(in_driver=driver)
