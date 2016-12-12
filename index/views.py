import jsonpickle
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from jsonpickle.tags import JSON_KEY

from index.models import Group, GroupMember
from index.forms import CreateGroup, AddMember
from django.contrib.auth.models import User
from django.shortcuts import render
import json



@csrf_exempt
def welcome(request):
    template =loader.get_template('index/welcome.html')
    groups = Group.objects.filter(groupmember__member_id=request.user.pk)
    context = { 'groups' : groups, 'user_id': request.user.pk }
    return HttpResponse(template.render(context, request))

def createForm(request):
    template =loader.get_template('index/createform.html')
    print("hoooooooooooooooooooooooooo")
    context=''
    return HttpResponse(template.render(context ,request))


def create(request):
    if request.method == "POST":
        # Get the posted form
        cgroup = CreateGroup(request.POST)
        if(cgroup.is_valid()):
            group =Group(name=cgroup.cleaned_data['name'], owner= User.objects.get(pk=request.user.pk))
            group.save()
            groupmember = GroupMember(groupId=group, member_id=request.user.pk)
            groupmember.save()
        # return redirect('addmembers',groupId = group.id)
        # return HttpResponseRedirect("http://google.com")
        return HttpResponseRedirect("../addmembers/"+str(group.id))
    else:
        return redirect('createForm')



def addmembers(request, group_id):
        if(Group.objects.get(pk=group_id).owner!=request.user):
            return redirect('welcome')
        else:
            template = loader.get_template('index/addmember.html')
            context = {'group_id' : group_id}
            return HttpResponse(template.render(context, request))


def addmember(request, group_id):
    if request.method == "POST":
        # Get the posted form
        # cgroup = CreateGroup(request.POST)
        addmember = AddMember(request.POST)
        if(addmember.is_valid()):
            email = addmember.cleaned_data['email']
            groupmember = GroupMember(groupId=Group.objects.get(pk=group_id), member_id=User.objects.get(email= email).id)
            groupmember.save()
            print("saved!")
            return HttpResponse("member added")
    return HttpResponse("ERROR adding the member")

    #     if (cgroup.is_valid()):
    #         group = Group(name=cgroup.cleaned_data['name'], owner=User.objects.get(pk=request.user.pk))
    #         group.save()
    #         groupmember = GroupMemeber(groupId=group, member_id=request.user.pk)
    #         groupmember.save()
    #     # return redirect('addmembers',groupId = group.id)
    #     # return HttpResponseRedirect("http://google.com")
    #     return HttpResponseRedirect("../addmembers/" + str(group.id))
    # else:
    #     return redirect('createForm')


def apiwelcome(request):
    groups = Group.objects.filter(groupmember__member_id=request.user.pk)
    return HttpResponse(json.dumps(json.loads(jsonpickle.encode(groups, unpicklable=True)), indent=2))