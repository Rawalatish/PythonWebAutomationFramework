
from selenium import webdriver  
import pytest  
from dotenv import load_dotenv  
import os  

load_dotenv()  

@pytest.fixture(scope="class")  
def setup(request):  
    driver = webdriver.Chrome()  
    driver.maximize_window()  

    username = os.getenv("USERNAME")  
    password = os.getenv("PASSWORD")  
    base_url = os.getenv("BASE_URL")  

    request.cls.driver = driver  
    request.cls.username = username  
    request.cls.password = password  
    request.cls.base_url = base_url  

    yield driver  
    driver.quit()  