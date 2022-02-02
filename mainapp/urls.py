from django.urls import path
from mainapp.apis.customers import CustomerList
from mainapp.apis.token import CreateToken

app_name = "core"

urlpatterns = [
    path("token/", CreateToken.as_view(), name="token"),
    path("customers/", CustomerList.as_view(), name="customers"),
]
