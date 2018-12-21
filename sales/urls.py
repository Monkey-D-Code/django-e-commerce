from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('make/' , views.make_sale , name='make-sale'),
]
