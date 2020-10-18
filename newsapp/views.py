from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Entry
from django.contrib.auth.mixins import LoginRequiredMixin 


# Create your views here.
def home(request):
	import requests
	import json

	news_api_request=requests.get(
		"http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=85aecb18dc8a459fb122eded328234d9"
	)
	api = json.loads(news_api_request.content)
	return render(request, 'home.html',{'api': api})

def bloghome(request):
    return render(request, 'bloghome.html')	

class HomeView(ListView):
	model = Entry
	template_name = 'entries/index.html'
	context_object_name = "blog_entries"
	ordering = ["-date"]
	paginate_by = 3

class EntryView(DetailView):
	model = Entry
	template_name = "entries/entry_detail.html"

class CreateEntryView(CreateView):
	model = Entry
	template_name = "entries/create_entry.html"
	fields = ['title', 'text']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class UpdatePostView(UpdateView):
	model = Entry
	template_name = "entries/update.html"
	fields = ['title', 'text']

class DeletePostView(DeleteView):
	model = Entry
	template_name = "entries/delete.html"
	fields = ['title', 'text']	











