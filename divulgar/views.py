from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from .models import Tag, Raca, Pet
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.


@login_required
def novo_pet(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        racas = Raca.objects.all()
        return render(request, "novo_pet.html", {'tags': tags, 'racas': racas})
    elif request.method == 'POST':
        foto = request.FILES.get('foto')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        tags = request.POST.getlist('tags')
        raca = request.POST.get('raca')

        # ToDo : validar os dados
        # ToDo : usar API para estado e cidade

        pet = Pet(
            usuario=request.user,
            foto=foto,
            nome=nome,
            descricao=descricao,
            estado=estado,
            cidade=cidade,
            telefone=telefone,
            raca_id=raca,
        )

        pet.save()

        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            pet.tags.add(tag)

        pet.save()
        return redirect('/divulgar/seus_pets')
       # tags = Tag.objects.all()
       # racas = Raca.objects.all()
       # messages.add_message(request, constants.SUCCESS, 'Novo pet cadastrado')
       # return render(request, 'novo_pet.html', {'tags': tags, 'racas': racas})


@login_required
def seus_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(usuario=request.user)
        return render(request, 'seus_pets.html', {'pets': pets})


@login_required
def remover_pet(request, id):
    pet = Pet.objects.get(id=id)
    if not pet.usuario == request.user:
        messages.add_message(request, constants.ERROR,
                             'Esse pet não é seu, espertinho hahaha')
        return redirect("/divulgar/seus_pets")

    pet.delete()
    messages.add_message(request, constants.SUCCESS,
                         'Pet removido com sucesso')
    return redirect("/divulgar/seus_pets")


def ver_pet(request, id):
    if request.method == "GET":
        pet = Pet.objects.get(id=id)
        return render(request, "ver_pet.html", {'pet': pet})
