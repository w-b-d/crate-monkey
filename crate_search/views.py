from django.shortcuts import render
from django.http import HttpResponse
import requests
import random
import os
import json


from django.urls import reverse

# Create your views here.
from . import forms
from django.shortcuts import redirect

token = 'rsBQBogyWJHPVFbkKHpXmfBLvjAHUbhHbqavFmES'



def home(response):
    if response.method =='POST':
        form = forms.Search(response.POST)



        if form.is_valid():





            form_genre = form.cleaned_data["genre"]



            if form_genre == 'Random':
                available_genres = [choice[0] for choice in form.fields['genre'].choices if choice[0] != 'Random']
                form_genre = random.choice(available_genres)















        return redirect(reverse('select_style') + '?genre=' + form_genre)



    else:

        form = forms.Search()
        print(token)



        return render(response,'crate_main/home.html',{'form':form})


def index(response):

    return render(response,"crate_main/base.html",{})

def search(response):
    if response.method =='POST':
        form = forms.Search(response.POST)



        if form.is_valid():



            form_genre = form.cleaned_data["genre"]



            if form_genre == 'Random':
                available_genres = [choice[0] for choice in form.fields['genre'].choices if choice[0] != 'Random']
                form_genre = random.choice(available_genres)















        return redirect(reverse('select_style') + '?genre=' + form_genre)



    else:

        form = forms.Search()



        return render(response,'crate_search/search.html',{'form':form})




def select_style(request):


    if request.method == 'POST':
        genre = request.POST.get('genre')

        if genre == 'Blues':
            form = forms.Blues(request.POST)
        elif genre == 'Brass':
            form = forms.Brass(request.POST)
        elif genre == 'Classical':
            form = forms.Classical(request.POST)
        elif genre == 'Electronic':
            form = forms.Electronic(request.POST)
        elif genre == 'Folk':
            form = forms.Folk(request.POST)
        elif genre == 'Funk / Soul':
            form = forms.Funk(request.POST)
        elif genre == 'Jazz':
            form = forms.Jazz(request.POST)
        elif genre == 'Latin':
            form = forms.Latin(request.POST)
        elif genre == 'Pop':
            form = forms.Pop(request.POST)
        elif genre == 'Reggae':
            form = forms.Reggae(request.POST)
        elif genre == 'Rock':
            form = forms.Rock(request.POST)
        else:
            print(genre)
            return HttpResponse("invalid genre")


        if form.is_valid():

            form_style = form.cleaned_data['style']
            if form_style == 'Random':
                avaliable_styles = [choice[0] for choice in form.fields['style'].choices if choice[0] != 'Random']
                form_style = random.choice(avaliable_styles)




            base_url = 'https://api.discogs.com/database/search?token={}&genre={}&style={}&page={}&per_page=1'
            url = base_url.format(token, genre,form_style,random.randint(1,10000))

            response_api = requests.get(url)
            data = response_api.json()

            title = data['results'][0]['title']
            cover_image_url = data['results'][0]['cover_image']
            uri = data['results'][0]['uri']
            year = data['results'][0].get('year','No year found')




            return render(request,'crate_search/display_result.html',{'cover_image_url':cover_image_url, 'title': title,'genre':genre,'style':form_style,'uri':uri,'year':year})


        return HttpResponse("hello")



    else:
        genre = request.GET.get('genre')





        if genre == 'Blues':
            form = forms.Blues()
        elif genre == 'Brass':
            form = forms.Brass()
        elif genre == 'Classical':
            form = forms.Classical()
        elif genre == 'Electronic':
            form = forms.Electronic()
        elif genre == 'Folk':
            form = forms.Folk()
        elif genre == 'Funk / Soul':
            form = forms.Funk()
        elif genre == 'Jazz':
            form = forms.Jazz()
        elif genre == 'Latin':
            form = forms.Latin()
        elif genre == 'Pop':
            form = forms.Pop()
        elif genre == 'Reggae':
            form = forms.Reggae()
        elif genre == 'Rock':
            form = forms.Rock()
        else:
            return HttpResponse(genre)

        return render(request,'crate_search/select_style.html',{'form':form, 'genre': genre})


