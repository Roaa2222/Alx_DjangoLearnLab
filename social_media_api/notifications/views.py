from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        data = [
            {
                "id": n.id,
                "actor": n.actor.username,
                "verb": n.verb,
                "target": str(n.target),
                "timestamp": n.timestamp,
                "is_read": n.is_read,
            }
            for n in notifications
        ]
        return Response(data)

    def post(self, request):  # Mark all as read
        Notification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)
        return Response({"message": "All notifications marked as read!"})
