import json

# open env.json
with open('src/env.json', 'r') as json_file:
    open_env = json.load(json_file)


# define functions
def listEnv():
    open_env_user = open_env['UserName']
    open_env_env = open_env['Url']
    open_env_storefront = open_env['Storefront']
    print('User Name: '+open_env_user+'\nEnvironment: '+open_env_env+' \nStorefront: '+open_env_storefront)

    change_data = input("Change Environment (y / n): ")
    if change_data == "y" or change_data == "yes":
        addNewEnv()
    else:
        exit

def addNewEnv():
    user_name = input('User Name: ')
    user_email = input('Email: ')
    ambient = input('Environment: ')
    api_key = input('API Key: ')
    storefront = input('Storefront / Sitename: ')

    env = {
        "Url": ambient,
        "Authorization": "Bearer "+api_key,
        "Storefront": storefront,
        "user_name": user_name,
        "user_email": user_email
    }
    with open("src/env.json", "w") as json_file:
        json.dump(env, json_file, indent=4)

# json data validation
if  not open_env:
    print('Environment is not defined! Create New? (y / n)')
    addNewEnv()
else:
    listEnv()





