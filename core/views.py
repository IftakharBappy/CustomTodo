from django.shortcuts import render_to_response
from .models import Todo


def index(request):

    items = Todo.objects.all()

    return render_to_response('index.html', {'items': items})

