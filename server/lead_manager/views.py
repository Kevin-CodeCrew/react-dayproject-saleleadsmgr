from json import loads
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import UserModel, SalesLeadModel
from .serializers import SalesLeadModelSerializer


# Simple landing page for testing
def index(req):
    print('Index View')
    return HttpResponse('Sales Lead Landing Page')


# // Returns the user ID for the username and password combo if they authenticate
def auth_users(request):
    requestBodyInfo = loads(request.body)
    bodyUsername = requestBodyInfo["username"]
    print(f'bodyUsername = {bodyUsername}')
    bodyPassword = requestBodyInfo["password"]
    print(f'bodyPassword = {bodyPassword}')
    allUsers = UserModel.objects.filter(username=bodyUsername)

    if (allUsers):
        if allUsers[0].password == bodyPassword:
            return HttpResponse(allUsers[0].id)
        else:
            return HttpResponse(False)
    else:
        return HttpResponse(False)


# Gets the ID for given user name
def get_userid(request, username):
    userID = UserModel.objects.filter(username=username)
    return HttpResponse(userID[0].id)


# Gets all sales leads matching the user id
def get_lead_models(request, userFk):
    # print(SalesLeadModel.objects.filter(userFk=userFk))
    # print(userFk)
    leads_for_user = SalesLeadModel.objects.filter(userFk=userFk)
    leads_serializer = SalesLeadModelSerializer(leads_for_user, many=True)
    return JsonResponse(leads_serializer.data, safe=False)
