from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
from .sort import sort
from django.contrib import auth
from django.contrib.auth import authenticate, login,logout
from django.forms.models import model_to_dict
from django.core import serializers


# Create your views here.
def auth(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/main/')
    else:
        authform = {'auth':FormsAuth()}
        return render(request,'auth.html',authform)

def check(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/auth/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/main/')
                else:
                    return HttpResponseRedirect('/auth/')
            else:
                return HttpResponseRedirect('/auth/')
        else:
            return HttpResponseRedirect('/auth/')



def result(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():

            text = ''
            for chunk in request.FILES['file'].chunks():
                text += chunk.decode('utf-8')

            words, allwordscount = sort.sort(text,Dict.objects.values_list('word', flat=True),Dict.objects.values_list('translate', flat=True))

            old_data = Data.objects.filter(user=request.user)
            old_data.delete()

            for word in words:
                note = Data()
                note.user = request.user
                note.word = word
                note.translate = words[word][0]
                note.iteration = words[word][1]
                note.save()

            stat = Data.objects.values_list('iteration', flat=True).order_by('-iteration')

            return render(request, 'result.html',{'statistic': sort.statistic(stat,allwordscount)})

        else:
            HttpResponseRedirect('/main/')
    else:
        HttpResponseRedirect('/main/')


def main(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/auth/')
    if request.method == 'POST':
        data = {'form': FileForm(), 'login': request.POST.get('percent')}
        return render(request, 'main.html', data)
    data = {'form': FileForm(),'login': request.user}
    return render(request, 'main.html', data)


def learn(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/auth/')

    data = Data.objects.filter(user=request.user).order_by('-level', '-iteration')
#    translate = Data.objects.filter(user=request.user).order_by('-level', '-iteration').values_list('translate', flat=True)
#    iteration = Data.objects.filter(user=request.user).order_by('-level', '-iteration').values_list('iteration', flat=True)
#    level = Data.objects.filter(user=request.user).order_by('-level', '-iteration').values_list('level', flat=True)
#,'translate':translate,'iteration':iteration,'level':level

    data = serializers.serialize('json',data)
    return render(request, 'learn.html', {'data':data,})#list(data)

def dictionary(request):
    return render(request, 'dictionary.html')