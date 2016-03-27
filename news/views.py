from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_news(request):
    txt = request.GET['txt']
    text = ''
    
    festa = 'Buona Pasqua'
    if txt == 'true':
        text = 'Risurrezione di nostro Signore Gesu Cristo'
    
    return JsonResponse({
        'status': 200,
        'data': {
            'news': festa,
            'text': 'Risurrezione di nostro Signore Gesu Cristo'
        }
    })
 