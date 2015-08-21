#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Copyright (C) 2015 ioerror / iostreams
## https://github.com/iostreams/kursy-walut
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

url='https://www.walutomat.pl/'
waluty = ('EUR', 'USD', 'GBP', 'CHF')
ua='Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)'
#########

import sys, urllib.request
from bs4 import BeautifulSoup

if len(sys.argv) != 2 or sys.argv[1] not in waluty :
    print('Użycie: ' + sys.argv[0] + ' EUR|USD|GBP|CHF', file=sys.stderr)
    sys.exit(11)

currency = sys.argv[1]
exchangeRate = ''

try :
    html = urllib.request.urlopen( urllib.request.Request(url, headers={'User-Agent' : ua}) ).read()
except :
    print('Błąd pobierania kursu ze strony www', file=sys.stderr)
    sys.exit(12)


soup = BeautifulSoup(html)
tab_rates = soup.find(name='div', id='best_curr')

if type(tab_rates).__name__ == 'Tag' :
    for tags in tab_rates:
        if type(tags).__name__ == 'Tag' :
            tag = tags.find(name='span', attrs={ 'class' : 'pair' })
            if type(tag).__name__ == 'Tag' and tag.text.find(currency+' / PLN') != -1 :
                #curr1 - kurs kupna #curr2 kurs sprzedaży
                exchangeRate = tags.find(name='span', attrs={ 'class' : 'curr2' }).text
                break

if (exchangeRate == '') :
    print('Błąd pobierania kursu', file=sys.stderr)
    sys.exit(13)
else :
    print('Kurs', currency, '=', exchangeRate, 'zł')

