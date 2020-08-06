# Python Alarm speaking in AIYproject Voice kit (with Google Calender)
I trying to read the alarm using a Google AIYproject Voice kit.   

## Purpose of this repository

## Operating environment

## Program actions and effects


## Pre-Install   
**1. Download credentials.json file**   
 Web page : https://developers.google.com/calendar/quickstart/go   
 Action : Enable the Google Calendar API > Desktop app > Download Client configuration


**2. Move credentials.json file**   
 $ mv credentials.json [$PROJECT_HOME]/conf   

## Library Install   
**OS Library Install (in Ubuntu or Raspberry pi)**   
 $ sudo apt-get install sox libsox-fmt-mp3 ffmpeg   
 
**Python Library Install**   
 $ pip3 install ntplib google-api-python-client google-auth-oauthlib google_speech logger schedule pytube3 pydub   
 
## Run   
**Terminal Run**   
 $ python3 main.py   

**[FIXME] Startup Launcher**   
$ sh startup.sh   
