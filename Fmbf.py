# uncompyle6 version 3.3.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr 24 2019, 10:05:31) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
# Embedded file name: <Ahmad_Riswanto>
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[+] \x1b[1;92mPlease Wait \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
v = '\x1b[32m'
r = '\x1b[91m'
y = '\x1b[93m'
u = '\x1b[36m'
al = v + '           >> \x1b[39mFACEBOOK MULTIBRUTEFORCE \x1b[92m<<             '
pm = '\x1b[91m===================================================='
print y + pm
jalan('\x1b[1;32m             > \x1b[34mSedang Di Perbaiki \x1b[92m<')
jalan('\x1b[1;32m             > \x1b[34mThanks For You \x1b[92m<')
print y + pm
