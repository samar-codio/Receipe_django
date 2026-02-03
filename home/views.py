from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import *

# Create your views here.


def receipe_form(request):
    if request.method == "POST":
        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        if receipe_name and receipe_description and receipe_image:
            receipe.objects.create(
                receipe_name=receipe_name,
                receipe_image=receipe_image,
                receipe_description=receipe_description,
            )
            return redirect('receipe_form')
    vals = receipe.objects.all()
    context = {'receipe_data': vals}

    return render(request, 'receipe_form.html', context)


def delete_receipe(request, id):
    queryset = receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipe/")
