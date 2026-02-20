from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer


class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        # Fetch only the notifications for the logged-in user and Sort by unread first (False = 0, True = 1), then by newest
        return Notification.objects.filter(recipient=self.request.user).order_by(
            "read", "-timestamp"
        )
