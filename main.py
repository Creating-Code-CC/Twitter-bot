import time
import random
from selenium import webdriver # Selenium is webdriver, you can refer to this as a Chrome window since that is what we will be initializing it as.
from selenium.webdriver.common.by import By # By will help us to select html elements.
driver = webdriver.Chrome()
driver.get("https://twitter.com/i/flow/login") # Open up the twitter log in page.
time.sleep(2)

# Locate first input element and send text.
username = driver.find_element(By.TAG_NAME, "input")
username.send_keys('JFlecco')
all_buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
all_buttons[-2].click()
time.sleep(2)

# Locate password field and send text.
password = driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys("VbotGotcha!@")
time.sleep(2)

# Finally, log in.
all_buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
all_buttons[-1].click()
time.sleep(2)

# Query something on twitter
search_for = "Python"
driver.get(f"https://twitter.com/search?q={search_for}&src=typed_query")
time.sleep(3)

# Make a list of messages to automate.
messages = ["Wowwwwwww!!!", "Amazingggg!!!!", "Fantastic!!!!!"]
n_scrolls = 3
for scroll in range(n_scrolls):
    '''I am looping to retweet 3 tweets. find the retweet element, confirm the tweet option, send your message to input field, and tweet. at the very end js is used to scroll
    and collect a new batch of tweets. This is because we are tweeting the last post in the visible batches so we scroll to find more. Lastly,
    if you run into any errors, try adjusting your sleep time a few seconds after each render.'''
    retweet = driver.find_elements(By.XPATH, "//div[@data-testid='retweet']")
    retweet[-1].click()
    time.sleep(2)


    confirm_retweet = driver.find_element(By.XPATH, "//a[@role='menuitem']")
    confirm_retweet.click()
    time.sleep(2)

    quote = driver.find_element(By.XPATH, "//div[contains(@class, 'public-DraftStyleDefault-block')]")
    quote.send_keys(random.choice(messages))
    time.sleep(2)

    send_the_tweet = driver.find_element(By.XPATH, "//div[@data-testid='tweetButton']")
    send_the_tweet.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)