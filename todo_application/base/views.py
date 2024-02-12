from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def home(request):
    todo_objs = Todo.objects.all()
    data = {'todos':todo_objs}
    return render(request, 'index.html', context=data)
       

def create(request):
   if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        print(name, description, status)
        Todo.objects.create(name=name, descrription=description, status=status)
        return redirect('home')
      
   return render(request, 'create.html')


def edit(request,pk):
   todo_obj = Todo.objects.get(id=pk)
   return render(request, 'edit.html')

