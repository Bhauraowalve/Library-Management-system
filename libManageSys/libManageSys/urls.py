from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

from account.views import LoginView, RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('',include('Library.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
