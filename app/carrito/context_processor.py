def cart_total_amount(request):
    total = 0.0
    if request.user.is_authenticated:
        for key, value in request.session['carrito'].items():
            total = total + (float(value['precio']) * value['cantidad'])
        return {'cart_total_amount': total}
    else:
        return {'cart_total_amount': 0}
