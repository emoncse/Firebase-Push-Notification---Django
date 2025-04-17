from firebase_admin import messaging
from .firebase_admin_sdk import firebase_admin

def send_push_notification_for_early_warning(user_message: dict):

    try:
        notification = messaging.Notification(
            title=user_message.get("title", "Notification"),
            body=user_message.get("body", "Notification"),
            image=user_message.get("image") if "image" in user_message else None
        )

        message = messaging.Message(
            notification=notification,
            topic="all-users"
        )
        print(message)

        response = messaging.send(message)
        print("Notification sent successfully:", response)
        return True
    except Exception as e:
        print("Error sending notification:", str(e))
        return False
