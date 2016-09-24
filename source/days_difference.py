#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date

days_difference_ico = """
#########################################################
#          PYTHON DAYS DIFFERENCE - GH0ST S0FTWARE      #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#           GMAIL : pentestdatabase@gmail.com           #
# Linkedin : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
######################################################### 
"""

star = "#########################################################"

print days_difference_ico

## First
first_year = input("İlk yılı giriniz : ")
first_month = input("İlk ayı giriniz : ")
first_day = input("İlk günü giriniz : ")

print star

## Second
second_year = input("Son yılı giriniz :")
second_month = input("Son ayı giriniz : ")
second_day = input("Son günü giriniz : ")

## The difference calculation
first_date = date(first_year, first_month, first_day)
second_date =  date(second_year, second_month, second_day)
day = first_date - second_date

print star

## Result
print "Gün Farkı : " + day.days

print star
