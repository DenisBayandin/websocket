from django.shortcuts import render


def note_view(request):
    return render(request, 'websocket/example.html')
