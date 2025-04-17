from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .push_notification import send_push_notification_for_early_warning

class SendNotificationAPIView(APIView):
    def post(self, request):
        user_message = request.data
        success = send_push_notification_for_early_warning(user_message)
        if success:
            return Response({"message": "Notification sent successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to send notification"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
