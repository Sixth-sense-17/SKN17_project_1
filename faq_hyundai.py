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

if __name__ == "__main__":    
    new_list = faq_hyundai()
    for i in new_list:
        print(i)
