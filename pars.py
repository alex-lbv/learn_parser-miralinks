from selenium import webdriver
import time
import csv
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class MiralinksParser:

    def __init__(self):
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_setting_values': {'images': 2}}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(executable_path='/Users/macbook/Desktop/Work/parser-miralinks/chromedriver', options=options)
        self.transin_to_site()
        self.login_in_site()
        self.transin_to_catalog()
        # self.see_all_list()
        pages = 1
        while pages <= 661:
            print(pages, '________________________________', pages)
            self.pars_table()
            pagination = self.driver.find_element_by_class_name('next')
            pagination.click()
            pages += 1
            time.sleep(2)

    def transin_to_site(self):
        self.driver.maximize_window()
        self.driver.get("https://www.miralinks.ru/")

    def login_in_site(self):
        email = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/input')
        email.send_keys('aal940722r')
        passw = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/input')
        passw.send_keys('vold6SOPT-shog_shif')
        login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[4]/a/span/span')
        login.click()
        time.sleep(1)

    def transin_to_catalog(self):
        self.driver.get('https://www.miralinks.ru/catalog')
        time.sleep(5)

    # def see_all_list(self):
    #     self.driver.find_element_by_xpath('/html/body/div[21]/section/div/div/div/div[3]/div[6]/div[4]/div[3]/a[2]').click()
    #     time.sleep(9)

    def pars_table(self):
        table_id = self.driver.find_element_by_id('Catalog_50479333')
        tbody = table_id.find_element_by_tag_name('tbody')
        rows = tbody.find_elements_by_tag_name('tr')
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            all_td = [(cells[i].text) for i in range(len(cells))]
            #print(all_td)
            with open("miralinks.csv", mode="a", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r\n")
                file_writer.writerow([(cells[i].text) for i in range(len(cells))])

def main():
    gp= MiralinksParser()

if __name__ == '__main__':
    main()