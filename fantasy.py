from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Fantasy:
    def __init__(self):
        self.driver = webdriver.Safari()  # Add path if needed: webdriver.Chrome(executable_path="/path/to/chromedriver")
    
    def draftplayer(self, player_name):
        print(f"Drafting {player_name}")
        driver = self.driver
        
        self.login("user", "pass")
        # Open the website
        driver.get("https://fantasy.espn.com/football/draft?leagueId=1975166350&seasonId=2023&teamId=9&memberId={93843567-797E-420C-87AA-304E13F718E4}")
        
        # Wait for the player's name to be visible
        player_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{player_name}')]"))
        )
        
        # Find the draft button associated with the player
        draft_button = player_element.find_element(By.XPATH, ".//following-sibling::*/button[@class='Button Button--draft']")
        player_id = draft_button.get_attribute("data-player-id")
        draft_button = driver.find_element(By.CSS_SELECTOR, f"[data-player-id='{player_id}']")
        
        # Draft the player
        draft_button.click()
        print(f"Drafted {player_name}")

    def login(self, username, password):
        driver = self.driver
        driver.get("https://plus.espn.com")  # Replace with the actual login URL
        #wait 3 seconds for page to load
        # Find the button by its type and aria-label attributes
        exit_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='button'][@aria-label='Close']"))
        )
        exit_button.click()

        login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".extra-small.tertiary")))
        login_button.click()

        # Assuming the username field can be found by its name attribute
        username_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='InputIdentityFlowValue']"))
        )
        username_field.send_keys(username)

        continue_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "BtnSubmit")))
        continue_button.click()

        # Assuming the password field can be found by its name attribute
        password_field = driver.find_element(By.NAME, "InputPassword")
        password_field.send_keys(password)

        # Clicking the login button
        login_button = driver.find_element(By.ID, "BtnSubmit")  # Replace with the actual button's identifier
        login_button.click()
        
