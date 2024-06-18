from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import regex as re

# Text Filtering using regex
def extract_tweet(text):
    pattern = r":(.*)"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return text

#Initialize driver
#options = webdriver.ChromeOptions()
#options.add_argument("--headless")
driver = webdriver.Chrome()
driver.get("https://huggingface.co/chat/")

#Get rid of cookies
cookies = driver.find_element(By.CSS_SELECTOR, ".whitespace-nowrap")
cookies.click()

#Fill in email button
email = driver.find_element(By.CSS_SELECTOR, ".mb-8 > label:nth-child(1) > input:nth-child(1)")
email.send_keys("valentino2006@me.com")

#Fill in password button
pwd = driver.find_element(By.CSS_SELECTOR, ".mb-8 > label:nth-child(2) > input:nth-child(1)")
pwd.send_keys("Vuwken-jumty3-vagwuw")

#Click login button
login = driver.find_element(By.CSS_SELECTOR, ".btn")
login.click()

#Click user prompt 
prompt = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/form/div/div/textarea')
prompt.click()

time.sleep(1)

#Enter user prompt
prompt.send_keys("Erstelle mir einen Tweet!")
prompt.send_keys(Keys.RETURN)

time.sleep(30)

#Fetch tweet
new_tweet = driver.find_element(By.CSS_SELECTOR,'#app > div.grid.h-full.w-screen.grid-cols-1.grid-rows-\[auto\,1fr\].overflow-hidden.text-smd.md\:grid-cols-\[280px\,1fr\].transition-\[300ms\].\[transition-property\:grid-template-columns\].md\:grid-rows-\[1fr\].dark\:text-gray-300 > div > div.scrollbar-custom.mr-1.h-full.overflow-y-auto > div > div > div.group.relative.-mb-6.flex.items-start.justify-start.gap-4.pb-4.leading-relaxed > div.relative.min-h-\[calc\(2rem\+theme\(spacing\[3\.5\]\)\*2\)\].min-w-\[60px\].break-words.rounded-2xl.border.border-gray-100.bg-gradient-to-br.from-gray-50.px-5.py-3\.5.text-gray-600.prose-pre\:my-2.dark\:border-gray-800.dark\:from-gray-800\/40.dark\:text-gray-300 > div')

#convert new_tweet object to text
tweet_text = new_tweet.text

#close driver
driver.close()

#return tweet
def return_tweet():
    return extract_tweet(tweet_text)