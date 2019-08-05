from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('test-page/', test_page, name='test-page'),
    path('myapp/', include('myapp.urls'))
]
