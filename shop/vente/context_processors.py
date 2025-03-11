def panier_count(request):
    if "panier" not in request.session:
        request.session["panier"] = []
    panier = request.session["panier"]
    nombre = len(panier)
    return {'nombre': nombre}