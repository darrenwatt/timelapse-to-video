import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    WEBCAM_PICS_DIR = os.getenv('WEBCAM_PICS_DIR') or '/data/' # base url to store snapshots
