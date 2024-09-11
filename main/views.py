from django.http import HttpRequest
from django.shortcuts import redirect, render


def main(request: HttpRequest):
    return render(request, "views/main.html")
