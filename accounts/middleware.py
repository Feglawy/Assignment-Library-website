from django.shortcuts import redirect
from django.urls import reverse

class RedirectAuthenticatedUsersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.path in [reverse('login'), reverse('signup')]:
                return redirect('index')
        response = self.get_response(request)
        return response
