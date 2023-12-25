from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [ 
    path("", views.index, name="ShopHome"),
    path("signup/", views.signup, name="signup"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContacttUs"),
    path("tracker/", views.tracker, name="Trackingstatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductViews"),
    path("checkout/", views.checkout, name="Checkout"),
    path("login/", views.loginpage, name="login"),
    path("logout/", views.logoutpage, name="logout"),



]
