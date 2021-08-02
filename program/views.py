from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .forms import ProgramForm
from .models import Programs, Specialty
from django.views.generic import ListView


# Create your views here.
def index(request):
    return render(request, 'program/home.html', {'title': 'Main page'})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Неверно введены значения'

    form = ProgramForm()
    data = {
        'form': form,
        'title': 'Creation',
        'error': error
    }

    return render(request, 'program/create.html', data)


class SearchListView(ListView):
    model = Programs

    template_name = 'program/search_results.html'

    # queryset = Programs.objects.filter(Name__contains="Math")
    def queryset(self):
        query = self.request.GET.get('q')
        object_list = Programs.objects.filter(
            Q(Name__contains=query) | Q(Dep__Code__contains=query) | Q(Specialty__Name__contains=query)
        ).distinct()
        return object_list
