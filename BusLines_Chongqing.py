import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def getBusStationName():
    options = webdriver.FirefoxOptions()
    options.set_headless()
    options.add_argument('--disable-gpu') # 静默启动火狐浏览器，即不要打开火狐浏览器
    option_profile = webdriver.FirefoxProfile()
    option_profile.set_preference("plugin.state.flash", 2)  # 开启flash插件（否者html5中的flash标签无法被渲染，如object就是flash标签）
    fbrs = webdriver.Firefox(firefox_profile=option_profile, firefox_options=options)
    fbrs.get('https://chongqing.8684.cn/line2')
    wait = WebDriverWait(fbrs, 60)
    buses = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="stie_list"]//a')))
    name = []
    for bus in buses:
        busName = 'busName'
        sName = bus.text
        name.append({busName: sName})

    fbrs.close()
    jsonData = json.dumps(name, indent=2, ensure_ascii=False)
    jsonFile = open('data.json', 'w', encoding='utf-8')
    jsonFile.write(jsonData)
    jsonFile.close()
getBusStationName()