import firebase_admin
from firebase_admin import credentials, messaging
import os
import json


cred_path = os.path.join(os.path.dirname(__file__), 'firebase.json')

if not firebase_admin._apps:
    with open(cred_path) as f:
        service_account_info = json.load(f)
    cred = credentials.Certificate(service_account_info)
    firebase_admin.initialize_app(cred)
