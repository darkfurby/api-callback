from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import os
import requests

output_text = ''

@csrf_exempt
def hello(request):

    global output_text

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if 'hello' in data:
                hello_text = data['hello']
                print(hello_text)
                output_text = hello_text
                # Return the received 'hello' text
                return JsonResponse({"hello": hello_text})
            else:
                return JsonResponse({"status": "error", "message": "Invalid payload."})
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON payload."})
    else:
        return JsonResponse({"status": "error", "message": "Invalid HTTP method."})

def get_output(request):
    global output_text
    return JsonResponse({"output_text": output_text})

def query_and_output(request):
    global output_text

    # Get the IP host from the environment variable
    callme_host = os.environ.get("CALL_ME_HOST")
    ec2_ip = os.environ.get("HOST_IP")

    try:
        # Make the HTTP POST request
        url = f"{callme_host}"
        payload = {"url": f"http://{ec2_ip}/hello"}
        response = requests.post(url, json=payload)
        response_data = response.json()

    except (requests.RequestException, ValueError, KeyError) as e:
        # Handle request errors or JSON decoding errors
        output_text = ""

    return JsonResponse({"output_text": output_text})


