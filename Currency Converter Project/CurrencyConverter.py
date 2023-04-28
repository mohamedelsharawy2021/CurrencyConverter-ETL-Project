#this code is getting currency rate from XE website and load it into a table
from xecd_rates_client import XecdClient #importing the library needed to use XE API
import pandas as pd
import datetime #import date time library to get the time stamp
from apscheduler.schedulers.background import BlockingScheduler #import apscheduler for code schedule

def currencyconverter():
    
    xecd = XecdClient('beinex291881425', 'jep3jd1rmaic38jkjjt2v1a5hk') #connecting to Api , please enter your ID and Key
    xecd.account_info()
    CT = datetime.datetime.now()
    USDToCurrencyRate=xecd.convert_from("NGN", "USD", 1)
    CurrencyToUSDRate = xecd.convert_from("USD", "NGN", 1)
    CurrencyToNigeria = xecd.convert_from("USD", "NGN", 1)
    CurrencyToGhana = xecd.convert_from("USD", "GHS", 1)
    CurrencyToKenya = xecd.convert_from("USD", "KES", 1)
    CurrencyToUghanda = xecd.convert_from("USD", "UGX", 1)
    CurrencyToMoroco = xecd.convert_from("USD", "MAD", 1)
    CurrencyToCotedev = xecd.convert_from("USD", "XOF", 1)
    CurrencyToEGP = xecd.convert_from("USD", "EGP", 1)
    ListOFCurr = ["NGN" ,"GHS" ,"KES","UGX","MAD","XOF","EGP"]
    ListOfRates = [CurrencyToNigeria.get('to')[0].get('mid') ,CurrencyToGhana.get('to')[0].get('mid') ,CurrencyToKenya.get('to')[0].get('mid'),CurrencyToUghanda.get('to')[0].get('mid'),CurrencyToMoroco.get('to')[0].get('mid'),CurrencyToCotedev.get('to')[0].get('mid'),CurrencyToEGP.get('to')[0].get('mid')]
    df = pd.DataFrame({'CurrencyName':ListOFCurr})
    df['currency_to'] = pd.DataFrame({'ChangeRate':ListOfRates})
    df['currency_from'] = 'USD'
    df['timestamp'] = CT
    df['USD_to_currency_rate'] = USDToCurrencyRate.get('to')[0].get('mid')
    df['currency_to_USD_rate'] = CurrencyToUSDRate.get('to')[0].get('mid')
    print (df)

scheduler = BlockingScheduler()#intialize the sceduler
scheduler.add_job(currencyconverter, 'cron', hour='1-23', minute= '0')#scedule the code to run at 1am and 11 pm
scheduler.start()
scheduler.shutdown
scheduler.remove_all_jobs