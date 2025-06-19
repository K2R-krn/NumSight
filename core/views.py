from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GlobalUser, GlobalContacts
from .serializers import GlobalUserSerializer
from django.db.models import Q

# Test View
class TestView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        return Response({"message": "Hello, authenticated user!"})

# RegisterUserView
class RegisterUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        phone_number = request.data.get('phone_number')

        try:
            user = GlobalUser.objects.get(phone_number=phone_number)

            updated = False
            if (not user.name) and request.data.get('name'):
                user.name = request.data.get('name')
                updated = True
            if (not user.email_address) and request.data.get('email_address'):
                user.email_address = request.data.get('email_address')
                updated = True

            if updated:
                user.save()
                serializer = GlobalUserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "User with this phone number already exists and no fields were updated."}, status=status.HTTP_400_BAD_REQUEST)

        except GlobalUser.DoesNotExist:
            serializer = GlobalUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CallView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        phone_number = request.data.get('phone_number')

        if not phone_number:
            return Response({"error": "Phone number is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = GlobalUser.objects.get(phone_number=phone_number)
        except GlobalUser.DoesNotExist:
            user = GlobalUser(phone_number=phone_number)
            user.save()

        user.total_appearance += 1
        if user.total_appearance > 0:
            user.spam_likelyhood = (user.num_spam / user.total_appearance) * 100
        else:
            user.spam_likelyhood = 0

        user.save()
        serializer = GlobalUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReportSpamView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        phone_number = request.data.get('phone_number')

        if not phone_number:
            return Response({"error": "Phone number is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = GlobalUser.objects.get(phone_number=phone_number)
        except GlobalUser.DoesNotExist:
            user = GlobalUser(phone_number=phone_number)
            user.save()

        user.num_spam += 1
        if user.total_appearance > 0:
            user.spam_likelyhood = (user.num_spam / user.total_appearance) * 100
        else:
            user.spam_likelyhood = 0

        user.save()
        serializer = GlobalUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('query')
        email = request.query_params.get('email')  
        
        if not query:
            return Response({"error": "Query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        search_type = 'phone' if query.isdigit() else 'name'

        if search_type == 'name':
            users_by_name_start = GlobalUser.objects.filter(name__istartswith=query)
            users_by_name_contains = GlobalUser.objects.filter(name__icontains=query).exclude(name__istartswith=query)
            
            users = users_by_name_start | users_by_name_contains
        else:
            users = GlobalUser.objects.filter(phone_number__icontains=query)

        results = []
        
        for user in users:
            user_data = {
                'name': user.name,
                'phone_number': user.phone_number,
                'spam_likelyhood': user.spam_likelyhood,
            }

            if email:
                try:
                    registered_user = GlobalUser.objects.get(email_address=email)
                    
                    contact_exists = GlobalContacts.objects.filter(
                        Q(contact_from=registered_user.email_address, contact_to=user.email_address) |
                        Q(contact_from=user.email_address, contact_to=registered_user.email_address)
                    ).exists()

                    if contact_exists:
                        user_data['email_address'] = user.email_address

                except GlobalUser.DoesNotExist:
                    pass

            results.append(user_data)

        return Response(results, status=status.HTTP_200_OK)