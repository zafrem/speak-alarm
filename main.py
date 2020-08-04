import utils.ntpClient as ntp
import utils.gCalendar as gcal
import utils.gSpeech as gspeech
import utils.yAudio as youtube
import utils.playMusic as playmusic
import datetime, time, schedule, os, logging
import logging.handlers
from datetime import timedelta
from apscheduler.schedulers.background import BackgroundScheduler

# Logger Setting
current_dir = os.path.dirname(os.path.realpath(__file__))
current_file = os.path.basename(__file__)
current_file_name = current_file[:-3] 
log_dir = '{}/logs'.format(current_dir)
if not os.path.exists(log_dir):
        os.makedirs(log_dir)
LOG_FILENAME = './logs/log_{}.log'.format(current_file_name)

logger = logging.getLogger('test') 
logger.setLevel(logging.DEBUG)

file_handler = logging.handlers.TimedRotatingFileHandler(
    filename=LOG_FILENAME, when='midnight', interval=1,  encoding='utf-8'
    )
file_handler.suffix = 'log-%Y%m%d'

logger.addHandler(file_handler)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] %(message)s'
    )
file_handler.setFormatter(formatter)

#Make scheduler Create
alarm_scheduler = BackgroundScheduler()
event_lists = []

#
# Main Function
#

def speaking_function():
    logger.info("Alarm Speaking function Start!")

    global event_lists, alarm_scheduler 

    alarm_scheduler.pause()

    #Set time (Used ntp)
    logger.info("Get NTP infomation.")

    now_datetime = ntp.now()
    if now_datetime == -1:
        now_datetime = datetime.datetime.now()

    strdate = now_datetime.strftime("%Y/%m/%d, %H:%M:%S")
    logger.info("NTP Time : " + strdate)

    #Clear events
    
    if not event_lists:
        logger.info("Scheduler Empty list.")
    else:
        for event_id in event_lists:
            try:
                alarm_scheduler.remove_job(event_id)
            except Exception as ex:
                pass
        event_lists = []
    logger.info("Clear Events.")
    
    #Schedule get google calendar api & file load
    logger.info("Get Google Calendar infomation.")
    events = gcal.getGoogleCalendar()
    logger.info("Google Calendar event count is " + str(len(events)))

    for event in events:
        if 'start' not in event:
            continue
        stime = (event['start'].get('dateTime', event['start'].get('date')))
        schTime = datetime.datetime.strptime(stime[0:16], '%Y-%m-%dT%H:%M').strftime("%s")
        alarmMinutes = 30
        if 'reminders' in event:
            remind = event['reminders']
            if ('useDefault' in remind) and (True != remind['useDefault']) and ('overrides' in remind):
                temp = remind['overrides']
                if 'minutes' in temp[0]:
                    alarmMinutes = int(temp[0]['minutes'])

        schTime = int(schTime) - int(alarmMinutes)*60
        str_arg = "\'" + event['summary'] + "\'"
        if datetime.datetime.now().timestamp() > int(schTime):
            continue

        alarm_scheduler.add_job(gspeech._textToSpeech, trigger="date", 
                run_date=str(datetime.datetime.fromtimestamp(schTime)),
                id=event['iCalUID'], args=(str_arg,))
        event_lists.append(event['iCalUID'])
        logger.info("Reg Event Time : " + str(datetime.datetime.fromtimestamp(schTime)) + ", Speech : " + str_arg)
        print("Reg Event Time : " + str(datetime.datetime.fromtimestamp(schTime)) + ", Speech : " + str_arg)

        #event['summary'])
        #event['description']
        #event['location']
        #event['start']
        #event['end']
        #event['reminders'] 'userDefault':True = 30 minutes 
        #                   'useDefault': False, 'overrides': [{'method': 'popup', 'minutes': 29}]}

        #FIXME Change Youtube Downlad to Streamming
        
        if 'description' in event:
            if 'youtube' in event['description'] :
                youtube.audioDownload(event['description'], './mp4', event['id'])
                schTime = int(schTime) - 10*60
                alarm_scheduler.add_job(playmusic.mp3ToSpeech, trigger="date", 
                        run_date=str(datetime.datetime.fromtimestamp(schTime)), 
                        id=(event['iCalUID'] + "_audio"), args=(str_arg,))
                event_lists.append(event['iCalUID'] + "_audio")
                logger.info("Reg Audio Event Time : " + str(datetime.datetime.fromtimestamp(schTime)) + 
                        ", Speech : " + './mp4/' + event['id'] + '.mp4')
    alarm_scheduler.resume()
    return


if __name__ == "__main__":
    logger.info("Alarm Speaking Main Start!")
    print("Alarm Speaking Start.")
    alarm_scheduler.add_job(speaking_function, 'interval', hours=1)
    
    try:
        alarm_scheduler.start()
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        pass
