from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        data = request.json()
        if 'hello' in data:
            hello_text = data['hello']
            # Do something with the received 'hello' text
            return JsonResponse({"status": "success", "message": "Hello text received and processed."})
        else:
            return JsonResponse({"status": "error", "message": "Invalid payload."})
    else:
        return JsonResponse({"status": "error", "message": "Invalid HTTP method."})
