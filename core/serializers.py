from rest_framework import serializers
from .models import GlobalUser

class GlobalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalUser
        fields = ['id', 'name', 'phone_number', 'email_address', 'num_spam', 'total_appearance', 'spam_likelyhood']