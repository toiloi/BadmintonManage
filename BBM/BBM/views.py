from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import Promotion

def get_promotions(request):
    promotions = list(Promotion.objects.values())
    return JsonResponse(promotions, safe=False)

@csrf_exempt
def add_promotion(request):
    if request.method == "POST":
        data = json.loads(request.body)
        promo_code = data.get("promo_code")
        discount = data.get("discount")
        
        if promo_code and discount:
            promo = Promotion.objects.create(promo_code=promo_code, discount=discount)
            return JsonResponse({"message": "Khuyến mãi đã được thêm!", "id": promo.id}, status=201)
        return JsonResponse({"error": "Dữ liệu không hợp lệ!"}, status=400)
