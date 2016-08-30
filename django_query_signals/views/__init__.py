"""
Project Views
"""

from django.http import JsonResponse

def view(request):
    "Example view"
    return JsonResponse({'response':str(request)})

