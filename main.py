import os
import requests
import webbrowser
import base64
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import threading
from NamasteAes import NamasteAes
from config import SESSION_ID, USER_TOKEN, USER_PK
# Constants
KEY = bytes.fromhex('83108793d2e582de26095e6365006b683549db8300bac461d36fb6e4c27f2dbd')
IV = bytes.fromhex('51afa8b2e0a47a37881424fb9b88b8bc')

# User credentials (for demonstration purposes; in practice, keep sensitive data secure)
id = USER_PK
token = USER_TOKEN
sid = SESSION_ID

session_str = f'{{"ds_user_id":"{id}","sessionid":"{sid}"}}'
session_bytes = session_str.encode('utf-8')
enc_bytes = base64.b64encode(session_bytes)
enc_str = enc_bytes.decode('utf-8')
ses = enc_str

def encrypt_data(data):
    """Encrypt data using AES encryption."""
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_data(encrypted_data):
    """Decrypt data using AES decryption."""
    encrypted_data_bytes = base64.b64decode(encrypted_data)
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    decrypted_data = unpad(cipher.decrypt(encrypted_data_bytes), AES.block_size)
    return decrypted_data.decode('utf-8')

def Coinlike(target_id, user_pk):
    url = "https://firafollower.xyz/api/v4/coin.php"
    data = {
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
            "rur": "CLN,257048640,1747523824:01f73f624cc5c2383348971cf6d70e19c381fdb0612f5e9c5f7809bb8802960ab57bc0dc",
            "auth": f"Bearer IGT:2:{ses}",
            "claim": "hmac.AR1WoaCh3Y3RfhES8hblKWni9RFpizjJ0LefiiDIVGmhBZ1N",
            "drh": "",
            "user_agent": "Instagram 178.1.0.37.123 Android (28/9; 280dpi; 720x1423; samsung; SM-A205FN; a20; exynos7885; ru_RU; 277249249)",
            "uuids": ["android-e47187f911867ae7", "f6f64d77-e04a-4471-a8a5-eac80cc4162f", "9d3ed3cb-2b33-48ff-be12-61bdcad921bb", "c3b1c133-4aab-4aac-b943-0785c72bb988", "e7b2c672-5d46-45e5-8e05-83391ba570b0"]
        },
        "order_id": str(target_id),
        "pk": str(user_pk),
        "action": "like"
    }
    payload = encrypt_data(json.dumps(data).encode())
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",
        'Accept-Encoding': "*",
        'Content-Type': "application/xml",
        'x-access': "FiraFollower",
        'x-version': "2"
    }
    response = requests.post(url, data=payload, headers=headers)
    decrypted_response = decrypt_data(response.text)
    print(decrypted_response)

def HHLIKE():
    while True:
        url = "https://firafollower.xyz/api/v4/orders.php"
        data = {
            "requested_with": "org.fasaroid.fira",
            "version_code": "120",
            "market_name": "zarinpal",
            "language_code": "ar",
            "device_info": "29/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N",
            "user_token": str(token),
            "user_pk": str(id),
            "action": "like"
        }
        payload = encrypt_data(json.dumps(data).encode())
        headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",
            'Accept-Encoding': "*",
            'Content-Type': "application/xml",
            'x-access': "FiraFollower",
            'x-version': "2"
        }
        response = requests.post(url, data=payload, headers=headers)
        decrypted_response = decrypt_data(response.text)
        json_data = json.loads(decrypted_response)
        if 'data' in json_data and len(json_data['data']) > 1:
            target_id = json_data['data'][1]['id']
            user_pk = json_data['data'][1]['user_pk']
            Coinlike(target_id, user_pk)
        else:
            print("No more Requests")

def CoinComment(target_id, user_pk):
    url = "https://firafollower.xyz/api/v4/coin.php"
    data = {
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
            "uuids": ["android-e47187f911867ae7", "f6f64d77-e04a-4471-a8a5-eac80cc4162f", "9d3ed3cb-2b33-48ff-be12-61bdcad921bb", "c3b1c133-4aab-4aac-b943-0785c72bb988", "e7b2c672-5d46-45e5-8e05-83391ba570b0"]
        },
        "order_id": str(target_id),
        "pk": str(user_pk),
        "action": "comment",
        "comment": "Nice!"
    }
    payload = encrypt_data(json.dumps(data).encode())
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",
        'Accept-Encoding': "*",
        'Content-Type': "application/xml",
        'x-access': "FiraFollower",
        'x-version': "2"
    }
    response = requests.post(url, data=payload, headers=headers)
    decrypted_response = decrypt_data(response.text)
    print(decrypted_response)

def HHCOM():
    while True:
        url = "https://firafollower.xyz/api/v4/orders.php"
        data = {
            "requested_with": "org.fasaroid.fira",
            "version_code": "120",
            "market_name": "zarinpal",
            "language_code": "ar",
            "device_info": "29/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N",
            "user_token": str(token),
            "user_pk": str(id),
            "action": "comment"
        }
        payload = encrypt_data(json.dumps(data).encode())
        headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",
            'Accept-Encoding': "*",
            'Content-Type': "application/xml",
            'x-access': "FiraFollower",
            'x-version': "2"
        }
        response = requests.post(url, data=payload, headers=headers)
        decrypted_response = decrypt_data(response.text)
        json_data = json.loads(decrypted_response)
        if 'data' in json_data and len(json_data['data']) > 1:
            target_id = json_data['data'][1]['id']
            user_pk = json_data['data'][1]['user_pk']
            CoinComment(target_id, user_pk)
        else:
            print("No more Requests")

def CoinFollow(target_id, user_pk):
    url = "https://firafollower.xyz/api/v4/coin.php"
    data = {
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
            "rur": "CLN,257048640,1747523824:01f73f624cc5c2383348971cf6d70e19c381fdb0612f5e9c5f7809bb8802960ab57bc0dc",
            "auth": f"Bearer IGT:2:{ses}",
            "claim": "hmac.AR1WoaCh3Y3RfhES8hblKWni9RFpizjJ0LefiiDIVGmhBZ1N",
            "drh": "",
            "user_agent": "Instagram 178.1.0.37.123 Android (28/9; 280dpi; 720x1423; samsung; SM-A205FN; a20; exynos7885; ru_RU; 277249249)",
            "uuids": ["android-e47187f911867ae7", "f6f64d77-e04a-4471-a8a5-eac80cc4162f", "9d3ed3cb-2b33-48ff-be12-61bdcad921bb", "c3b1c133-4aab-4aac-b943-0785c72bb988", "e7b2c672-5d46-45e5-8e05-83391ba570b0"]
        },
        "order_id": str(target_id),
        "pk": str(user_pk),
        "action": "follow"
    }
    payload = encrypt_data(json.dumps(data).encode())
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",
        'Accept-Encoding': "*",
        'Content-Type': "application/xml",
        'x-access': "FiraFollower",
        'x-version': "2"
    }
    response = requests.post(url, data=payload, headers=headers)
    decrypted_response = decrypt_data(response.text)
    print(decrypted_response)

def HHFOL():
    while True:
        url = "https://firafollower.xyz/api/v4/orders.php"
        data = {
            "requested_with": "org.fasaroid.fira",
            "version_code": "120",
            "market_name": "zarinpal",
            "language_code": "ar",
            "device_info": "29/10; 320dpi; 720x1491; HUAWEI; ART-L29N; ART-L29N; ART-L29N",
            "user_token": str(token),
            "user_pk": str(id),
            "action": "follow"
        }
        payload = encrypt_data(json.dumps(data).encode())
        headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; ART-L29N Build/HUAWEIART-L29N)",
            'Accept-Encoding': "*",
            'Content-Type': "application/xml",
            'x-access': "FiraFollower",
            'x-version': "2"
        }
        response = requests.post(url, data=payload, headers=headers)
        decrypted_response = decrypt_data(response.text)
        json_data = json.loads(decrypted_response)
        if 'data' in json_data and len(json_data['data']) > 1:
            target_id = json_data['data'][1]['id']
            user_pk = json_data['data'][1]['user_pk']
            CoinFollow(target_id, user_pk)
        else:
            print("No more Requests")

def link_Hacktive_Mahos():
    """Start the automation processes in separate threads."""
    threading.Thread(target=HHLIKE).start()
    threading.Thread(target=HHCOM).start()
    threading.Thread(target=HHFOL).start()

def MainMahos():
    """Main function to execute the script."""
    print("Starting Fira Coin Up...")
    link_Hacktive_Mahos()

if __name__ == "__main__":
    MainMahos()
