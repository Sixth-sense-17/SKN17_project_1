from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def faq_kia():

    path = 'chromedriver.exe'
    service = webdriver.chrome.service.Service(path)
    driver = webdriver.Chrome(service=service)

    driver.get('https://www.kia.com/kr/customer-service/center/faq')
    time.sleep(1)

    faq_data = []

    # 탭 버튼 클릭
    next_btn = driver.find_element(By.XPATH,'//*[@id="tab-list"]/li[3]/button')
    next_btn.click()
    time.sleep(1)

    # 첫 번째 항목 열기
    next_btn = driver.find_element(By.XPATH,'//*[@id="accordion-item-0-button"]/span[2]')
    next_btn.click()
    time.sleep(1)

    # FAQ 항목 수집
    faq_items = driver.find_elements(By.CSS_SELECTOR, 'div.cmp-accordion__item')

    for i, item in enumerate(faq_items):
        # 안정성 확보: 버튼/아이템 새로 갱신
        buttons = driver.find_elements(By.CSS_SELECTOR, 'div.cmp-accordion__item button.cmp-accordion__button')
        items = driver.find_elements(By.CSS_SELECTOR, 'div.cmp-accordion__item')

        buttons[i].click()
        time.sleep(0.5)

        title_content = items[i].find_element(By.CSS_SELECTOR, 'span.cmp-accordion__title').text
        response_content = items[i].find_element(By.CSS_SELECTOR, 'div.cmp-accordion__panel p').text

        faq_dict = {
            '질문': title_content,
            '답변': response_content
        }
        faq_data.append(faq_dict)   

    driver.quit()
    return faq_data

if __name__ == '__main__':
    print(faq_kia())