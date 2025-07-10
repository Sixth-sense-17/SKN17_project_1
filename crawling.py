from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Car:
    def __init__(self, manufacture, car_name, purchase,):
        self.manufacture = manufacture
        self.car_name = car_name
        self.purchase = purchase
        

def crawl_car_sedan(page_num):
    path = 'chromedriver.exe'
    service = webdriver.chrome.service.Service(path)
    driver = webdriver.Chrome(service=service)

    sedan_dict = dict()
    
    driver.get('https://www.car365.go.kr/ccpt/carlife/newcar/registerCountAnalysisView.do?_menuId=M620102000&moblYn=Y')
    time.sleep(1)

    next_btn = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div/ul/li[1]/div[2]/span[2]')
    next_btn.click()
    time.sleep(1)

    next_btn = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div/ul/li[2]/div[2]/span[2]')
    next_btn.click()
    time.sleep(1)

    next_btn = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div/ul/li[3]/div[2]/span[2]')
    next_btn.click()
    time.sleep(1)

    next_btn = driver.find_element(By.XPATH, '//*[@id="ageScope"]/div[2]/span[1]')
    next_btn.click()
    time.sleep(1)

    next_btn = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div/ul/li[5]/div[2]/span[1]')
    next_btn.click()
    time.sleep(1)

    next_btn = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div/ul/li[6]/div[2]/span[1]')
    next_btn.click()
    time.sleep(1)

    next_btn = driver.find_element(By.XPATH, '//*[@id="form1"]/div/div/ul/li[7]/div[2]/span[1]')
    next_btn.click()
    time.sleep(1)

    for _ in range(page_num):
        tbody_tag = driver.find_element(By.ID, 'result-tbody')
        tr_tag = tbody_tag.find_elements(By.CSS_SELECTOR, 'tr')

        for tr in tr_tag:
            td_tag = tr.find_elements(By.CSS_SELECTOR, 'td')
            manufacture = td_tag[0].text
            car = td_tag[1].text
            purchase = int(td_tag[3].text.replace(',', ''))

            print(manufacture, car, purchase, type(purchase))
            new_car = Car(manufacture, car, purchase)
            
            if (manufacture, car) in sedan_dict.keys():
                sedan_dict[(manufacture, car)].purchase += new_car.purchase
            else:
                sedan_dict[(manufacture, car)] = new_car
            
            time.sleep(1)

        next_btn = driver.find_element(By.XPATH, '//*[@id="pageDiv"]/a[2]')
        next_btn.click()
        time.sleep(2)

    for i in sedan_dict:
        print(sedan_dict[i].manufacture, sedan_dict[i].car_name, sedan_dict[i].purchase)

    driver.quit()

    return sedan_dict
    
if __name__ == "__main__":
    crawl_car_sedan()
        



