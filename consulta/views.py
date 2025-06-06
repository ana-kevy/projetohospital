from django.shortcuts import render
# fazer import de consulta
from .models import consulta


# Create your views here.
def lista_consultas(request):
    consultas = consulta.objects.all()
    return render(request, 'consultas/consulta_list.html', {'consultas': consultas})

# funções e operaões do sistema 
