# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 18:20:29 2015

@author: mdblr
"""
import sqlite3 as lite
import pandas as pd
con = lite.connect('getting_started.db')
cur = con.cursor()

#this was just a tuple of tuples, but modifying with a SQLite statetment
cities_populate = """INSERT into cities (name, state) VALUES 
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA');"""

#Doing the same as above   
weather_populate = """INSERT into weather (city, year, warm_month, cold_month, average_h) VALUES
            ('New York City', 2013, 'July', 'January', 62),
            ('Boston', 2013, 'July', 'January', 59), 
            ('Chicago', 2013, 'July', 'January', 59), 
            ('Miami', 2013, 'August', 'January', 84), 
            ('Dallas', 2013, 'July','January', 77), 
            ('Seattle', 2013, 'July', 'January', 61), 
            ('Portland', 2013, 'July', 'December', 63), 
            ('San Francisco', 2013, 'September', 'December', 64), 
            ('Los Angeles', 2013, 'September', 'December', 75);"""


#creating tables in database with new values   
cur.execute('drop table if exists cities;')
cur.execute('drop table if exists weather;')
cur.execute('create table cities (name text, state text);')
cur.execute('create table weather (city text, year integer, warm_month text, cold_month text, average_h integer);')

#insert values using python variable containing sqlite command
cur.execute(cities_populate)
cur.execute(weather_populate)

#joining tables together
cities_weather = cur.execute('SELECT name, state, average_h FROM cities LEFT OUTER JOIN weather ON name = city;')

#feeding data into panda dataframe
df_tables = pd.read_sql(cities_weather, con)

#indexing to select the months that are warmest in july
julying = df_tables(df_tables(['average_h' == 'July']))

#printing
print "cities that are warmest in July are:", ', '.join(julying.tolist())
