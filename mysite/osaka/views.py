from django.shortcuts import render
from django.views.decorators.http import require_POST

@require_POST  # 이 데코레이터는 POST 요청만 처리하도록 합니다.
def submit_data(request):
    context =[{'name':'Mitsuka Bose',
               'addr':'1-2-16 Oyodominami, Kita-ku, Osaka 531-0075 Osaka Prefecture',
               'ranking':5},
               {'name':'Mitsuka Bose',
               'addr':'1-2-16 Oyodominami, Kita-ku, Osaka 531-0075 Osaka Prefecture',
               'ranking':5},
    ]
    check_box_values = {'search':"", "Vegan option":"", "Vegetarian friendly":"","Gluten free":"",'selectedOption':""}
    for name in check_box_values:
        check_box_values[name] = request.POST.get(name)
    print(check_box_values)
    return render(request,"osaka.html",context={'datas':context})


def osaka_init(request):
    context = {}
    return render(request,"osaka.html",context=context)