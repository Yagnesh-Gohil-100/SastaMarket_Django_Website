from django.contrib import admin
from .models import Customer, Category, Product, Order, Cart, Review, Wishlist, Coupon, ProductImage

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(Coupon)
admin.site.register(ProductImage)
