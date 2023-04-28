# CurrencyConverter-ETL-Project
his project pull the data every day at 1am and 11 pm and save in this format, 
timestamp, which is the datetime in which the record was pulled, currency_from, which is the currency you are converting from (should always be USD), USD_to_currency_rate, which is the rate to 1 NGN cost in USD, currency_to_USD_rate, which is the rate of 1 USD cost in NGN, currency_to is the currency you are converting to from USD, In our case 7 currencies, for Nigeria, Ghana, Kenya, Uganda, Morocco, Côte d'Ivoire and Egypt.
# Installation
 pip install xecd-rates-client#responsible for API integration 
 pip install APScheduler# for sceduling the task
