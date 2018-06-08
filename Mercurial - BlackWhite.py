#!/usr/bin/python
#.------..------..------..------..------.
#|S.--. ||L.--. ||3.--. ||4.--. ||K.--. |
#| :/\: || :/\: || :(): || :/\: || :/\: |
#| :\/: || (__) || ()() || :\/: || :\/: |
#| '--'S|| '--'L|| '--'3|| '--'4|| '--'K|
#`------'`------'`------'`------'`------'
#https://twitter.com/SL34K
#https://github.com/SL34K
import requests,datetime,time,names,random,string,imaplib,re
from datetime import datetime
from random import choice,randint
from bs4 import BeautifulSoup  as bs
from termcolor import cprint, colored
from colorama import init 
init(convert=True)
def __timestamp():
	timestamp = str("["+datetime.now().strftime("%H:%M:%S.%f")[:-3]+"]")
	return timestamp
def log(text):
	print("{} {}".format(__timestamp(), text))
	return
def success(text):
	print("{} {}".format(__timestamp(), colored(text, "green")))
	return
def warn(text):
	print("{} {}".format(__timestamp(), colored(text, "yellow")))
	return
def error(text):
	print("{} {}".format(__timestamp(), colored(text, "red")))
	return
def status(text):
	print("{} {}".format(__timestamp(), colored(text, "magenta")))
	return
def proxysession(proxy):
    ip,port,username,password = proxy.split(":")
    formattedProxy = (username+':'+password+'@'+ip+':'+port)
    proxies = {'http': 'http://'+formattedProxy,
    'https': 'https://'+formattedProxy}
    sesh = requests.Session()
    sesh.proxies = proxies
    sesh.headers = {
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Origin':'https://www.supplystore.com.au',
        'Referer':'https://www.supplystore.com.au/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    sesh.headers.update()
    return sesh
def session():
    sesh = requests.session()
    sesh.headers = {
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Origin':'https://www.supplystore.com.au',
        'Referer':'https://www.supplystore.com.au/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    sesh.headers.update()
    return sesh
def getnum():
    num = str(randint(0,9))
    return num
def getphone():
    pnum = (str(0)+getnum()+getnum()+getnum()+getnum()+getnum()+getnum()+getnum()+getnum()+getnum())
    return pnum
sizes = ['11548317','11548318','11548319','11548320','11548321','11548322','11548323','11548324','11548325','11548326','11548327']
def getlinkk(email,login, password):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(login, password)
    y = 0
    while y == 0:
        try:
            mail.list()
            mail.select("inbox") # connect to inbox.
            result, data = mail.search(None, '(TO "{}")'.format(email))
            ids = data[0] # data is a list.
            id_list = ids.split() # ids is a space separated string
            latest_email_id = id_list[-1] # get the latest
            result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
            raw_email = data[0][1]
            urls = re.findall(r'r-c-(.*)', str(raw_email))
            urls = urls[0].split('=')[0]
            try:
                end = urls
                link = 'http://flipsidedistribution.cmail20.com/t/r-c-'+end
                #print(link)
                return(link)
                y = 1
            except:
                print("Error getting link")
        except:
            log("Waiting for link")
            time.sleep(10)
def signup(domain,address1,city,state,country,postcode,delay,login, password):
    first = names.get_first_name()
    last = names.get_last_name()
    randomletters = "".join(choice(string.ascii_letters) for x in range(randint(1, 4)))
    username = randomletters+first+randomletters
    email = username+'@'+domain
    sesh = session()
    getlink = sesh.get('https://www.supplystore.com.au/raffles-nike-zoom-fly-mercurial-fkow-blackwhite-volt.aspx')
    soup = bs(getlink.text,'lxml')
    code = soup.find('form', {'id': 'raffleForm'}).get('data-id')
    data={'email':email,'data':code}
    getsub = 'https://createsend.com//t/getsecuresubscribelink'
    test = sesh.post(getsub,data=data)
    size = choice(sizes)
    url = test.text
    phone = getphone()
    data = {
        'cm-f-dykuiyii': first,
        'cm-f-dykuiyid': last,
        'cm-uulklly-uulklly': email,
        'cm-f-dykuiyih': phone,
        'cm-fo-dykuiydh': size,
        'cm-f-dykuiyik': address1,
        'cm-f-dykuiyiu': city,
        'cm-f-dykuiydl': state,
        'cm-f-dykuiydr': country,
        'cm-f-dykuiydy': postcode,
        'cm-privacy-consent': 'on',
        'cm-privacy-consent-hidden': 'true',
        'cm-privacy-email': 'on',
        'cm-privacy-email-hidden': 'true',
        'terms': 'Yes',
        'cm-f-dykuiydj': 'Yes',
        'terms': 'Yes',
        'g-recaptcha-response': '',
    }
    submit = sesh.post(url,data=data)
    if submit.status_code == 200:
        status("Entry submitted - waiting for email")
        try:
            verify = getlinkk(email,login, password)
            sesh.get(verify)
            success('Entered and confirmed: '+email)
        except:
            error("Unable to verify")
    else:
        error("Error entering")
def main():
    status("@SL34k's Supply Store Raffle Bot")
    success("Captcha bypass - Working As Of 06/18")
    log("Raffle: NIKE ZOOM FLY MERCURIAL FK/OW - BLACK/WHITE-VOLT")
    login = input("{} {}".format(__timestamp(), 'Enter the gmail email for your catchall i.e. ukcarts@gmail.com: '))
    password = input("{} {}".format(__timestamp(), 'Enter the gmail password for your catchall: '))
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(login, password)
        domain = input("{} {}".format(__timestamp(), 'Enter your catchall domain i.e. ukcarts.co.uk: '))
        address1 = input("{} {}".format(__timestamp(), 'Enter your address line 1: '))
        city = input("{} {}".format(__timestamp(), 'Enter your city: '))
        state = input("{} {}".format(__timestamp(), 'Enter your state/county: '))
        country = input("{} {}".format(__timestamp(), 'Enter your Country i.e. United Kingdom: '))
        postcode = input("{} {}".format(__timestamp(), 'Enter your postcode: '))
        delay = input("{} {}".format(__timestamp(), 'Please enter the signup delay (in seconds): '))
        try:
            delay = int(delay)
            try:
                entries = input("{} {}".format(__timestamp(), 'Please enter the number of times to enter: '))
                entries = int(entries)
                x = 0
                try:
                    status("Entering for Sizes US7-14")
                    while x < entries:
                        try:
                            signup(domain,address1,city,state,country,postcode,delay,login, password)
                            x = x+1
                            time.sleep(delay)
                        except Exception as e: 
                            print (e)
                    success("Completed all entries")
                except:
                    print("Error")
            except:
                error("You didn't enter how many times you wanted to enter correctly")
        except:
            error('Delay was not a number')
    except:
        print("Errow with gmail details - makesure access for less secure apps is enabled...")
sesh = session()
def sizechoice():
    pull = sesh.get('https://www.supplystore.com.au/raffles-nike-zoom-fly-mercurial-fkow-blackwhite-volt.aspx')
    soup = bs(pull.text,'lxml')
    code = soup.find_all('option')
    for i in code:
        size = i.text
        value = i.get('value')
        print(str(value))
main()