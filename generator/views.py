import random

from django.shortcuts import render


def password(request):
    return render(
        request,
        'generator/password.html'
    )


def about(request):
    return render(
        request,
        'generator/about.html'
    )


def generate(request):
    if request.GET:
        CHARACTERS: list = list('qwertyuiopasdfghjklzxcvbnm')
        length: int = int(request.GET.get('length'))

        if request.GET.get('uppercase'):
            CHARACTERS.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
        if request.GET.get('number'):
            CHARACTERS.extend(list('1234567890'))
        if request.GET.get('special'):
            CHARACTERS.extend(list('!@#$%^&*()_-=+'))

        the_password: str = ''
        for i in range(length):
            the_password += random.choice(CHARACTERS)

        return render(
            request,
            'generator/generate.html',
            {
                "password": the_password
            }
        )

    return render(
        request,
        'generator/password.html'
    )
