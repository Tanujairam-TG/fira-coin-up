import os
import requests
import base64
import json
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from NamasteAes import NamasteAes
import threading

# Constants
PASSWORD_URL = 'https://pastebin.com/raw/cGFrRgCV'
KEY = bytes.fromhex('83108793d2e582de26095e6365006b683549db8300bac461d36fb6e4c27f2dbd')
IV = bytes.fromhex('51afa8b2e0a47a37881424fb9b88b8bc')
ID = '55651283589'
TOKEN = '5de3db1526d972d25e666bdac92865e8'
SID = '55651283589%3A4Dwt7ZFkkj2vI1%3A12%3AAYfnh_iv8VsJxDGiKO0h4FmyBgSq1fgl-hvWs2RPRQ'

SESSION_STR = f'{{"ds_user_id":"{ID}","sessionid":"{SID}"}}'
SESSION_BYTES = SESSION_STR.encode('utf-8')
ENC_BYTES = base64.b64encode(SESSION_BYTES)
SES = ENC_BYTES.decode('utf-8')

#def fetch_password():
#  try:
#        response = requests.get(PASSWORD_URL)
#        response.raise_for_status()  # Ensure we notice bad responses
#        return response.text.strip()
#    except requests.RequestException as e:
#        print(f"Error fetching password: {e}")
#        exit()

def Coinlike(target_id, user_pk):
    url_coin = "https://firafollower.xyz/api/v4/coin.php"
    data_coin = {
        "requested_with": "org.fasaroid.fira",
        "version_code": "120",
        "market_name": "zarinpal",
        "language_code": "ar",
        "device_info": "29/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N",
        "user_token": str(TOKEN),
        "user_pk": str(ID),
        "control": {
            "csrf": "",
            "shbid": "15397,257048640,1747383932:01f7e6f21c56a952f4d101d4381e012903da3c95e0eaefba4f31a3934a2e02cd7540d63d",
            "shbts": "1715847932,257048640,1747383932:01f7fc07edf1a64bd80aa438160b2029571224dd6f7a8eb2ec8502cd55ab75b3b57fe2cf",
            "mid": "ZkXC1wABAAGsgtsHABtlMrZ5qJuF",
            "rur": "CLN,257048640,1747523824:01f73f624cc5c2383348971cf6d70e19c381fdb0612f5e9c5f7809bb8802960ab57bc0dc",
            "auth": f"Bearer IGT:2:{SES}",
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
        "action": "like"
    }
    data_json_coin = json.dumps(data_coin).encode()
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
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
    data_decrypted_coin_response = NamasteAes.dec_cbc(data_encrypted_coin_response, KEY.hex(), IV.hex())
    print(data_decrypted_coin_response)

def HFOL():
    while True:
        url_orders = "https://firafollower.xyz/api/v4/orders.php"
        data = {
            "requested_with": "org.fasaroid.fira",
            "version_code": "120",
            "market_name": "zarinpal",
            "language_code": "ar",
            "device_info": "29/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N",
            "user_token": str(TOKEN),
            "user_pk": str(ID),
            "action": "like"
        }
        bayt = json.dumps(data).encode()
        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        ciph = cipher.encrypt(pad(bayt, AES.block_size))
        enc = base64.b64encode(ciph).decode('utf-8')
        payload_orders = f"{enc}"
        headers_orders = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",
            'Accept-Encoding': "*",
            'Content-Type': "application/xml",
            'x-access': "FiraFollower",
            'x-version': "2"
        }

        response_orders = requests.post(url_orders, data=payload_orders, headers=headers_orders)
        data_encrypted_orders = response_orders.text
        data_decrypted_orders = NamasteAes.dec_cbc(data_encrypted_orders, KEY.hex(), IV.hex())
        json_data_orders = json.loads(data_decrypted_orders)
        if 'data' in json_data_orders and len(json_data_orders['data']) > 1:
            target_id = json_data_orders['data'][1]['id']
            user_pk = json_data_orders['data'][1]['user_pk']
            Coinlike(target_id, user_pk)
        else:
            print("No more Request")
        time.sleep(3)  # Sleep to avoid hitting API limits

def CoinComment(target_id, user_pk):
    url_coin = "https://firafollower.xyz/api/v4/coin.php"
    data_coin = {
        "requested_with": "org.fasaroid.fira",
        "version_code": "120",
        "market_name": "zarinpal",
        "language_code": "ar",
        "device_info": "29/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N",
        "user_token": str(TOKEN),
        "user_pk": str(ID),
        "control": {
            "csrf": "",
            "shbid": "15397,257048640,1747383932:01f7e6f21c56a952f4d101d4381e012903da3c95e0eaefba4f31a3934a2e02cd7540d63d",
            "shbts": "1715847932,257048640,1747383932:01f7fc07edf1a64bd80aa438160b2029571224dd6f7a8eb2ec8502cd55ab75b3b57fe2cf",
            "mid": "ZkXC1wABAAGsgtsHABtlMrZ5qJuF",
            "rur": "CLN,257048640,1747523824:01f73f624cc5c2383348971cf6d70e19c381fdb0612f5e9c5f7809bb8802960ab57bc0dc",
            "auth": f"Bearer IGT:2:{SES}",
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
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
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
    data_decrypted_coin_response = NamasteAes.dec_cbc(data_encrypted_coin_response, KEY.hex(), IV.hex())
    print(data_decrypted_coin_response)

def HHCOMMENT():
    while True:
        url_orders = "https://firafollower.xyz/api/v4/orders.php"
        data = {
            "requested_with": "org.fasaroid.fira",
            "version_code": "120",
            "market_name": "zarinpal",
            "language_code": "ar",
            "device_info": "29/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N",
            "user_token": str(TOKEN),
            "user_pk": str(ID),
            "action": "comment"
        }
        bayt = json.dumps(data).encode()
        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        ciph = cipher.encrypt(pad(bayt, AES.block_size))
        enc = base64.b64encode(ciph).decode('utf-8')
        payload_orders = f"{enc}"
        headers_orders = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",
            'Accept-Encoding': "*",
            'Content-Type': "application/xml",
            'x-access': "FiraFollower",
            'x-version': "2"
        }

        response_orders = requests.post(url_orders, data=payload_orders, headers=headers_orders)
        data_encrypted_orders = response_orders.text
        data_decrypted_orders = NamasteAes.dec_cbc(data_encrypted_orders, KEY.hex(), IV.hex())
        json_data_orders = json.loads(data_decrypted_orders)
        if 'data' in json_data_orders and len(json_data_orders['data']) > 1:
            target_id = json_data_orders['data'][1]['id']
            user_pk = json_data_orders['data'][1]['user_pk']
            CoinComment(target_id, user_pk)
        else:
            print("No more Request")
        time.sleep(3)  # Sleep to avoid hitting API limits

def main():
    # Start the processes in separate threads
    threading.Thread(target=HFOL).start()
    threading.Thread(target=HHCOMMENT).start()

if __name__ == "__main__":
    main()
