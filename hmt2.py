#!/usr/bin/python3

import time, datetime

midnight = datetime.timedelta(0, 0, 0, 0, 0, 2, 0)
current_time = datetime.timedelta(0, 0, 0, 0, int(time.strftime('%M')), int(time.strftime('%H')), 0)

if current_time.__lt__(midnight):
    dst_time = datetime.timedelta(0, 0, 0, 0, 0, 2, 0)
else:
    dst_time = datetime.timedelta(1, 0, 0, 0, 0, 2, 0)

print('\nremaining time in seconds: ', int(dst_time.total_seconds() - current_time.total_seconds()), '\n')
