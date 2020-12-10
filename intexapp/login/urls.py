from django.urls import path
from .views import listingsView, loginTemplate, CreateTemplate, CreateCompanyTemplate, loggedTemplate, CreatedLoginView, deleteTemplate, deleteView, updateTemplate, updateView,profileView, listingsView, descriptionView1
from django.conf import settings
from django.conf.urls.static import static

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
    path('profile/<int:personID>/<int:personTypeID>/', profileView, name="profileview"),
    path('listings', listingsView, name="listingview"),
    path('listings/description1', descriptionView1, name="descriptionview1"),
    path('listings/description2', descriptionView1, name="descriptionview2"),
    path('listings/description3', descriptionView1, name="descriptionview3"),
    path('listings/description4', descriptionView1, name="descriptionview4"),
    path('listings/description5', descriptionView1, name="descriptionview5"),
    path('listings/description6', descriptionView1, name="descriptionview6"),
    path('listings/description7', descriptionView1, name="descriptionview7"),
    path('listings/description8', descriptionView1, name="descriptionview8"),
    path('listings/description9', descriptionView1, name="descriptionview9"),
    path('listings/description10', descriptionView1, name="descriptionview10"),
]