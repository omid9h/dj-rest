from django.urls import path

from mainapp.apis.token import CreateToken

app_name = 'core'

urlpatterns = [
    path('token/', CreateToken.as_view(), name='token'),
]
