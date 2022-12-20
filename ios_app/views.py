from .models import Account
from rest_framework import viewsets, permissions
from .serializer import AccountSerializer

class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]