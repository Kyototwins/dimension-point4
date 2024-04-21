import os
import firebase_admin
from firebase_admin import credentials, firestore

def initialize_firestore():
    # サービスアカウントキーファイルのパス
    service_account_key_path = os.path.join(os.getcwd(), "serviceAccountKey2.json")
    # Firebase Admin SDKの初期化
    cred = credentials.Certificate(service_account_key_path)
    firebase_admin.initialize_app(cred)
    # Firestoreクライアントの初期化
    return firestore.client()

# Firestoreクライアントをグローバル変数として初期化
db = initialize_firestore()

# ユーザー情報を追加
user_ref = db.collection('users').document('Kyototwins')  # ユーザーIDが'Kyototwins'の場合
user_ref.set({
    'password': '123',
    'points': 100
})
