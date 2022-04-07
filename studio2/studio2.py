#######################################################################
# Program Filename: studio2.py
# Author:  Baird Quinn
# Date: 7 April 2022
# Description: Studio 2 part 2 assignment gas and prices
# Input: Car MPG or MPGe, miles driven in a year, kWh per gallon
# Output: Gallons/kW used, price
#######################################################################

#variables:
mpgSedan = 30
mpgSedanHybrid = 45
mpgSUV = 20
mpgSUVHybrid = 30
mpgeTesla = 126
mpgeBolt = 108
kWhpergallon = 33.7
miles_year = 14032
gasOR = 4.72
gasCA = 5.92
powerCorvallis = 0.1116
powerCharging = .3

#computation
gallons_year = miles_year/mpgeBolt
dollars_yearCorvallis = gallons_year*kWhpergallon*powerCorvallis
dollars_yearCharging = gallons_year*kWhpergallon*powerCharging

#printing
print("This car will use the equivalent of", gallons_year, "gallons per year.")
print("At Corvallis power prices, this will cost $",dollars_yearCorvallis, "per year.")
print("At a charging station, this will cost $",dollars_yearCharging, "per year.")