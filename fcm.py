import requests

# Firebase 콘솔에서 발급받은 서버 키로 바꿔주세요!
FCM_API_KEY = "YOUR_FIREBASE_SERVER_KEY"
FCM_ENDPOINT = "https://fcm.googleapis.com/fcm/send"

def send_fcm_notification(device_token: str, title: str, body: str):
    headers = {
        "Authorization": f"key={FCM_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "to": device_token,
        "notification": {
            "title": title,
            "body": body
        },
        "priority": "high"
    }

    response = requests.post(FCM_ENDPOINT, json=payload, headers=headers)

    if response.status_code != 200:
        print("FCM Error:", response.json())

    return response.status_code, response.json()
