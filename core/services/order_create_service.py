from django.db import transaction
from core.models import Customer, CartItem, Order, OrderItem, Cart


@transaction.atomic()
def create_order_from_cart(cart_id, user):
        customer = Customer.objects.get(user=user)
        order = Order(customer=customer)
        order.save()
        cart_items = CartItem.objects.filter(cart_id=cart_id)
                
        order_items = [
            OrderItem(
                order=order,
                product=item.product,
                quantity=item.quantity,
                unit_price=item.product.price
            )
            for item in cart_items
        ]        

        OrderItem.objects.bulk_create(order_items)
        
        Cart.objects.get(pk=cart_id).delete()
        
        return order