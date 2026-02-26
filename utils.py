def segmentation(sales):
    if sales<=3:
        return "bas"
    elif 3<sales<=50:
        return "moyen"
    elif 50<sales<=100:
        return "haut"
    else:
        return "trés haut"