from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def faq_hyundai():
    '''
    현대 홈페이지에서 나온 FAQ들을 크롤링해 반환.

    Args :
        None
    
    Return :
        hyundai_FAQ_list (list) :
            원소를 (질문, 답변) 튜플로 가지는 리스트 반환
    '''

    path = 'chromedriver.exe'
    service = webdriver.chrome.service.Service(path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    hyundai_FAQ_list = []

    driver.get('https://www.hyundai.com/kr/ko/e/customer/center/faq')
    time.sleep(3)

    next_btn = driver.find_elements(By.CSS_SELECTOR,'div.list-wrap div.list-item')

    print(len(next_btn))
    for btn in next_btn:
        btn.click()
        time.sleep(1)

        title_tag = btn.find_element(By.CSS_SELECTOR, 'div.title')
        title = title_tag.text.strip('[차량구매]').replace('\n\n', ' ').replace('\n', ' ')
        div_conts_tag = btn.find_element(By.CSS_SELECTOR, 'div.conts > div')
        content = div_conts_tag.text.replace('\n', ' ')

        hyundai_FAQ_list.append((title, content))
        time.sleep(2)
        
    driver.quit()
    
    return hyundai_FAQ_list

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

        faq_dict = (title_content, response_content)
        faq_data.append(faq_dict)

    driver.quit()
    return faq_data


if __name__ == "__main__":    
    new_list = faq_hyundai()
    for i in new_list:
        print(i)
    print(faq_kia())
