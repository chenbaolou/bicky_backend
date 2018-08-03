from django.http import (HttpResponse, JsonResponse, HttpResponseForbidden)
from django.contrib.auth import authenticate, login, logout as djlogout
import json


class HttpResponseUnauthorized(HttpResponse):
    status_code = 401


def check_authentication_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):

        # ajax session expired
        if request.user.is_authenticated is False:
            if request.is_ajax():
                return HttpResponseUnauthorized()
            else:
                pass
        else:
            pass
        setattr(request, '_dont_enforce_csrf_checks', True)

        response = get_response(request)

        return response

    return middleware


def loginauth(request):
    req = json.loads(request.body)
    login_type = req.get('type')
    user = authenticate(username=req.get('userName'), password=req.get('password'))

    res = {
        'status': 'ok',
        'type': login_type,
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


def current_user(request):
    user = request.user
    res = dict()
    res['name'] = user.username
    res['avatar'] = 'https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png'
    res['userid'] = user.id
    res['notifyCount'] = 12
    return JsonResponse(res)


def logout(request):
    djlogout(request)
    return JsonResponse({'success':'yes'})
