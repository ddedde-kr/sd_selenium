from time import sleep
import pyautogui 
global shadow, driver

def set_driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    from pyshadow.main import Shadow
    global driver , shadow
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        chrome_options.add_argument("--window-size=1540,1162"  )
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("http://127.0.0.1:7860")
        driver.implicitly_wait(5)
        shadow = Shadow(driver)
        shadow.set_explicit_wait(20, 5)
        return True
    except:
        return False

def get_element_xpath(xpath_value):
    element = shadow.find_element(xpath_value)
    return element
 
def send_key_xpath(xpath_value, send_key_value):
    # from selenium.webdriver.common.keys import Keys
    try:
        element_value = get_element_xpath(xpath_value)
        element_value.send_keys(send_key_value)
        return True
    except:
        return False

def send_key_element(send_key_value):
    try:
        import pyperclip
        pyautogui.moveTo(500, 300)
        pyautogui.click()
        pyperclip.copy(send_key_value)
        pyautogui.hotkey('ctrl', 'v') 
        sleep(2)
        return True
    except:
        return False

def get_wait_height():
    xpath_value = "div#txt2img_results>div" ## 결과 창 
    try:
        element = shadow.find_element(xpath_value) 
        size = element.size
        h = size['height']
        return int(h)
    except:
        return 0

def click_xpath_from_shadow(xpath_value):
    try:
        element = shadow.find_element(xpath_value) ## 정상 동작 한다 이건 
        element.click()
        return True
    except:
        return False
    
def generate_image():
    height_wait = get_wait_height()
    xpath_value = "button#txt2img_generate"
    click_xpath_from_shadow(xpath_value)
    sleep(2)
    while 1:
        height_wait_temp = get_wait_height()
        if height_wait_temp == height_wait:
            sleep(1)
            return True
    return False

def save_image():
    xpath_value = "button#save_txt2img"
    click_xpath_from_shadow(xpath_value)
    return True

def run_generate(text_value, number_of_iterations = 1 ):
    if not isinstance(number_of_iterations, int):
        return False
    if number_of_iterations < 1 :
        return False
    set_driver()
    send_key_element(text_value)
    for i in range(0 , number_of_iterations):
        generate_image()   
        # sleep(1)
        save_image()
        print("[ " , i + 1 , " / " , number_of_iterations , " ] 회 동작 진행 하였습니다. " )
        sleep(10)
         