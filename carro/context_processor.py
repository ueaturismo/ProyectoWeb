def importe_total_carro(request):
    total = 0.0 
    if request.user.is_authenticated:
        if 'carro' in request.session:
            for key,value in request.session['carro'].items():
                total = total +float(value['precio'])
    else:
        total="Debes Ingresar"

    return {'importe_total_carro':total}