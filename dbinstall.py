#!/usr/bin/python
# -*- coding: utf-8
# version 1.000
import dbIceServ as dbd

db = dbd.dbIceServ('mysql','localhost','root','mysql1024')
db._create()
db = dbd.dbIceServ(dbd.DATABASE, "localhost", dbd.MYSQL_USER, dbd.MYSQL_PASSWORD)
#if db.open():
#    db.price_load("site/files/download/price/pos1.spr")
#    db.close()

