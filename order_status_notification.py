import json
import requests

# open env.json
with open('src/env.json', 'r') as json_file:
    global open_env
    open_env = json.load(json_file)
# print(open_env)

def get_auth():
    url = open_env['Url']+"/ccadmin/v1/login"
    data = {"grant_type": "client_credentials"}
    headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": open_env['Authorization']
        }
    # print(headers)
    res = requests.post(url, data=data, headers=headers)
    # print(json.loads(res.text)['access_token'])
    global accessToken
    accessToken = json.loads(res.text)['access_token']
    # print(accessToken)
    get_order()
    
def get_order():
    global orderID
    orderID = input('Insert Order ID: ')

    # print("Access"+accessToken)
    headers_getorder = { 
        "Authorization": "Bearer "+accessToken
    }
    url_order = open_env['Url']+'/ccadmin/v1/orders/'+orderID
    global response_order
    req_order = requests.get(url_order, headers=headers_getorder)
    response_order = json.loads(req_order.text)
    # print(response_order)

    with open('mailsJson/order_'+orderID+'.json', 'w') as json_file:
        json.dump(response_order, json_file, indent=4)

    print('ORDER ID: '+response_order['id'])
    print('ORDER STATUS: '+response_order['state'])
    print('SUBMITTETD DATE: '+response_order['submittedDate'])
    # print('ITEMS QTY: '+len(response_order['commerceItems']))
    print('SHOPPER NAME: '+response_order['profile']['firstName'])
    get_mail_payload()

def get_mail_payload():
    global mailStatus
    mailStatus = input('Notification Type: ')
    global data_mail
    data_mail = {"messageDetails": 
                            {"notificationType": "payment_initiated_order_v1", 
                                "locale": response_order["locale"],
                                "toEmail": response_order["profile"]["email"],
                            },
                            "storefrontUrl": open_env["Storefront"],
                            "orderId": response_order["id"],
                            "shopper": {
                                "firstName": response_order["profile"]["firstName"]   
                            },
                            "total": response_order["priceInfo"]["total"],
                            "orderLocation": mailStatus
                        }


    with open('mailsJson/order_'+orderID+'_'+mailStatus+'.json', 'w') as json_file:
        json.dump(data_mail, json_file, indent=4)

    post_mail()

def post_mail():
    url_mail = open_env['Url']+'/ccadmin/v1/emailNotifications'

    y = json.dumps(data_mail)

    headers_postmail = { 
    "Authorization": "Bearer "+accessToken,
    "Content-Type": "application/json"
	}

    # print(headers_postmail)
    post_mail = requests.post(url_mail, data=y, headers=headers_postmail)

    print(post_mail)

# json data validation
if  not open_env:
    print('Environment is not defined!\nEnter:\n    python3 env.py\nTo set new environment')
else:
    print('Environment OK')
    get_auth()


