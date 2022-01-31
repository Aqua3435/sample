from django.shortcuts import render, redirect
from django.views import View

class HomeView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'shop/home.html')

Home = HomeView.as_view()