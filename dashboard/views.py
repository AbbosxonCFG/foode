from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def table(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
    return render(request, 'table.html')
