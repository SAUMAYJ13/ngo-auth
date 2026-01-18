from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect('/login/')   # ✅ FIXED

urlpatterns = [
    path('', home),              # homepage redirect
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
