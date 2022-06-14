from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Homepage,Homepage1,Homepage2,Homepage3,Homepage4,Homepage5,Homepage6,Aboutnew,Hotelpage,Hotelpage2,Blogpage,Blogpage1
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")



class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        prod = Homepage1.objects.filter()
        homes = Homepage.objects.all()
        prod2 = Homepage2.objects.filter()
        prod3 = Homepage3.objects.filter()
        prod4 = Homepage4.objects.filter()
        prod5 = Homepage5.objects.filter()
        prod6 = Homepage6.objects.filter()
        return render(request, self.template_name, {'prod':prod, 'homes':homes, 'prod2':prod2, 'prod3':prod3, 'prod4':prod4, 'prod5':prod5, 'prod6':prod6})



class HomePageDetailView(DetailView):
    template_name = 'index_detail.html'

    def get(self, request, id):
        homs = Homepage1.objects.get(pk=id)
        return render(request, self.template_name, {'homs':homs})


class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        abouts = Aboutnew.objects.all()
        return render(request, self.template_name, {'abouts':abouts})




class HotelListView(ListView):
    template_name = 'hotel.html'

    def get(self, request):
        hotels = Hotelpage.objects.all()
        hotels2 = Hotelpage2.objects.all()
        return render(request, self.template_name, {'hotels':hotels, 'hotels2':hotels2})


class BlogListView(ListView):
    template_name = 'blog.html'

    def get(self, request):
        slide = Blogpage.objects.all()
        slide1 = Blogpage1.objects.all()
        return render(request, self.template_name, {'slide':slide, 'slide1':slide1})









def trichq(request):
    return render(request, 'trichq.html')


def comment(request):
    return render(request, 'comment.html')