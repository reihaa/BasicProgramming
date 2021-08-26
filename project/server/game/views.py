from game.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    inf = request.POST.dict()
    if User.objects.filter(username=inf['username']):
        return HttpResponse("Your data is not valid", status=403)
    if request.session.get('User_id', False):
        return HttpResponse('You have been loged in previously', status=403)
    try:
        person = User.objects.create(username=inf['username'], password=inf['password'])
        person.save()
    except:
        return HttpResponse("Your data is not valid", status=403)
    request.session['User_id'] = person.id
    request.session.save()
    return HttpResponse('registration successful')


@csrf_exempt
def login(request):
    inf = request.POST.dict()
    if request.session.get('User_id', False):
        return HttpResponse('You have been loged in previously', status=403)
    person = User.objects.filter(username=inf['username'], password=inf['password'])
    if person:
        request.session['User_id'] = person[0].id
        request.session.save()
        return HttpResponse('you loged in', status=200)
    else:
        return HttpResponse('incorrect username or password', status=403)


@csrf_exempt
def logout(request):
    try:
        del request.session['User_id']
    except KeyError:
        pass
    return HttpResponse('loged out', status=200)

