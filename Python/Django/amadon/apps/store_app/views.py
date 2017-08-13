from django.shortcuts import render, redirect

# Create your views here.
def test(req):
    return render(req, 'store_app/index.html')

def process(req):
    miniDB = {
        "1" : {"name":"Trousers of Power", "price":"88.05"},
        "2" : {"name":"Hat of Deceipt", "price":"700.00"},
        "3" : {"name":"Socks of Sadness", "price":"10.05"},
        "4" : {"name":"Brazire of Misdirection", "price":"40"},   
    }

    productID = req.POST["productID"]
    product = miniDB[productID]

    req.session["pQuant"] = req.POST["quantity"]
    req.session["pTitle"] = product["name"]
    req.session["pPrice"] = product["price"]
    req.session["pTotal"] = float(req.POST["quantity"]) * float(product["price"])

    try :
        req.session["totalPrice"] += req.session["pTotal"]
        req.session["totalOrders"] += 1
    except :
        req.session["totalPrice"] = req.session["pTotal"]
        req.session["totalOrders"] = 1

    print "-------> Product '{}' ordered. Quanitity {}. Price {}".format(req.session["pTitle"], req.session["pQuant"], req.session["pPrice"])
    return redirect('/purchase')

def complete(req):
    return render(req, 'store_app/complete.html')

def reset(req):
    del req.session["pQuant"]
    del req.session["pTitle"]
    del req.session["pPrice"] 
    del req.session["pTotal"]
    del req.session["totalPrice"]
    del req.session["totalOrders"]
    return redirect('/')