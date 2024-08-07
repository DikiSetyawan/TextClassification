from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pandas as pd
import time
import os

profUrl = 'https://twitter.com/kopididid'

driver = webdriver.Chrome()
driver.get(profUrl)
time.sleep(5)
