from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import PostForm


def index(request):
    lottos = GuessNumbers.objects.all
    location = Location.objects.get(id=1)
    return render(request, 'lotto/index.html', {'lottos': lottos, 'location': location})


def post(request):
    form = PostForm()
    return render(request, 'lotto/form.html', {'form': form})


def post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'lotto/form.html',
                      {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()
            return redirect('/lotto')


def detail(request):
    key = request.GET['lotto_num']
    lotto = GuessNumbers.objects.get(id=key)
    return render(request, 'lotto/detail.html', {'lotto': lotto})


def detail2(request, num):
    lotto = GuessNumbers.objects.get(id=num)
    return render(request, 'lotto/detail2.html', {'lotto': lotto})


def join(request):
    if request.method == 'GET':
        return render(request, 'lotto/join.html', {})
    else:
        id = request.POST['id']
        pw = request.POST['pw']
        name = request.POST['name']

        m = Member(id=id, password=pw, name=name)
        m.save()
        return render(request, 'lotto/join_result.html', {'id': id, 'name': name})

@csrf_exempt
def id_check(request):
    id = request.POST['id']
    try :
        Member.objects.get(id=id)

    except Member.DoesNotExist as e :
        pass
        return HttpResponse('가입가능')
    else :
        res = {'id':id, 'msg':'가입불가'}
        return JsonResponse(res)


