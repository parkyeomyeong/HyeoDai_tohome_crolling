from selenium import webdriver
from lib import random_num, random_date, save_image, scroll_down, croll_data_to_csv
from PIL import Image
import csv
import time
import re
category_ids = ["100571", "100610", "100615"]


def app():
    input_prod_id = 1
    error_count = 0
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(
        "C:\Dev\chromedriver_win32\chromedriver.exe", chrome_options=chrome_options)

    # 카테고리별 접근
    for id in category_ids:
        driver.get(
            f"https://tohome.thehyundai.com/front/dp/dpc/ctgrList.do?highCtgrId={id}")
        driver.implicitly_wait(1)

        head_name = driver.find_element_by_css_selector(
            'section.categorylist > div.depth > h2').text

        # 끝까지 스크롤 내리기
        scroll_down.infinite_loop(driver)
        prod_lis = [link.find_element_by_css_selector(
            "li > a").get_attribute('href') for link in driver.find_elements_by_css_selector("#ulItemList > li")]

        # 각 물품에 들어가 정보 스크롤
        for prod_li in prod_lis:
            try:
                # a의 href가 주소가아닌 js로 넘어가게 해놔서 정규표현식으로 params를 가지고와서 link를 만들어 접속
                t = re.findall(
                    r"'.*'", prod_li[prod_li.find("fnProductDetailMove"):])
                params = [string.strip("'") for string in t[0].split(',')]
                next_href = f"https://tohome.thehyundai.com/front/pd/pdd/productDetail.do?slitmCd={params[0]}&sectId={params[1]}&ctgrId={params[2]}"
                driver.get(next_href)

                # 안정화를 위해 잠시 타임
                time.sleep(0.5)
                # driver.get("https://tohome.thehyundai.com/front/pd/pdd/productDetail.do?slitmCd=S02006004353&sectId=101007&ctgrId=119970")
                # driver.implicitly_wait(3)

                # ---- data 긁어오는 부분 ----
                prod_id = input_prod_id
                shop_name = driver.find_element_by_css_selector(
                    "#brand_section > a").text
                prod_name = driver.find_element_by_css_selector(
                    ".proinfo > h2 > strong").text

                prod_price = ''
                try:
                    prod_price = driver.find_element_by_css_selector(
                        "#price_section > .txt-price > del").text
                except:
                    prod_price = driver.find_element_by_css_selector(
                        "#price_section > .txt-price > strong > em").text

                url = driver.find_element_by_css_selector(
                    "div.propicbig > div > img").get_attribute('src')

                category_id = id
                subscribe_yn = random_num.make_random_num(1)
                pack_type = driver.find_elements_by_css_selector(
                    ".detailinfo > dl > dd")
                if driver.find_element_by_css_selector(
                        ".detailinfo > dl > dt").text == '원산지':
                    pack_type = pack_type[1].text
                else:
                    pack_type = pack_type[0].text
                prod_stock = random_num.make_random_num2(3, 11)
                prod_info = prod_id
                admin_no = "0707"
                create_date = random_date.make_random_date(150)
                # ---- data 긁어오는 부분 ----

                # csv 저장
                croll_data_to_csv.save_csv(
                    prod_id,
                    shop_name,
                    prod_name,
                    prod_price,
                    url,
                    category_id,
                    subscribe_yn,
                    pack_type,
                    prod_stock,
                    prod_info,
                    admin_no,
                    create_date,
                    head_name
                )

                img_out_path = f"out/{category_id}/{prod_id}.png"

                # 제품설명 스크린샷
                width = driver.execute_script(
                    "return document.body.scrollWidth")  # 스크롤 할 수 있는 최대 넓이
                height = driver.execute_script(
                    "return document.body.scrollHeight")  # 스크롤 할 수 있는 최대 높이
                driver.set_window_size(width, height)  # 스크롤 할 수 있는 모든 부분을 지정
                driver.save_screenshot(img_out_path)
                element = driver.find_element_by_css_selector(
                    "#p_proDetail > .detailcont > .speedycat_container_root_class")
                save_image.save_prod_detail_image(element, img_out_path)

                input_prod_id += 1
                print("success! category : {} prod_id {}".format(
                    head_name, prod_id))
            except Exception as e:
                error_count += 1
                print("error count is " + str(error_count))
                print(e)
    driver.close()


if __name__ == "__main__":
    app()
