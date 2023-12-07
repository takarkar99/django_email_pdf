from django.shortcuts import render, redirect, HttpResponse
from .forms import CustomUserCreationForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from CustomUser.models import CustomUser
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from .token import account_activation_token
from django.core.mail import send_mail
from django.conf import settings

class SignUpview(View):
    form = CustomUserCreationForm
    temp = 'Auth/Sign.html'

    def get(self, request):
        self.form = SignUpview.form
        self.temp = SignUpview.temp
        context = {'forms': self.form}
        return render(request, self.temp, context)
    
    
    def post(self, request):
        self.form = SignUpview.form(request.POST)
        try:
            user_email = request.POST.get("email")
            print("user_email", user_email)
            if user_email:
                existing_user = CustomUser.objects.get(email=user_email)
                if not existing_user.is_active:
                    existing_user.delete()
        except CustomUser.DoesNotExist:
            pass
        if self.form.is_valid():
                self.form.save()
                user_email = self.form.cleaned_data.get("email")
                # print("user_email", user_email)
                try:
                    user = CustomUser.objects.get(email=user_email)
                except CustomUser.DoesNotExist:
                    pass
                if user:
                    current_site = get_current_site(request) ## www.https://8000
                    mail_subject = "Activate Your Account"
                    message = render_to_string("Auth/acc_active_email.html", {
                        "user": user,
                        "domain": current_site.domain,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": account_activation_token.make_token(user),
                    })

                    to_mail = user_email

                    # form = self.get_form()

                    try:
                        send_mail(
                            subject=mail_subject,
                            message=message,
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=[to_mail],
                            fail_silently=False 
                        )
                        # messages.success(request, "Activation email sent. Please check your email.")
                        return HttpResponse("Activation email sent. Please check your email.")
                    except Exception as e:

                        self.form.add_error(None, "Error occurred in sending email. Please try again.")

                        #messages.error(request, "Error occurred in sending email. Please try again.")
                        return render(request, self.temp, {'form': self.form})
                else:
                
                    self.form.add_error('email', "User with this email does not exist.")
                    messages.error(request, "User with this email does not exist.")
        return render(request, self.temp, {'form': self.form}) 


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist) as e:
        pass

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active =True
        user.email_is_verified = True
        user.save()
        messages.success(request, "Successfully  Activate!! ")
        return redirect("login_url")
    return HttpResponse("Activation link is invalid or your account is already Verified! Try To Login")




class LoginView(View): 

    temp = 'Auth/login.html'
    def get(self, request):
        self.temp = LoginView.temp
        return render(request, self.temp, {})

    def post(self, request):
        self.temp = LoginView.temp
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        print(un)
        print(pw)
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect("employee_list_url") 

        return HttpResponse("Enter the correct credential")
    

class LogOutView(View):

    def get(self, reqeust):
        logout(reqeust)
        return redirect("login_url")