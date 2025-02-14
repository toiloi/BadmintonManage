from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import VIPCustomer, Payment, Revenue, Court, Promotion 

def get_vip_customers(request):
    vip_customers = list(VIPCustomer.objects.values())
    return JsonResponse(vip_customers, safe=False)

def get_payments(request):
    payments = list(Payment.objects.values())
    return JsonResponse(payments, safe=False)

def get_revenue(request):
    revenue = Revenue.objects.aggregate(
        total_revenue=sum([r.total_revenue for r in Revenue.objects.all()]),
        total_bookings=sum([r.total_bookings for r in Revenue.objects.all()])
    )
    return JsonResponse(revenue)

def vip_page(request):
    vip_customers = VIPCustomer.objects.all()
    return render(request, "vip.html", {"vip_customers": vip_customers})

def payment_page(request):
    return render(request, "payment.html")

def report_page(request):
    return render(request, "report.html")

def get_promotions(request):
    """API lấy danh sách khuyến mãi"""
    promotions = list(Promotion.objects.values())
    return JsonResponse(promotions, safe=False)

@csrf_exempt  # ⚠️ Nếu có thể, hãy dùng CSRF token thay vì exempt
def add_promotion(request):
    """API thêm khuyến mãi mới"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            promo_code = data.get("promo_code")
            discount = data.get("discount")

            # Kiểm tra dữ liệu hợp lệ
            if not promo_code or not discount:
                return JsonResponse({"error": "Thiếu mã khuyến mãi hoặc giảm giá!"}, status=400)
            if not isinstance(discount, (int, float)) or discount < 0:
                return JsonResponse({"error": "Giảm giá phải là số dương!"}, status=400)

            # Tạo mới khuyến mãi
            promo = Promotion.objects.create(promo_code=promo_code, discount=discount)
            return JsonResponse({"message": "Khuyến mãi đã được thêm!", "id": promo.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Dữ liệu không hợp lệ!"}, status=400)

    return JsonResponse({"error": "Phương thức không được hỗ trợ!"}, status=405)

