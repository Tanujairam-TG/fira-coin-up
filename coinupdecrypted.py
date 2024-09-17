import os


os.system("pip install requests pycrypto pycryptodomex pycryptodome NamasteAes webbrowser")


os.system("clear")


import requests

import webbrowser


from Crypto.Cipher import AES


from Crypto.Util.Padding import pad, unpad


import base64


import json


from NamasteAes import NamasteAes


import threading





# Constants


PASSWORD_URL = 'https://pastebin.com/raw/q6e6cKcX'


KEY = bytes.fromhex('83108793d2e582de26095e6365006b683549db8300bac461d36fb6e4c27f2dbd')


IV = bytes.fromhex('51afa8b2e0a47a37881424fb9b88b8bc')





def fetch_password():


    try:


        response = requests.get(PASSWORD_URL)


        response.raise_for_status()  # Ensure we notice bad responses


        return response.text.strip()


    except requests.RequestException as e:


        print(f"Error fetching password: {e}")


        exit()





def check_password():


    stored_password = fetch_password()
    print("Password download link: https://f.technicalatg.in/dJOYrBxblb")






    input_password = input("Enter Password: ")


    if input_password != stored_password:


        print("Incorrect password. Exiting.")


        exit()


    print("Password correct. Proceeding...")





check_password()  # Ensure this is called before any sensitive operations


os.system("clear")


id = input("Enter Your ID_Fira : ")


token = input("ENTER Your Token_Fira :")


sid = input("ENTER YOUR SESSION_ID: ")


session_str = f'{{"ds_user_id":"{id}","sessionid":"{sid}"}}'


session_bytes = session_str.encode('utf-8')


enc_bytes = base64.b64encode(session_bytes)


enc_str = enc_bytes.decode('utf-8')


ses = enc_str





key = bytes.fromhex('83108793d2e582de26095e6365006b683549db8300bac461d36fb6e4c27f2dbd')


iv = bytes.fromhex('51afa8b2e0a47a37881424fb9b88b8bc')





def Coinlike(target_id, user_pk):


    url_coin = "https://firafollower.xyz/api/v4/coin.php"


    data_coin = {"requested_with":"org.fasaroid.fira","version_code":"120","market_name":"zarinpal","language_code":"ar","device_info":"29\/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N","user_token":str(token),"user_pk":str(id),"control":{"csrf":"","shbid":"15397,257048640,1747383932:01f7e6f21c56a952f4d101d4381e012903da3c95e0eaefba4f31a3934a2e02cd7540d63d","shbts":"1715847932,257048640,1747383932:01f7fc07edf1a64bd80aa438160b2029571224dd6f7a8eb2ec8502cd55ab75b3b57fe2cf","mid":"ZkXC1wABAAGsgtsHABtlMrZ5qJuF","rur":"CLN,257048640,1747523824:01f73f624cc5c2383348971cf6d70e19c381fdb0612f5e9c5f7809bb8802960ab57bc0dc","auth":f"Bearer IGT:2:{ses}","claim":"hmac.AR1WoaCh3Y3RfhES8hblKWni9RFpizjJ0LefiiDIVGmhBZ1N","drh":"","user_agent":"Instagram 178.1.0.37.123 Android (28\/9; 280dpi; 720x1423; samsung; SM-A205FN; a20; exynos7885; ru_RU; 277249249)","uuids":["android-e47187f911867ae7","f6f64d77-e04a-4471-a8a5-eac80cc4162f","9d3ed3cb-2b33-48ff-be12-61bdcad921bb","c3b1c133-4aab-4aac-b943-0785c72bb988","e7b2c672-5d46-45e5-8e05-83391ba570b0"]},"order_id":str(target_id),"pk":str(user_pk),"action":"like"}





    data_json_coin = json.dumps(data_coin).encode()


    cipher = AES.new(key, AES.MODE_CBC, iv)


    data_encrypted_coin = cipher.encrypt(pad(data_json_coin, AES.block_size))


    payload_coin = base64.b64encode(data_encrypted_coin).decode('utf-8')





    headers_coin = {


        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",


        'Accept-Encoding': "*",


        'Content-Type': "application/xml",


        'x-access': "FiraFollower",


        'x-version': "2"


    }





    response_coin = requests.post(url_coin, data=payload_coin, headers=headers_coin)


    data_encrypted_coin_response = response_coin.text





    data_decrypted_coin_response = NamasteAes.dec_cbc(data_encrypted_coin_response, key.hex(), iv.hex())


    print(data_decrypted_coin_response)





def HHLIKE():


    while True:


        url_orders = "https://firafollower.xyz/api/v4/orders.php"


        data = {"requested_with":"org.fasaroid.fira","version_code":"120","market_name":"zarinpal","language_code":"ar","device_info":"29\/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N","user_token":str(token),"user_pk":str(id),"action":"like"}


        bayt = json.dumps(data).encode()


        cipher = AES.new(key, AES.MODE_CBC, iv)


        ciph = cipher.encrypt(pad(bayt, AES.block_size))


        enc = base64.b64encode(ciph).decode('utf-8')


        da = (enc)


        payload_orders = f"{da}"


        headers_orders = {


            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",


            'Accept-Encoding': "*",


            'Content-Type': "application/xml",


            'x-access': "FiraFollower",


            'x-version': "2"


        }





        response_orders = requests.post(url_orders, data=payload_orders, headers=headers_orders)


        data_encrypted_orders = response_orders.text





        data_decrypted_orders = NamasteAes.dec_cbc(data_encrypted_orders, key.hex(), iv.hex())





        json_data_orders = json.loads(data_decrypted_orders)





        if 'data' in json_data_orders and len(json_data_orders['data']) > 1:


            target_id = json_data_orders['data'][1]['id']


            user_pk = json_data_orders['data'][1]['user_pk']


            Coinlike(target_id, user_pk)


        else:


            print("No more Request")


            





def CoinComment(target_id, user_pk):


    url_coin = "https://firafollower.xyz/api/v4/coin.php"


    data_coin = {


    "requested_with": "org.fasaroid.fira",


    "version_code": "120",


    "market_name": "zarinpal",


    "language_code": "ar",


    "device_info": "29/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N",


    "user_token": str(token),


    "user_pk": str(id),


    "control": {


        "csrf": "",


        "shbid": "15397,257048640,1747383932:01f7e6f21c56a952f4d101d4381e012903da3c95e0eaefba4f31a3934a2e02cd7540d63d",


        "shbts": "1715847932,257048640,1747383932:01f7fc07edf1a64bd80aa438160b2029571224dd6f7a8eb2ec8502cd55ab75b3b57fe2cf",


        "mid": "ZkXC1wABAAGsgtsHABtlMrZ5qJuF",


        "rur": "CLN,257048640,1747557786:01f7dc11c3751dc802e4388247eb1e2b524c662f870a2cc2a9f53e2149d2f0aedcd8e14c",


        "auth": f"Bearer IGT:2:{ses}",


        "claim": "hmac.AR1WoaCh3Y3RfhES8hblKWni9RFpizjJ0LefiiDIVGmhBZ1N",


        "drh": "",


        "user_agent": "Instagram 178.1.0.37.123 Android (28/9; 280dpi; 720x1423; samsung; SM-A205FN; a20; exynos7885; ru_RU; 277249249)",


        "uuids": [


            "android-e47187f911867ae7",


            "f6f64d77-e04a-4471-a8a5-eac80cc4162f",


            "9d3ed3cb-2b33-48ff-be12-61bdcad921bb",


            "c3b1c133-4aab-4aac-b943-0785c72bb988",


            "e7b2c672-5d46-45e5-8e05-83391ba570b0"


        ]


    },


    "order_id": str(target_id),


    "pk": str(user_pk),


    "action": "comment"


}


    data_json_coin = json.dumps(data_coin).encode()


    cipher = AES.new(key, AES.MODE_CBC, iv)


    data_encrypted_coin = cipher.encrypt(pad(data_json_coin, AES.block_size))


    payload_coin = base64.b64encode(data_encrypted_coin).decode('utf-8')





    headers_coin = {


        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",


        'Accept-Encoding': "*",


        'Content-Type': "application/xml",


        'x-access': "FiraFollower",


        'x-version': "2"


    }





    response_coin = requests.post(url_coin, data=payload_coin, headers=headers_coin)


    data_encrypted_coin_response = response_coin.text





    data_decrypted_coin_response = NamasteAes.dec_cbc(data_encrypted_coin_response, key.hex(), iv.hex())


    print(data_decrypted_coin_response)





def HHCOM():


    while True:


        url_orders = "https://firafollower.xyz/api/v4/orders.php"


        data = {"requested_with":"org.fasaroid.fira","version_code":"120","market_name":"zarinpal","language_code":"ar","device_info":"29\/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N","user_token":str(token),"user_pk":str(id),"action":"comment"}


        bayt = json.dumps(data).encode()


        cipher = AES.new(key, AES.MODE_CBC, iv)


        ciph = cipher.encrypt(pad(bayt, AES.block_size))


        enc = base64.b64encode(ciph).decode('utf-8')


        da = (enc)


        payload_orders = f"{da}"


        headers_orders = {


            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",


            'Accept-Encoding': "*",


            'Content-Type': "application/xml",


            'x-access': "FiraFollower",


            'x-version': "2"


        }





        response_orders = requests.post(url_orders, data=payload_orders, headers=headers_orders)


        data_encrypted_orders = response_orders.text





        data_decrypted_orders = NamasteAes.dec_cbc(data_encrypted_orders, key.hex(), iv.hex())





        json_data_orders = json.loads(data_decrypted_orders)





        if 'data' in json_data_orders and len(json_data_orders['data']) > 1:


            target_id = json_data_orders['data'][1]['id']


            user_pk = json_data_orders['data'][1]['user_pk']


            CoinComment(target_id, user_pk)


        else:


            print("No more Request")


            





def CoinFollow(target_id, user_pk):


    url_coin = "https://firafollower.xyz/api/v4/coin.php"


    data_coin = {


        "requested_with": "org.fasaroid.fira",


        "version_code": "120",


        "market_name": "zarinpal",


        "language_code": "ar",


        "device_info": "29/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N",


        "user_token": str(token),


        "user_pk": str(id),


        "control": {


            "csrf": "",


            "shbid": "15397,257048640,1747383932:01f7e6f21c56a952f4d101d4381e012903da3c95e0eaefba4f31a3934a2e02cd7540d63d",


            "shbts": "1715847932,257048640,1747383932:01f7fc07edf1a64bd80aa438160b2029571224dd6f7a8eb2ec8502cd55ab75b3b57fe2cf",


            "mid": "ZkXC1wABAAGsgtsHABtlMrZ5qJuF",


            "rur": "CLN,257048640,1747521207:01f7070685c28c922472413ef010d85ae3cf7258ed98bbb718eceaeb22538ca817bc22d7",


            "auth": f"Bearer IGT:2:{ses}",


            "claim": "hmac.AR1WoaCh3Y3RfhES8hblKWni9RFpizjJ0LefiiDIVGmhBZ1N",


            "drh": "",


            "user_agent": "Instagram 178.1.0.37.123 Android (28/9; 280dpi; 720x1423; samsung; SM-A205FN; a20; exynos7885; ru_RU; 277249249)",


            "uuids": [


                "android-e47187f911867ae7",


                "f6f64d77-e04a-4471-a8a5-eac80cc4162f",


                "9d3ed3cb-2b33-48ff-be12-61bdcad921bb",


                "c3b1c133-4aab-4aac-b943-0785c72bb988",


                "e7b2c672-5d46-45e5-8e05-83391ba570b0"


            ]


        },


        "order_id": str(target_id),


        "pk": str(user_pk),


        "action": "follow"


    }





    data_json_coin = json.dumps(data_coin).encode()


    cipher = AES.new(key, AES.MODE_CBC, iv)


    data_encrypted_coin = cipher.encrypt(pad(data_json_coin, AES.block_size))


    payload_coin = base64.b64encode(data_encrypted_coin).decode('utf-8')





    headers_coin = {


        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",


        'Accept-Encoding': "*",


        'Content-Type': "application/xml",


        'x-access': "FiraFollower",


        'x-version': "2"


    }





    response_coin = requests.post(url_coin, data=payload_coin, headers=headers_coin)


    data_encrypted_coin_response = response_coin.text





    data_decrypted_coin_response = NamasteAes.dec_cbc(data_encrypted_coin_response, key.hex(), iv.hex())


    print(data_decrypted_coin_response)





def HHFOL():


    while True:


        url_orders = "https://firafollower.xyz/api/v4/orders.php"


        data = {"requested_with":"org.fasaroid.fira","version_code":"120","market_name":"zarinpal","language_code":"ar","device_info":"29\/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N","user_token":str(token),"user_pk":str(id),"action":"follow"}


        bayt = json.dumps(data).encode()


        cipher = AES.new(key, AES.MODE_CBC, iv)


        ciph = cipher.encrypt(pad(bayt, AES.block_size))


        enc = base64.b64encode(ciph).decode('utf-8')


        da = (enc)


        payload_orders = f"{da}"


        headers_orders = {


            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",


            'Accept-Encoding': "*",


            'Content-Type': "application/xml",


            'x-access': "FiraFollower",


            'x-version': "2"


        }





        response_orders = requests.post(url_orders, data=payload_orders, headers=headers_orders)


        data_encrypted_orders = response_orders.text





        data_decrypted_orders = NamasteAes.dec_cbc(data_encrypted_orders, key.hex(), iv.hex())





        json_data_orders = json.loads(data_decrypted_orders)





        if 'data' in json_data_orders and len(json_data_orders['data']) > 3:


            target_id = json_data_orders['data'][3]['id']


            user_pk = json_data_orders['data'][3]['user_pk']


            CoinFollow(target_id, user_pk)


        else:


            print("No more Requests")


            


def link_Hacktive_Mahos():


    threading.Thread(target=HHLIKE).start()


    threading.Thread(target=HHCOM).start()


    threading.Thread(target=HHFOL).start()


webbrowser.open("https://t.me/hacktive_mind")


def linked():


    sg = input(


        f'''

═════════════════════════════════════════
[1] Unlimited Coin Up: 

[2] more need :
═════════════════════════════════════════





[⌯] ChooSe Number » ''')





    if sg == '1':


    	 link_Hacktive_Mahos()   


    elif sg == '2':


          telegram()



def telegram():
	webbrowser.open("https://t.me/hacktive_mind")

def MainMahos():


    


    data = "Hacktive"





    key = '83108793d2e582de26095e6365006b683549db8300bac461d36fb6e4c27f2dbd'


    iv = '51afa8b2e0a47a37881424fb9b88b8bc'


    stat = NamasteAes.dec_cbc(data, key, iv)


    results = json.loads(stat)





    auth_token = results['control']['auth']


    encoded_part = auth_token.split('Bearer IGT:2:')[1]


    decoded_auth = base64.b64decode(encoded_part).decode('utf-8')


    decoded_auth_json = json.loads(decoded_auth)

    session_id = decoded_auth_json.get('sessionid', 'N/A')
    user_token = results.get('user_token', 'N/A')
    user_pk = results.get('user_pk', 'N/A')
    print(f"sessionid: {session_id}")
    print(f"user_token: {user_token}")
    print(f"user_pk: {user_pk}")
linked()
