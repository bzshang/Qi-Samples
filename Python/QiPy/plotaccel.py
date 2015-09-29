from qipy import *
import datetime

import requests as req
import json

from dateutil import parser

import matplotlib.pyplot as plt

#print method for returned events
def dumpEvents(foundEvents):
    print "Total Events found: "+ str(len(foundEvents))
    for i in foundEvents:
        print i


authItems = {'resource' : "https://qihomeprod.onmicrosoft.com/historian",
             'authority' : "https://login.windows.net/b36cfd3b-8749-4898-9d6d-db0e18747472/oauth2/token",
             'appId' : "64f52acc-4a02-40ad-a059-7dcd1d38be68",
             'appKey' : "GjqVItbTHEgW1f8u3zaPUAqP8wDjDHrZpMUq8Mb8ZNo="}

QiServerUrl = "qi-data.osisoft.com:3380"

client = QiClient(QiServerUrl, authItems)

foundEvents = client.getRangeValues("AccelerometerStream2", "2015-09-24T15:53:00-07:00", 0, 10000, False, QiBoundaryType.ExactOrCalculated.value)
#dumpEvents(foundEvents)

timestamps = [x["Timestamp"] for x in foundEvents]

#datetimes = [ datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in timestamps ]
datetimes = [ parser.parse(x) for x in timestamps ]


ax = [x["AccelerationX"] for x in foundEvents]
ay = [x["AccelerationY"] for x in foundEvents]
az = [x["AccelerationZ"] for x in foundEvents]

indices  = [i for i in xrange(len(foundEvents))]

#for i in datetimes:
#    print i

plt.plot(datetimes,ax)
plt.plot(datetimes,ay)
plt.plot(datetimes,az)
plt.ylabel('acceleration')
plt.show()


#2015-09-24T11:40-07:00