from django.urls import include, path

from accounts.views import ProfilePageView, UserRegistrationView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('registration/', UserRegistrationView.as_view(), name='registration')
]
