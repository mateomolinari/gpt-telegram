from selenium.webdriver.common.by import By
from telegram import ChatAction
import time

input_field = "/html/body/div[1]/div/div[1]/main/div[2]/form/div/div[2]/textarea"
submit_button = "/html/body/div[1]/div/div[1]/main/div[2]/form/div/div[2]/button"
reset_thread = "/html/body/div[1]/div/div[2]/div/div/nav/a[1]"
try_again = "/html/body/div[1]/div/div[1]/main/div[2]/form/div/div[1]/button"


def try_again(driver, update, context) -> None:
    return submit_query(driver, "try again", update, context)


def submit_query(driver, query, update, context):
    assert (type(query) == str)

    try:
        driver.find_elements(By.XPATH, input_field)[0].send_keys(query)
        driver.find_elements(By.XPATH, input_field)[0].submit()

        response = ""

        time.sleep(0.25)
        while True:
            context.bot.send_chat_action(
                chat_id=update.message.chat_id, action=ChatAction.TYPING)
            temp_response = driver.find_elements(
                By.CLASS_NAME, "prose")[-1].text

            if temp_response == "":
                continue

            if temp_response != response:
                response = temp_response
            else:
                return response

            time.sleep(0.5)

    except:
        return 'Error: Could not submit query'
