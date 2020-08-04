import unittest
import utils.ntpClient as ntp
import utils.gCalendar as gcal
import utils.gSpeech as gspeech
import utils.yAudio as youtube
import datetime, time
import logging
import logging.handlers
import sched
import schedule
import os
from datetime import timedelta


def speaking_agent():
    logger.info("Speaking Alarm Main Start!")

    sch = sched.scheduler(time.time, time.sleep)
    speaking_agent()
    schedule.every().hour.do(speaking_agent)

    while True:
        schedule.run_pending()
        time.sleep(1)


    logger.info("Speaking Alarm agnet Start!")
    print("Speaking Alarm Start!", datetime.datetime.now())

    #get time (ntp client)
    logger.info("Get NTP infomation.")

    now_datetime = ntp.now()
    if now_datetime == -1:
        now_datetime = datetime.datetime.now()

    strdate = now_datetime.strftime("%Y/%m/%d, %H:%M:%S")
    logger.info("NTP Time : " + strdate)

    #clear events
    if True != sch.empty():
        for event in sch.queue:
            sch.cancel(event)
        logger.info("Clear Event")

    #get schedule (google calendar api) & file load
    logger.info("Get Google Calendar infomation.")
    events = gcal.getGoogleCalendar()
    logger.info("Google Calendar event(" + str(len(events)) + ")")

    for event in events:
        if 'start' not in event:
            continue
        stime = (event['start'].get('dateTime', event['start'].get('date')))
        schTime = datetime.datetime.strptime(stime[0:15], '%Y-%m-%dT%H:%M').strftime("%s")

        if 'reminders' in event:
            remind = event['reminders']
            alarmTime = 0
            if 'useDefault' not in remind:
                alarmMinutes= 30
            else :
                if True == remind['useDefault']:
                    alarmMinutes= 30
                else :
                    if 'overrides' not in remind:
                        alarmMinutes = 30
                    else:
                        temp = remind['overrides']
                        alarmMinutes = int(temp[0]['minutes'])
            schTime = int(schTime) - alarmMinutes*60
        str_arg = "\'" + event['summary'] + "\'"
        sch.enterabs(int(schTime), 1, gspeech.ptextToSpeech, argument=(str_arg,))
        print(schTime, event['summary'])
        #event['summary'])
        #event['description']
        #event['location']
        #event['start']
        #event['end']
        #event['reminders'] 'userDefault':True = 30 minutes 
        #                   'useDefault': False, 'overrides': [{'method': 'popup', 'minutes': 29}]}
        if 'description' in event:
            if 'youtube' in event['description'] :
                youtube.audioDownload(event['description'], './mp3', event['id'])
                schTime = int(schTime) - 10*60
                sch.enterabs(int(schTime), 1, gspeech.pmp3ToSpeech, argument=('./mp3/'+ event['id'],))
    sch.run(blocking=False)
    return

class alarmTest(unittest.TestCase):
    def test_ntp(self):
        self.assertEqual(datetime.datetime.nmow(), ntp.now())
    def test_gcal(self):
    def test_gspeech(self):
    def test_youtube(self):
    def test_sch_add(self):
    def test_sch_del(self):

if __name__ == "__main__":
    unittest.main()

