from django.shortcuts import render, redirect
from .models import Employee
from django.views import View
from .forms import Employeeform
from django.http import HttpResponse
from .models import Employee
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class EmployeeView(LoginRequiredMixin , View):
    login_url = 'login_url'
    temp = 'App1/home.html'
    forms = Employeeform

    def get(self, request):
        self.temp = EmployeeView.temp
        self.form = EmployeeView.forms
        context = {'forms': self.forms}
        return render(request, self.temp, context)
    

    def post(self, request):

        self.forms = EmployeeView.forms(request.POST)
        if self.forms.is_valid():
            self.forms.save()
            return redirect("employee_list_url")
        return HttpResponse("their is some error")
    

class EmployeListView(LoginRequiredMixin , View):
    login_url = 'login_url'
    temp = "App1/List.html"

    def get(self, request):
        obj = Employee.objects.all()
        self.temp = EmployeListView.temp
        context = {"obj": obj}
        return render(request, self.temp, context)


class EmployeeUpdate(LoginRequiredMixin , View):
    login_url = 'login_url'
    temp = "app1/home.html"
    form = Employeeform

    def get(self,request, pk):
        obj = get_object_or_404(Employee, id=pk)
        self.temp = EmployeeUpdate.temp
        self.form = Employeeform(instance=obj)
        context = {"forms": self.form}
        return render(request, self.temp, context)
    
    def post(self, request, pk):
        obj = get_object_or_404(Employee, id=pk)
        self.form = Employeeform(request.POST, instance=obj)
        if self.form.is_valid():
            self.form.save()
            return redirect("employee_list_url")
        return HttpResponse("Enter Proper Information")


class EmployeeDelete( LoginRequiredMixin, View):
    login_url = 'login_url'
    temp = "App1/delete.html"

    def get(self, request, pk):
        obj = get_object_or_404(Employee, id=pk)
        self.temp = EmployeeDelete.temp
        context = {"obj": obj}
        return render(request, self.temp, context)


    def post(self, request, pk):
        obj = get_object_or_404(Employee, id=pk)
        obj.delete()
        return redirect("employee_list_url")
        