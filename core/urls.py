from django.urls import path
from .views import TestView, RegisterUserView, CallView, ReportSpamView, SearchView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('call/', CallView.as_view(), name='call'),
    path('search/', SearchView.as_view(), name='search'),
    path('spam/', ReportSpamView.as_view(), name='report_spam'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
