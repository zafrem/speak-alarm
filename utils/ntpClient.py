import ntplib
import time, datetime

def nowMonth():
    try :
        c = ntplib.NTPClient()
        response = c.request('kr.pool.ntp.org', version=3)
        date_time = datetime.datetime.fromtimestamp(response.tx_time)
        return date_time.month
    except :
        print("Error nowMonth()")
        return -1

def nowDay():
    try :
        c = ntplib.NTPClient()
        response = c.request('kr.pool.ntp.org', version=3)
        date_time = datetime.datetime.fromtimestamp(response.tx_time)
        return date_time.day
    except :
        print("Error nowDay()")
        return -1

def nowHour():
    try :
        c = ntplib.NTPClient()
        response = c.request('kr.pool.ntp.org', version=3)
        date_time = datetime.datetime.fromtimestamp(response.tx_time)
        return date_time.hour
    except :
        print("Error nowHour()")
        return -1

def nowMinute():
    try :
        c = ntplib.NTPClient()
        response = c.request('kr.pool.ntp.org', version=3)
        date_time = datetime.datetime.fromtimestamp(response.tx_time)
        return date_time.minute
    except :
        print("Error nowMinute()")
        return -1

def now():
    try :
        c = ntplib.NTPClient()
        response = c.request('kr.pool.ntp.org', version=3)
        date_time = datetime.datetime.fromtimestamp(response.tx_time)
        return date_time
    except :
        print("Error now()")
        return -1

if __name__ == "__main__":
    print ("month : " + str(nowMonth()))
    print ("day : " + str(nowDay()))
    print ("hour : " + str(nowHour()))
    print ("minute : " + str(nowMinute()))
    print ("now : " + str(now()))


