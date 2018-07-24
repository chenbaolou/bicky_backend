from django.shortcuts import render
from django.http import (HttpResponse, JsonResponse, HttpResponseForbidden)
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout as djlogout
import json

class HttpResponseUnauthorized(HttpResponse):
    status_code = 401

def CheckAuthenticationMiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):

        #ajax session expired
        if request.user.is_authenticated == False:
            if request.is_ajax():
                return HttpResponseUnauthorized()
            else:
                pass
        else:
            pass

        response = get_response(request)

        if response.status_code == 403:
            return HttpResponseForbidden()
        else:
            return response

        return response

    return middleware

def loginauth(request):
    print(request.body)
    req = json.loads(request.body)
    type = req.get('type')
    user = authenticate(username=req.get('userName'), password=req.get('password'))

    res = {
        'status': 'ok',
        'type': type,
        'currentAuthority': 'admin'
    }
    
    if user is not None:
        # the password verified for the user
        if user.is_active:
            login(request, user)
        else:
            res['status'] = 'error'
    else:
        # the authentication system was unable to verify the username and password
        res['status'] = 'error'
    
    return JsonResponse(res)

def currentUser(request):
    user = request.user
    res = {}
    res['name'] = user.username
    res['avatar'] = 'https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png'
    res['userid'] = user.id
    res['notifyCount'] = 12
    return JsonResponse(res)

def logout(request):
	djlogout(request)
	return JsonResponse({'success':'yes'})
