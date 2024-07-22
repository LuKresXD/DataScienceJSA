from flask import Flask, request, jsonify

app = Flask(__name__)


class Notification:
    def send(self, params):
        raise NotImplementedError("Send method not implemented")


class EmailNotification(Notification):
    def send(self, params):
        email = params.get("email")
        subject = params.get("subject")
        message = params.get("message")
        print(f"Sending email to {email} with subject '{subject}' and message '{message}'")
        return {"status": "Email sent"}


class SMSNotification(Notification):
    def send(self, params):
        phone = params.get("phone")
        message = params.get("message")
        print(f"Sending SMS to {phone} with message '{message}'")
        return {"status": "SMS sent"}


class PushNotification(Notification):
    def send(self, params):
        device_id = params.get("device_id")
        message = params.get("message")
        print(f"Sending push notification to device {device_id} with message '{message}'")
        return {"status": "Push notification sent"}


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "EmailNotification":
            return EmailNotification()
        elif notification_type == "SMSNotification":
            return SMSNotification()
        elif notification_type == "PushNotification":
            return PushNotification()
        else:
            raise ValueError("Unknown notification type")


@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.json
    notification_type = data.get("type")
    params = data.get("params", {})

    try:
        notification = NotificationFactory.create_notification(notification_type)
        result = notification.send(params)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)