# Firebase Testing Project

This project demonstrates how to integrate Firebase with Django to send push notifications to devices.

## Prerequisites

- Python 3.12 or higher
- Firebase Admin SDK JSON file (e.g., `firebase.json`)
- SQLite (default database for Django)

## Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/emoncse/Firebase-Push-Notification---Django.git
   cd firebase_testing
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Firebase**
   - Place your Firebase Admin SDK JSON file in the root directory and name it `firebase.json`.

5. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver 9000
   ```

## Usage

### Send Notification to All Devices
- Endpoint: `/notify/`
- Method: `GET` or `POST`
- Query Parameters (for GET):
  - `title`: Title of the notification
  - `body`: Body of the notification
  - `data` (optional): Additional data payload


- Example `POST` Request with Weather Alert:
  ```bash
  curl -X POST http://127.0.0.1:9000/notify/ \
  -H "Content-Type: application/json" \
  -d '{
        "title": "Weather Alert!",
        "body": "Hello this is test."
      }'
  ```

## Notes
- Ensure the Firebase Admin SDK JSON file is correctly configured.
- This project is for development purposes only. Do not use the development server in production.

## License
This project is licensed under the MIT License.