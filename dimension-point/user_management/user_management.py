from firebase_connection import initialize_firestore

db = initialize_firestore()

def get_user_data(user_id):
    # Firestoreからユーザーの情報を取得
    user_ref = db.collection('users').document(user_id)
    return user_ref.get().to_dict()