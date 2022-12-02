from django.http import HttpResponseNotFound

class FilterCookies(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # pid_cookie = request.COOKIES.get("pid")

        # print(pid_cookie)
        
        # if pid_cookie != "12345" :
        #     return HttpResponseNotFound

        response = self.get_response(request)

        return response