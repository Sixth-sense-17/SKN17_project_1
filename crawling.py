from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Car:
    '''
    차 정보 저장용 클래스
    manufacture: 자동차 제조사
    car_name: 모델명
    purchase: 구매대수
    '''
    def __init__(self, manufacture, car_name, purchase,):
        self.manufacture = manufacture
        self.car_name = car_name
        self.purchase = purchase
        

def crawl_car_sedan(page_num):
    '''
    국산->개인->승용->전체->전체->전체->전체 카테고리를 선택하고
    나오는 자동차 정보들을 크롤링해 저장하고 반환하는 함수

    Args :
        page_num (int) :
            카테고리 선택 후 크롤링 할 페이지 개수
            
    Return :
        sedan_dict (dict) :
            크롤링 한 자동차 정보를 저장하고 있는 dictionary
            key : (manufacture, car_name)
                자동차 제조사, 자동차명을 묶은 튜플을 key값으로 사용
            value : Car 객체
                해당 key값을 가진 Car 객체 저장
    '''
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
    time.sleep(3)

    for i in range(page_num):
        tbody_tag = driver.find_element(By.ID, 'result-tbody')
        tr_tag = tbody_tag.find_elements(By.CSS_SELECTOR, 'tr')
        print(i, 'page')

        for tr in tr_tag:
            td_tag = tr.find_elements(By.CSS_SELECTOR, 'td')
            manufacture = td_tag[0].text
            car = td_tag[1].text
            purchase = int(td_tag[3].text.replace(',', ''))

            print(manufacture, car, purchase)
            new_car = Car(manufacture, car, purchase)
            
            if (manufacture, car) in sedan_dict.keys():
                sedan_dict[(manufacture, car)].purchase += new_car.purchase
            else:
                sedan_dict[(manufacture, car)] = new_car

        wait = WebDriverWait(driver, 10)
        next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.page-navi.next")))
        next_btn.click()
        time.sleep(2)

    print('-----------------------------------------')
    for i in sedan_dict:
        print(sedan_dict[i].manufacture, sedan_dict[i].car_name, sedan_dict[i].purchase)

    driver.quit()

    return sedan_dict


if __name__ == "__main__":
    crawl_car_sedan(50)
        



