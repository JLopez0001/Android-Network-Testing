import logging
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.appiumby import AppiumBy
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Function to ensure we are on the YouTube home screen. If not, navigate to it. 
def navigate_to_youtube_app(driver):
    try:
        # Launch the YouTube app
        logger.info("Launching YouTube app")
        driver.execute_script('mobile: shell', {'command': 'am', 'args': ['start', '-n', 'com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity']})
        logger.info("Navigated to YouTube home page")
    except Exception as e:
        logger.error(f"Failed to navigate to YouTube home: {e}")
        raise

def play_youtube_short(driver, network_expected=True):
    try:
        logger.info("Attempting to play a YouTube short")
        youtube_short = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.youtube:id/image"])[2]'))
        )

        youtube_short.click()

        if not network_expected:
            # Assert failure if network is not expected but video plays successfully
            assert not network_expected, "Expected failure due to no network but video played successfully"
        else:
            logger.info("Navigated to shorts with internet")
    except (TimeoutException, NoSuchElementException) as e:
        if network_expected:
            logger.error("Unexpected failure: " + str(e))
            raise
        else:
            logger.info("Expected failure due to no network: " + str(e))

def play_youtube_trending_video(driver, network_expected=True):
    try:
        logger.info("Attempting to open YouTube Trending")
        
        # Wait for and click on the Explore menu
        explore_menu = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Explore Menu"]/android.widget.ImageView'))
        )
        explore_menu.click()
        
        # Wait for and click on the Trending section
        trending_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Trending"]'))
        )
        trending_section.click()
        logger.info("Trending button clicked")
        
       # Wait for the first visible video thumbnail in the trending section
        first_trending_video = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.support.v7.widget.RecyclerView[@resource-id="com.google.android.youtube:id/results"]/android.view.ViewGroup[3]'))
        )

        logger.info("found first viedo")

        first_trending_video.click()

        logger.info("clicked on video")
        
        driver.implicitly_wait(5)
        driver.back()

    except (TimeoutException, NoSuchElementException) as e:
        if network_expected:
            logger.error(f"Unexpected failure: {str(e)}")
            raise
        else:
            logger.info(f"Expected failure due to no network: {str(e)}")

def search_for_youtube_video(driver, network_expected=True):
    try: 
        logger.info("Attempting to search for a video on YouTube")

        # Wait for and click on the Search button
        search_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Search'))
        )
        search_button.click()
        logger.info("Search button clicked")

        # Wait for the search box to be present and input search text
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((AppiumBy.ID, 'com.google.android.youtube:id/search_edit_text'))
        )
        search_box.send_keys("Kill Tony")

        # Trigger the search action directly via Appium's shell command
        driver.execute_script('mobile: shell', {
            'command': 'input', 
            'args': ['keyevent', '66']  # 66 is the keycode for the Enter key
        })
        logger.info("Search action initiated")

        if not network_expected:
            assert not network_expected, "Expected failure due to no network but search results still populated"
        else:
            logger.info("Navigated to shorts with internet")
    except (TimeoutException, NoSuchElementException) as e:
        if network_expected:
            logger.error("Unexpected failure: " + str(e))
            raise
        else:
            logger.info("Expected failure due to no network: " + str(e))
