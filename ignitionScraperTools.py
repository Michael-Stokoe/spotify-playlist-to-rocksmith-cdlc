import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def login(driver, url):
    # Credentials used to login to CustomsForge. Don't forget to set this.
    credentials = {
        "ips_username": "your-username",
        "ips_password": "your-password"
    }
    driver.get(url)
    # Finds the login button and inputs
    loginUsernameInput = driver.find_element_by_css_selector("input#ips_username")
    loginPasswordInput = driver.find_element_by_css_selector("input#ips_password")
    # Fill the login form and sugmit.
    loginUsernameInput.send_keys(credentials['ips_username'])
    loginPasswordInput.send_keys(credentials['ips_password'])
    loginPasswordInput.send_keys(Keys.RETURN)
    # Wait until the index page loads
    WebDriverWait(driver, 10).until(EC.url_contains('index.php'))
    time.sleep(4)
    
def performAntiBotCounterMeasures(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class*="banner_continue"]'))
    )

    antiBotContinueButton = driver.find_element_by_css_selector('a[class*="banner_continue"]')

    actions = ActionChains(driver)
    actions.move_to_element(antiBotContinueButton)
    actions.click()
    actions.perform()

    time.sleep(4)
    
def searchForTrack(driver, searchTerms):
    time.sleep(4)
    searchText = searchTerms['artist'] + ' ' + searchTerms['title']
    searchInputBox = driver.find_element_by_id('search_input')
    time.sleep(2)
    searchInputBox.clear()
    time.sleep(5)
    searchInputBox.send_keys(searchText)
    time.sleep(2)
    searchInputBox.send_keys(Keys.RETURN)
    time.sleep(4)

def sortSongsByMostDownloads(driver):
    downloadsSorterButton = driver.find_element_by_css_selector('th[class*="downloads"')
    actions = ActionChains(driver)
    actions.move_to_element(downloadsSorterButton)
    actions.click()
    actions.perform()

    time.sleep(4)
    downloadsSorterButton = driver.find_element_by_css_selector('th[class*="downloads"')

    actions = ActionChains(driver)
    actions.move_to_element(downloadsSorterButton)
    actions.click()
    actions.perform()

    time.sleep(4)

def downloadSong(driver, songRow):
    time.sleep(1)

    dropdownButton = songRow.find_elements_by_css_selector('div[class*="open-context"')

    actions = ActionChains(driver)
    actions.move_to_element(dropdownButton[0])
    actions.click()
    actions.perform()

    time.sleep(1)

    downloadButton = songRow.find_elements_by_css_selector('a[class*="context-dl"')

    actions = ActionChains(driver)
    actions.move_to_element(downloadButton[0])
    actions.key_down(Keys.LEFT_CONTROL)
    actions.click()
    actions.key_up(Keys.LEFT_CONTROL)
    actions.perform()

    time.sleep(4)