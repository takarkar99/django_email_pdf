from django.urls import path
from .views import SignUpview, LoginView, LogOutView
from .views import activate
from django.contrib.auth import views as auth_views 
from django.urls import reverse_lazy

urlpatterns = [
    path("s/", SignUpview.as_view(), name='Sign_url'),
    path('a/', LoginView.as_view(), name='login_url'),
    path('b/', LogOutView.as_view(), name='log_url'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),


# change password

    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name='Auth/password_change_done.html'), name='password_change_done/'), ## password change successfully

    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="Auth/password_change.html", success_url = reverse_lazy("password/change/done/")),name='password_change'), ## To change the password 

# format password

    path("reset_password/", auth_views.PasswordResetView.as_view(template_name ="Auth/password_reset.html", success_url = reverse_lazy("password_reset_done"), email_template_name='Auth/format_password_email.html '), name="reset_password"),
    #1
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="Auth/password_reset_sent.html"),name="password_reset_done"),   
    #2 
    
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="Auth/password_rest_form.html" , success_url = reverse_lazy("password_reset_complete")), name="password_reset_confirm"),
    #3
    
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="Auth/password_reset_done.html"),name='password_reset_complete')
    #4
 ] 