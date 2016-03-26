#! python3

import reverse_file
import scramble_file
import delete_file
import open_youtube
import time
import webbrowser
import datetime


response = input('Commands:\'reverse\' / \'youtube\' / \'scramble\' / '
                 '\'delete\' / \'mess me up\': ')
if response == 'reverse':
    alarm_time = input('In how long? (xxx hours or xxx minutes or '
                       'xxx seconds:')
    if alarm_time.split(' ')[1] == 'hours':
        for i in range(int(3600 * float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    if alarm_time.split(' ')[1] == 'minutes':
        for i in range(int(60 * float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    if alarm_time.split(' ')[1] == 'seconds':
        for i in range(int(float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    webbrowser.open('https://www.youtube.com/watch?v=PowGPSdAxTI')
    time.sleep(180)
    reverse_file.reverse_file('Fake Home Directory')

if response == 'scramble':
    alarm_time = input('In how long? (xxx hours or xxx minutes or'
                       ' xxx seconds:')
    if alarm_time.split(' ')[1] == 'hours':
        for i in range(int(3600 * float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    if alarm_time.split(' ')[1] == 'minutes':
        for i in range(int(60 * float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    if alarm_time.split(' ')[1] == 'seconds':
        for i in range(int(float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    webbrowser.open('https://www.youtube.com/watch?v=PowGPSdAxTI')
    time.sleep(180)
    scramble_file.scramble_file('Fake Home Directory')

if response == 'delete':
    alarm_time = input('In how long? (xxx hours or xxx minutes or'
                       ' xxx seconds:')
    if alarm_time.split(' ')[1] == 'hours':
        for i in range(int(3600 * float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    if alarm_time.split(' ')[1] == 'minutes':
        for i in range(int(60 * float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    if alarm_time.split(' ')[1] == 'seconds':
        for i in range(int(float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    webbrowser.open('https://www.youtube.com/watch?v=PowGPSdAxTI')
    time.sleep(180)
    delete_file.delete_file('Fake Home Directory')

if response == 'youtube':
    alarm_time = input('In how long? (xxx hours or xxx minutes or'
                       ' xxx seconds:')
    if alarm_time.split(' ')[1] == 'hours':
        for i in range(int(3600 * float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    if alarm_time.split(' ')[1] == 'minutes':
        for i in range(int(60 * float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    if alarm_time.split(' ')[1] == 'seconds':
        for i in range(int(float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    webbrowser.open('https://www.youtube.com/watch?v=PowGPSdAxTI')
    time.sleep(180)
    while 1:
        time.sleep(10)
        open_youtube.open_youtube()

if response == 'mess me up':
    alarm_time = input('In how long? (xxx hours or xxx minutes or'
                       ' xxx seconds:')
    if alarm_time.split(' ')[1] == 'hours':
        for i in range(int(3600 * float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    if alarm_time.split(' ')[1] == 'minutes':
        for i in range(int(60 * float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    if alarm_time.split(' ')[1] == 'seconds':
        for i in range(int(float(alarm_time.split(' ')[0])), 0, -1):
            time.sleep(1)
            time_standard = datetime.timedelta(seconds=i)
            print(time_standard)
    webbrowser.open('https://www.youtube.com/watch?v=PowGPSdAxTI')
    time.sleep(180)
    delete_file.delete_file('Fake Home Directory')
    while 1:
        time.sleep(0.05)
        open_youtube.open_youtube()


