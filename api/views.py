import requests
from datetime import datetime, timezone
from django.http import JsonResponse

def me(request):
    try:
        # Fetch cat fact
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        cat_data = response.json()
        cat_fact = cat_data.get("fact", "Cats are mysterious creatures.")
    except Exception as e:
        cat_fact = "Could not fetch cat fact at the moment."

    data = {
        "status": "success",
        "user": {
            "email": "jamicojerahmeel@gmail.com",
            "name": "Jerahmeel Princewill",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return JsonResponse(data, content_type="application/json")
