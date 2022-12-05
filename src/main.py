from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from set_cookies import set_cookies
from dotenv import load_dotenv
import os
from queries import try_again, submit_query

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)


def main():

    load_dotenv()
    init_chat()

    updater = Updater(token=os.getenv('BOT_TOKEN'))
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(~Filters.command, handle_messages))
    dispatcher.add_handler(CommandHandler("try_again", handle_try_again))
    dispatcher.add_handler(CommandHandler("reset_thread", handle_reset))

    updater.start_polling()
    updater.idle()


def handle_try_again(update: Update, context: CallbackContext) -> None:
    response = try_again(driver, update, context)
    update.message.reply_text(response)


def handle_reset(update: Update, context: CallbackContext) -> None:
    driver.get("https://chat.openai.com")
    update.message.reply_text("Resetting thread...")


def handle_messages(update: Update, context: CallbackContext) -> None:
    if update.message:
        response = submit_query(driver, update.message.text, update, context)
        update.message.reply_text(response)


def init_chat():

    driver.get("https://chat.openai.com")
    set_cookies(driver)
    driver.get("https://chat.openai.com")

    time.sleep(1)

    # skip popup dialog
    driver.find_elements(
        By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button")[0].click()
    driver.find_elements(
        By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button[2]")[0].click()
    driver.find_elements(
        By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button[2]")[0].click()

    print('Bot is ready to chat')


if __name__ == "__main__":
    main()
