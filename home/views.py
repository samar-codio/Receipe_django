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

    if request.GET.get('search'):
        queryset = vals.filter(
            receipe_name__icontains=request.GET.get('search'))
        context = {'receipe_data': queryset}
    return render(request, 'receipe_form.html', context)


def delete_receipe(request, id):
    queryset = receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipe/")


def update_receipe(request, id):
    queryset = receipe.objects.get(id=id)
    context = {'up_receipe': queryset}
    if request.method == "POST":

        data = request.POST

        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipe/')

    return render(request, "update_receipe.html", context)
