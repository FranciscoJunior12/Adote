from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from divulgar.models import Pet, Raca
from adotar.models import Pedido_Adocao
from django.contrib.messages import constants
from django.contrib import messages
from datetime import datetime
# Create your views here.

@login_required
def listar_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status="P")
        racas = Raca.objects.all()

        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')

        if cidade:
            pets = pets.filter(cidade__icontains=cidade)

        if raca_filter:
            pets = pets.filter(raca=raca_filter)

        return render(request, 'listar_pets.html', {'pets': pets, 'racas': racas, 'cidade': cidade, 'raca_filter': raca_filter})


def pedido_adocao(request, id):
    if request.method == "GET":
        pet = Pet.objects.filter(id=id).filter(status='P')

        if not pet.exists():
            messages.add_message(request, constants.WARNING,
                                 'Esse pet ja foi adotado')
            return redirect('/adotar')

        pedido = Pedido_Adocao(
            usuario=request.user,
            pet=pet.first(),
            data=datetime.now()

        )
        # ToDo : validar  se ja existe um pedido do usuario logado ao pet
        pedido.save()
        messages.add_message(request, constants.SUCCESS,
                             'Pedido de Adoção feito com sucesso.')

        return redirect('/adotar')
