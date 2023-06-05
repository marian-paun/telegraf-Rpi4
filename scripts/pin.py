#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import lgpio
import time

# Pin Number
PIN = 14

h = lgpio.gpiochip_open(0)
if h >= 0:
	print (h)
else:
	print ('error')

lgpio.gpio_claim_input(h, PIN)

if h == 0:
	print ('ok')
else:
	print ('error')
#pin_status = lgpio.gpio_read(h, PIN)
#print(pin_status)
lgpio.gpiochip_close(h)


