import os
from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

class Veez(object):
        admins = {}
        BOT_TOKEN = getenv("BOT_TOKEN", "1825536303:AAFdViSgyUoYGKr8mHMjUNpLsGpPjNavuTE")
        CHANNEL = int(os.getenv('CHANNEL', 123456))
        API_ID = int(getenv("API_ID", "3866700"))
        API_HASH = getenv("API_HASH", "629f9f3c93bf94c9276722876ca610a1")
        SESSION_NAME = getenv("SESSION_NAME", "BQCMRCbhEiDD_6Vb8dHvq4xGj5Syepz50Ighu1metgv1kXK0WZdeGnGQ_6Q909Lg2bkc-6sxGRZatCI-ENqXmkNmPDx5JBVzqs93M0Uixv6DC4MzRrda6Ns-D_Iu2sja7UYhq0vpkCE7f4s1SKNH7gjqYMP3BODH3GY-Vfb3ApJvR68jU5u72VKhRlu__rHAtX8LuADWdMU3-5dJJa4HwmgdfEe_x-r8HziFHZ--e-8r5XAw4dTyB7xhaTEliF19paZ-vBzzF0Fgk2eR52Rsxv-GOB95bsoPO4D92xQPKt3TYLc-vfDSaQV-f3SHkbjkwa08S0hXzbs_9aoU3l-AUt6zVOFnuAA")
        DURATION_LIMIT = int(getenv("DURATION_LIMIT", "50"))
        SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
        ASSISTANT_NAME = getenv("ASSISTANT_NAME", "TwincyRobot")
        BOT_USERNAME = getenv("BOT_USERNAME", "TwincyBot")
        COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
