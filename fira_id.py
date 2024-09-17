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
    encrypted_data = '''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'''
    key = '83108793d2e582de26095e6365006b683549db8300bac461d36fb6e4c27f2dbd'
    iv = '51afa8b2e0a47a37881424fb9b88b8bc'
    
    extracted_data = decrypt_and_extract(encrypted_data, key, iv)
    
    print(f"Session ID: {extracted_data['session_id']}")
    print(f"User Token: {extracted_data['user_token']}")
    print(f"User PK: {extracted_data['user_pk']}")
    
    time.sleep(2)
    webbrowser.open('https://t.me/hacktive_mind')
