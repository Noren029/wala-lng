'''
pasteBinAPI.py - Module to make a pastefile with passed arguments
Keiffer McEwan - 10355836

### Import this module into your main program ### 

This program is strictly my own work. Any material beyond course learning
materials that is taken from the Web or other sources is properly cited,
giving credit to the original author(s).
'''

#to send a post request to the api
import requests
#my pastebin credentials
import credentials

def postNewPaste(title, bodyText, expiration='10M', listed=True):
    
    print("Gathering arguments passed to paste function..")
    url = credentials.PASTEBIN_API_URL
    api_dev_key = credentials.API_DEV_KEY
    api_paste_code = bodyText
    api_paste_name = title

    if listed == True:
        api_paste_private = '0'
    else:
        api_paste_private = '1'

    api_paste_expire_date = expiration  # 10 minutes, 1H, 1D, 1W, 1M, 1Y

    #passes given arguments into a dictionary for pastebin
    print("formating arguments passed into dictionary understood by pastebin...")
    data = {
        'api_dev_key': api_dev_key,
        'api_option': 'paste',
        'api_paste_code': api_paste_code,
        'api_paste_name': api_paste_name,
        'api_paste_private': api_paste_private,
        'api_paste_expire_date': api_paste_expire_date
    }

    print("sending post request")
    #sends the post request to pastebin with passed data
    response = requests.post(url, data=data)

    #if program runs return the url else say there was an error and return code
    if (response.status_code == requests.codes.ok):
        print("Recived data okay returning url..")
        return response.text
    else:
        print("Recived error when communicating with page. Ending script...")
        print("error code: ", response.status_code)
        return 0


if __name__ == "__main__":
    print("please import this as a module to your main code")