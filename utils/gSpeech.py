from google_speech import Speech
import os, datetime, sys
import logging.handlers

def textToSpeech(text):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    current_file = os.path.basename(__file__)
    current_file_name = current_file[:-3]
    log_dir = '{}/logs'.format(current_dir)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    LOG_FILENAME = current_dir + '/../logs/log_{}.log'.format(current_file_name)
    logger = logging.getLogger('Google-Speech')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename=LOG_FILENAME, when='midnight', interval=1, encoding='utf-8'
        )
    file_handler.suffix = 'log=%Y%m%d'
    logger.addHandler(file_handler)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] %(message)s'
        )
    file_handler.setFormatter(formatter)

    try :
        sox_effects=("speech", "2")
        sox_effects=("vol", "1")

        lang="en_US"
        now_time = datetime.datetime.now().strftime("%Y %H %M %d%m")
        speech = Speech(now_time, lang)
        speech.play(sox_effects)

        lang="ko_KR"
        speech = Speech(text, lang)
        speech.play(sox_effects)
    except Exception as ex:
        logger.info("Exception sox Error(google speech).")

    logger.info("[" + now_time + "] Text : " + text)

if __name__ == "__main__":
    textToSpeech("Hi Google Speech")
