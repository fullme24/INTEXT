from django.urls import path
from .views import loginTemplate, CreateTemplate, CreateCompanyTemplate, loggedTemplate, CreatedLoginView, deleteTemplate, deleteView, updateTemplate, updateView
urlpatterns = [
    path("", loginTemplate, name="login"),
    path("create/", CreateTemplate, name="create"),
    path("createcompany/",CreateCompanyTemplate, name="create_company"),
    path("created/", CreatedLoginView, name="created"),
    path("delete/", deleteTemplate, name="deletetemp"),
    path("delete_login/", deleteView, name="delete"),
    path("update_account/", updateView, name="update"),
    path("update/", updateTemplate, name="updatetemp"),
    path('logged_in/', loggedTemplate, name="logged_in"),
]