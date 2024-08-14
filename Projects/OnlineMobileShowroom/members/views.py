from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import Member
from django.db.models import Q

# Create your views here.

# def members(request):
#     return HttpResponse("Hello World!")


# def members(request):
#     template = loader.get_template('home.html')
#     return HttpResponse(template.render())

def members(request):
    mymembers = Member.objects.all().values()
    total_members = Member.objects.all().count()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers,
        'total_members' : total_members,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def category(request):
    return HttpResponse("Categories wil be displayed here!<br>Like Honda, Suzuki, etc which we will show them using html pages")

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    filtering_data = Member.objects.filter(firstname = 'Muhammad').values()
    filtering_data_with_s_r_c = Member.objects.filter(firstname = 'Muhammad', id = 1).values()
    filtering_data_with_s_r_c_Q = Member.objects.filter(Q(firstname = 'Muhammad') | Q(firstname = 'Ahmed')).values()
    mydata = Member.objects.all().values()
    mydata1 = Member.objects.values_list('firstname')
    mydata2 = Member.objects.filter(firstname__startswith='M').values()
    template = loader.get_template('childtemplate.html')
    ob_firstname = Member.objects.all().order_by('firstname', '-id').values()
    context = {
        "firstname": "Usman",
        'greeting': 1,
        'heading': 'Hello &lt;i&gt;my&lt;/i&gt; World!',
        'fruits': ['Apple', "Banana", "Cherry", "Orange"],
        'cars': [
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Ford',
                'model': 'Sierra',
                'year': '1981',
            },
            {
                'brand': 'Volvo',
                'model': 'XC90',
                'year': '2016',
            },
            {
                'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964',
            }],
        'fruits' : ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Mango", "Pineapple", "Watermelon", "Avocado", "Blueberry", "Cherry", "Kiwi", "Lemon", "Lime", "Pear"],
        'x' : 20,
        'y' : 20,
        'mymembers': mydata,
        'mydata1': mydata1,
        'mydata2': mydata2,
        'filtering_data' : filtering_data,
        'filtering_data_with_s_r_c' : filtering_data_with_s_r_c,
        'filtering_data_with_s_r_c_Q' : filtering_data_with_s_r_c_Q,
        'ob_firstname': ob_firstname,
    }
    return HttpResponse(template.render(context, request))