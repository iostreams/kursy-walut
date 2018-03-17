#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Copyright (C) 2015-2018 ioerror / iostreams
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

import sys
import urllib.request
import json

url = 'https://panel.walutomat.pl/api/v1/best_offers.php'
currencies = ('EUR', 'USD', 'GBP', 'CHF')
ua = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)'
#########

if len(sys.argv) != 2 or sys.argv[1] not in currencies:
    print('Użycie: ' + sys.argv[0] + ' ' + '|'.join(currencies), file=sys.stderr)
    sys.exit(11)

currency = sys.argv[1]
exchangeRate = ''

try:
    jsonOffers = urllib.request.urlopen(
        urllib.request.Request(url, headers={'User-Agent': ua, 'Origin': 'https://www.walutomat.pl'})).read()
except:
    print('Błąd pobierania kursu ze strony www', file=sys.stderr)
    sys.exit(12)

try:
    jsonOffers = json.loads(jsonOffers)
    for offer in jsonOffers['offers']:
        if offer['pair'] == currency + 'PLN':
            exchangeRate = offer['sell']
            break
except:
    print('Błąd json', file=sys.stderr)
    sys.exit(14)

if exchangeRate == '':
    print('Błąd pobierania kursu', file=sys.stderr)
    sys.exit(13)
else:
    print('Kurs', currency, '=', exchangeRate, 'zł')
