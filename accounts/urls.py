from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect('login')

urlpatterns = [
    path('', home),   # 👈 THIS FIXES THE 404
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
