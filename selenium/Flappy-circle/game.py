from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://tanksw.com/flappy-circle/") # 게임화면 로드


play_button = driver.find_element_by_css_selector("div#menu") # div 테그에 #(id)가 menu 인것
replay_button = driver.find_element_by_css_selector("div#replay") # div 테그에 #(id)가 replay 인것
play_button.click()
driver.execute_script("return window.sound =false") # 소리 변수 조작해서 소리끄기

while(True):
    is_playing = driver.execute_script("return window.isPlaying") # js 의 isPlaying 이 라는 변수를 가져온다.
    if not is_playing: #게임중인 상태가 아니라면 = 죽은상태
        time.sleep(3)
        replay_button.click() # 재시작
        time.sleep(2)
        play_button.click()

    pos_now = driver.execute_script("return window.PosNow") # 원의 좌표
    lines = driver.execute_script("return window.line") # 닿으면 안되는 라인 좌표
    cp = int(driver.execute_script("return window.CP")) # 원이 어떤 라인에있는지 인덱스


    nowLineHeight = -(lines[cp + 1][0] - pos_now[0]) * ((lines[cp + 1][1] - lines[cp][1]) / (lines[cp + 1][0] - lines[cp][0])) + lines[cp + 1][1]
    
    gap = (nowLineHeight-8) - (pos_now[1]-65) # js에서 얻어온 충돌 조건 값 (원의 상단이 줄보다 낮다면 충돌)
    if gap < 10 : # 여유가 10보다 작다면
        driver.execute_script("mouseListener(new Event('none'))") # js 에있는 mouseListener() 를 호출하여 점프
        time.sleep(0.1)

    # 걍 죽는 메소드를 변경시켜서 절대 안죽게 하기
    #driver.execute_script("checkCollision =  function (checkPoint) { return false; };")