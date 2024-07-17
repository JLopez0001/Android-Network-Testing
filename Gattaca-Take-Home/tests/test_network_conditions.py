import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import logging
import pytest

from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType

from utils.appium_setup import get_driver
from utils.youtube_helpers import play_youtube_short, navigate_to_youtube_app, play_youtube_trending_video, search_for_youtube_video

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@pytest.fixture(scope='module')
def driver():
    driver = get_driver()

    # Navigate to the youtube
    navigate_to_youtube_app(driver)

    yield driver
    driver.quit()

#FOR DATA ONLY
# def set_network_connection(driver, connection_type):
#     """
#     Helper function to set network connection type on the device.
#     """
#     actions = {
#         "disconnect_data": (ConnectionType.NO_CONNECTION, "Disconnecting cellular data"),
#         "reconnect_data": (ConnectionType.DATA_ONLY, "Reconnecting cellular data"),
#     }
    
#     try:
#         action = actions.get(connection_type)
#         if action:
#             logger.info(action[1])
#             driver.set_network_connection(action[0])
#         else:
#             logger.warning(f"Unknown network connection type: {connection_type}")
#     except Exception as e:
#         logger.error(f"Failed to set network connection: {e}")
#         raise


############  THIS TEST CAN BE CONDUCTED WITH WIFI ONLY OR DATA PLEASE CHOOSE DESIRED NETWORK ########################

# Helper function to set network connection type on the device.
def set_network_connection(driver, connection_type):
    actions = {
        "disconnect_wifi": (ConnectionType.NO_CONNECTION, "Disconnecting Wi-Fi"),
        "reconnect_wifi": (ConnectionType.WIFI_ONLY, "Reconnecting Wi-Fi"),
        "disconnect_data": (ConnectionType.NO_CONNECTION, "Disconnecting cellular data"),
        "reconnect_data": (ConnectionType.DATA_ONLY, "Reconnecting cellular data"),
    }
    
    try:
        action = actions.get(connection_type)
        if action:
            logger.info(action[1])
            driver.set_network_connection(action[0])
        else:
            logger.warning(f"Unknown network connection type: {connection_type}")
    except Exception as e:
        logger.error(f"Failed to set network connection: {e}")
        raise


#Test case to verify YouTube's behavior when the network is Connected.
def test_network_connection(driver):
    logger.info("Starting test: test_network_connection")
    
    ########## REPLACE reconnect_wifi with the desired actions of the set_network_connection function ################
    # Verify network is reconnected
    set_network_connection(driver, "reconnect_wifi")
    
    navigate_to_youtube_app(driver)

    # Play trending video
    play_youtube_trending_video(driver, network_expected=True)

    # Play YouTube short video
    play_youtube_short(driver, network_expected=True)

    # Search for a YouTube video
    search_for_youtube_video(driver, network_expected=True)


# Test case to verify YouTube's behavior when the network is disconnected
def test_network_disconnection(driver):
    logger.info("Starting test: test_network_disconnection")

    # Simulate network disconnection
    set_network_connection(driver, "disconnect_wifi")

    navigate_to_youtube_app(driver)

    # Play YouTube short video
    ##### PLEASE BE AWARE THAT IF THERE IS AN AD IT WILL NEED TO BE EXITED MANUALLY #########
    play_youtube_short(driver, network_expected=False)

    # Play trending video
    play_youtube_trending_video(driver, network_expected=False)

    # Search for a YouTube video
    search_for_youtube_video(driver, network_expected=False)    
        
    set_network_connection(driver, "reconnect_wifi")

if __name__ == "__main__":
    pytest.main(["-s", "test_network_conditions.py"])
