from django.shortcuts import render
from django.views.decorators.http import require_POST
import static.main as search
@require_POST  #execute fuction when enter is pushed 
def submit_data(request): #after push enter
    search.init_osaka()

    check_box_values = {'search':"", "Vegan option":"", "Vegetarian friendly":"","Gluten free":"",'selectedOption':"",'orderOption':''}
    for name in check_box_values:
        check_box_values[name] = request.POST.get(name)
    context = search.search_osaka(check_box_values)
    return render(request,"osaka.html",context={'datas':context})

def osaka_init(request):
    context = {}
    return render(request,"osaka.html",context=context)