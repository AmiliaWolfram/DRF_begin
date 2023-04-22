from app.models import *
c1 = Category(name="Goods")
c1.save()
c2 = Category(name="Soap-washing")
c2.save()
p1 = Product(name="Bread", price=20, category=c1)
p1.save()
Product.objects.all()
<QuerySet [<Product: Bread>]>
p2 = Product.objects.create(name="Water", price=45, category=c1)
p3 = Product.objects.create(name="Soap detergent", price=150, category=c2)
p4 = Product.objects.create(name="Detergent", price=320, category=c2)
p5 = Product.objects.create(name="Shampoo", price=500, category=c2)