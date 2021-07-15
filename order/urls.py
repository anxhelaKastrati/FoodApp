from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import MyPasswordChangeView,MyPasswordResetDoneView


urlpatterns = [

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),

    path('account/', views.accountSettings, name="account"),

    path('items/', views.items, name="items"),
    path('customer/<str:pk>/', views.customer, name="customer"),

    path('change-password/',MyPasswordChangeView.as_view(), name="password-change"),
    path('change-password/done/',MyPasswordResetDoneView.as_view(), name="password-change-done-view"),

    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('add_items/', views.AddItem, name="add_item"),


    ]