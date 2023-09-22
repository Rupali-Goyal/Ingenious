from django.contrib import admin
from django.urls import path,include

from django.contrib.auth import views as auth_views

from home import views

urlpatterns = [
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path("",views.index2,name='home'),
    path("textSummary",views.index,name='textSummary'),
    path("questions",views.questions,name='questions'),
    path("about",views.about,name='about'),
    # submit email form
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset/reset_password.html',html_email_template_name='password_reset/password_reset_email.html',subject_template_name='password_reset/password_reset_subject.txt',from_email=''),name="reset_password"),
    # email sent success message
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset/password_reset_done.html"),name="password_reset_done"),
    # link to password reset form in email -- uid is user id in bas 64---token to check if password is valid
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset/password_reset_confirm.html"),name="password_reset_confirm"),
    # password succesfully changed message
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset/password_reset_complete.html"),name="password_reset_complete"),
   # path("new",views.new,name='new'),
]