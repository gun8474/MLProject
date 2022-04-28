import os.path
import time
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def createFoledr(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print('Error: Creating directory. ' + dir)

def crawling_image(name):
    chromedriver = './chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl") # 구글 이미지 검색 url

    elem = driver.find_element_by_name('q') # 구글 검색창 선택
    elem.send_keys(name) # 검색창에 검색할 이름 넣기
    elem.send_keys(Keys.RETURN) # 검색한 내용 Enter 역할

    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script('return document.body.scrollHeight') # 브라우저의 높이를 자바스크립트로 찾음

    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # 브라우저의 끝까지 스크롤을 내림

        # page가 load할 때 까지 wait
        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector('.mye4qd').click() # 스크롤을 내리다가 '결과 더보기'가 뜨는 경우 이를 클릭
            except:
                break

        last_height = new_height

    imgs = driver.find_elements(By.CSS_SELECTOR, '.rg_i.Q4LuWd') # 작게 뜬 이미지들을 모두 선택
    dir = './image/' + name

    createFoledr(dir)
    count = 1
    for img in imgs:
        try:
            img.click()
            time.sleep(5)
            # imgURL = driver.find_elements_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute('src')
            imgURL = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute('src')
            path = 'C:/Users/USER/prlab/AtoZ/MLProject1/image/' + name + '/'
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'MyApp/1.0')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgURL, path + name + str(count) + '.jpg')
            count = count + 1
            if count >= 100:
                break
        except:
            pass
    driver.close()

names = [ '이광수', '하하', '지석진', '송지효', '강호동', '전소민', '양서찬', '정준하', '박명수', '박나래', '전현무',
         '노홍철', '송은이', '티파니', '화사', '장도연', '솔라', '김준현', '이경규', '데프콘', '김태희', '전지현', '송강호',
         '광희', '써니', '박혜미', '이순재', '신동엽', '주현영', '안영미', '엄정화', '박미선', '조혜련', '수지', '지드레곤',
         '양세형', '이승기', '김소연', '엄기준', '조수민', '강동원', '원빈', '장동건', '안정환', '서장훈', '현영', '오지헌',
         '정종철', '박준형', '이수민', '이수근', '탁재훈', '김종국', '전소미', '강하나', '오나미', '김지민', '김준호', '한지민',
         '박민영', '구준엽', '김현중', '김우빈', '정우성', '황정민', '박수진', '이지아', '아이린', '제니', '장원영', '제시', '이이경',
         '지수', '손나은', '노사연', '이무송', '한채영', '최수종', '장나라', '문근영', '박보영', '신세경', '황정음', '윤시윤', '최지우',
         '고두심', '윤여정', '하지원', '강하늘', '김혜수', '진지희', '송혜교', '박보검', '차은우', '김희선', '현빈', '손예진', '베성재', '이민호']
for name in names:
    crawling_image(name)




