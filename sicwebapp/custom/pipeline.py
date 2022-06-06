from django.shortcuts import redirect
import requests

def auth_allowed(backend, details, response, *args, **kwargs):
    if not backend.auth_allowed(response, details):
        return redirect('/login')