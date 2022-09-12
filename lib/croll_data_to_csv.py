from selenium import webdriver
import csv


def save_csv(
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
):
    with open(f'out/{head_name}.csv', 'a') as f:
        wr = csv.writer(f, lineterminator='\n')
        wr.writerow([
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
            create_date
        ])


def make_scv(driver, li_list):
    head = driver.find_element_by_css_selector(
        'section.categorylist > div.depth > h2').text
    with open(f'out/{head}.csv', 'w') as f:
        wr = csv.writer(f, lineterminator='\n')
        for i in range(li_list):
            number_of_li_elements = len(driver.find_elements_by_xpath(
                f'//*[@id="ulItemList"]/li[{i+1}]/*'))
            li_elements = driver.find_elements_by_xpath(
                f'//*[@id="ulItemList"]/li[{i+1}]/*')

            url = li_elements[0].find_element_by_xpath(
                f'//*[@id="ulItemList"]/li[{i+1}]/a/span/img').get_attribute('src')
            price = li_elements[0].find_element_by_xpath(
                f'//*[@id="ulItemList"]/li[{i+1}]/span/span/strong/em').text.replace(',', '')

            sale_and_product = li_elements[0].find_element_by_xpath(
                f'//*[@id="ulItemList"]/li[{i+1}]/a/strong').text
            split_index = sale_and_product.find(']')
            if split_index == -1:
                continue
            sale = sale_and_product[:split_index].split('[')[1].strip()
            product = sale_and_product[split_index:].replace(
                ']', '', 1).strip()

            tag_list = ""
            if number_of_li_elements > 2:
                tags = li_elements[0].find_elements_by_xpath(
                    f'//*[@id="ulItemList"]/li[{i+1}]/span[2]/*')
                for tag in tags:
                    tag_list += str(tag.text)+', '
                tag_list = tag_list[:-2]

            wr.writerow([sale, product, price, url, tag_list])
