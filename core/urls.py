from django.contrib import admin
from django.urls import path

from main.views import ContactCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact-create/', ContactCreateView.as_view(), name='contact-create'),
]
