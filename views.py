
from django.shortcuts import render,redirect
from employee.models import Employee
from employee.forms import Employeeform


def emp(requset):
    if requset.method=="POST":
        form=Employeeform(requset.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except :
                pass
    else:
        form=Employeeform()
    return render(requset,"index.html",{'form':form})


# def show(requset):
#     data = Employee.objects.all()
#     return render(requset,"show.html",{'Employees':data}) 




def show(request):
    data = Employee.objects.all()
    return render(request, "show.html", {'employees': data})




def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employee': employee})




def updata(requset,id):
    employee=Employee.objects.get(id=id)
    form=Employeeform(requset.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    
    return render(requset,"edit.html",{'employee':employee})


def destory(requset,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
