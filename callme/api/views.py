from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import requests

@csrf_exempt
def receive_url(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if 'url' in data:
                url = data['url']
                # Make a POST request to the given URL
                response = requests.post(url, json={"hello": "message i need"})
                return JsonResponse({"status": "success", "message": "URL received and processed."})
            else:
                return JsonResponse({"status": "error", "message": "Invalid payload."})
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON payload."})
    else:
        return JsonResponse({"status": "error", "message": "Invalid HTTP method."})
