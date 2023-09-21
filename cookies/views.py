from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.


def set_session(request):
    # data = {
    #     'name': 'kashem',
    #     'age': 35,
    #     'lang': 'Bangla'
    # }
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_date())
    # request.session.update(data)
    request.session['name'] = 'karim'
    return render(request, 'home.html')


def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'guest')
        request.session.modified = True
        return render(request, 'get_session.html', {'name': name})
    # age = request.session.get('age')
    # lang = request.session.get('lang')
    # return render(request, 'get_session.html', {'name': name})
    return HttpResponse('Your session has been expired')


def delete_session(request):
    # del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'del.html')


def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'Chaity', max_age=5)  # save for 5 second
    # response.set_cookie(
    #     'name', 'Chaity', expires=datetime.utcnow()+timedelta(days=7))  # saving cookies for 7 days
    return response


def get_cookies(request):
    name = request.COOKIES.get('name')
    return render(request, 'get_cookie.html', {'name': name})


def delete_cookies(request):
    response = render(request, 'home.html')
    response.delete_cookie('name')
    return response
