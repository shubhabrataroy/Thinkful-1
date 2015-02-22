# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 18:20:29 2015

@author: mdblr
"""
import sqlite3 as lite
import pandas as pd
con = lite.connect('getting_started.db')

cities = (('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA'))
    
weather = (('New York City', 2013, 'July', 'January', 62),
           ('Boston', 2013, 'July', 'January', 59), 
            ('Chicago', 2013, 'July', 'January', 59), 
            ('Miami', 2013, 'August', 'January', 84), 
            ('Dallas', 2013, 'July','January', 77), 
            ('Seattle', 2013, 'July', 'January', 61), 
            ('Portland', 2013, 'July', 'December', 63), 
            ('San Francisco', 2013, 'September', 'December', 64), 
            ('Los Angeles', 2013, 'September', 'December', 75))


with con:
    cur = con.cursor()    
    cur.execute('drop table if exists cities;')
    cur.execute('drop table if exists weather;')
    cur.execute('create table cities (name text, state text);')
    cur.execute('create table weather (city text, year integer, warm_month text, cold_month text, average_h integer);')
    cur.executemany('insert into weather values (?,?,?,?,?)', weather)
    cur.executemany('insert into cities values (?,?)', cities)
    cur.execute('SELECT name, state, average_h FROM cities LEFT OUTER JOIN weather ON name = city;')
    rows = cur.fetchall()
    df = pd.DataFrame(rows)

    
    