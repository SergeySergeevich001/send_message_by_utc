from django.http import JsonResponse

from src.tasks import send_messages


def run(request):
    if request.method == 'GET':
        start_hour = request.GET.get('start_hour')
        send_messages(start_hour)
        return JsonResponse({'message': 'OK'})
