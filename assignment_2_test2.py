from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximize the browser window
driver.maximize_window()

# Navigate to the YouTube page
driver.get('https://www.youtube.com/@markets')

# Allow the page to load
time.sleep(30)

# Scroll through the page to load dynamic content
scroll_height = driver.execute_script('return document.body.scrollHeight')
for i in range(0, scroll_height+1500, 500):
    driver.execute_script(f'window.scrollTo(0, {i});')
    time.sleep(1)

# Extract page source
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find all video links
video_links = []
for a in soup.find_all('a', href=True):
    if '/watch' in a['href']:
        video_links.append(f"https://www.youtube.com{a['href']}")

# Remove duplicates
video_links = list(set(video_links))

# Print video links
for link in video_links:
    print(link)

# Close the WebDriver
driver.quit()
