from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    # if (request.user.username == ""):
        return HttpResponse(
            '<h1>Hi There!<br> Please <a href="/accounts/login">Login</a> or <a href="/accounts/register">Sign up</a></h1>')

    # else:
    #     return redirect('/welcome')