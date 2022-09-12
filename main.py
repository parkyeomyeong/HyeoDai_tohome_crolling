from selenium import webdriver
import csv

from lib import scroll_down, croll_data_to_csv

category_ids = ["100571","100610","100615"]

def app():
    driver = webdriver.Chrome("C:\Dev\chromedriver_win32\chromedriver.exe")
    for id in category_ids:
        driver.get(f"https://tohome.thehyundai.com/front/dp/dpc/ctgrList.do?highCtgrId={id}")
        driver.implicitly_wait(3)
        
        scroll_down.infinite_loop(driver)
        number_of_li = len(driver.find_elements_by_css_selector("#ulItemList > li"))
        croll_data_to_csv.make_scv(driver, number_of_li)

    driver.close()

if __name__ == "__main__":
	app()