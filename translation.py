class Translation(object):
    START_TEXT = """Hi!
    
Enter your Telegram Phone Number, to get the APP-ID from my.telegram.org

/start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """Please send the Telegram code that you received from Telegram!"""
    BEFORE_SUCC_LOGIN = "Recieved code. Scrapping web page ..."
    ERRED_PAGE = "Something went wrong. failed to get app id. \n\n@MysticOp"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "Sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "Sorry, but the input does not seem to be a valid phone number"
