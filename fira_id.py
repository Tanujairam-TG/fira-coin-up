import base64
import json
import webbrowser
import time
from NamasteAes import NamasteAes
from config import encrypted_data

def decrypt_and_extract(data, key, iv):
    decrypted_data = NamasteAes.dec_cbc(data, key, iv)
    results = json.loads(decrypted_data)

    auth_token = results['control']['auth']
    encoded_part = auth_token.split('Bearer IGT:2:')[1]
    decoded_auth = base64.b64decode(encoded_part).decode('utf-8')
    decoded_auth_json = json.loads(decoded_auth)

    session_id = decoded_auth_json.get('sessionid', 'N/A')
    user_token = results.get('user_token', 'N/A')
    user_pk = results.get('user_pk', 'N/A')

    return {
        'session_id': session_id,
        'user_token': user_token,
        'user_pk': user_pk
    }

if __name__ == "__main__":
    encrypted_data = 'Enter_Encrypted_Data'
    key = '83108793d2e582de26095e6365006b683549db8300bac461d36fb6e4c27f2dbd'
    iv = '51afa8b2e0a47a37881424fb9b88b8bc'
    
    extracted_data = decrypt_and_extract(encrypted_data, key, iv)
    
    print(f"Session ID: {extracted_data['session_id']}")
    print(f"User Token: {extracted_data['user_token']}")
    print(f"User PK: {extracted_data['user_pk']}")
    
    time.sleep(2)
    webbrowser.open('https://t.me/hacktive_mind')
