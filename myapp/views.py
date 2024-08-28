from django.shortcuts import render, redirect
from myapp.models import Employee

# View to display all employees
def home(request):
    empdata = Employee.objects.all()
    return render(request, 'home.html', {'empdata': empdata})

# View to add a new employee
def Addemp(request):
    if request.method == "GET":
        return render(request, 'Addemp.html')
    else:
        ename = request.POST["Name"]
        department = request.POST["department"]

        try:
            # Check if an employee with the same name already exists
            user = Employee.objects.get(ename=ename)
        except Employee.DoesNotExist:
            # If not, create a new employee
            user = Employee(ename=ename, department=department)
            user.save()
            return redirect(home)
        else:
            # If an employee with the same name exists, show an error message
            message = "Username already exists. Try another username."
            return render(request, 'Addemp.html', {'message': message})

# View to delete an employee
def delete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect(home)

# View to update an employee's details
def update(request, id):
    if request.method == "GET":
        emp = Employee.objects.get(id=id)
        return render(request, 'update.html', {'emp': emp})
    else:
        ename = request.POST["Name"]
        department = request.POST["Department"]

        emp = Employee.objects.get(id=id)
        emp.ename = ename
        emp.department = department
        emp.save()
        return redirect(home)
