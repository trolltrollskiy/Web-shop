from .models import Cart
from django.db import models


def recalc_cart(cart):
    try:
        cart_data = cart.products.aggregate(models.Sum('final_price'), models.Count('id'))
        if cart_data.get('final_price__sum'):
            cart.final_price = cart_data['final_price__sum']
        else:
            cart.final_price = 0
        print(cart_data)
        cart.total_products = cart_data['id__count']
    except:
        pass
    cart.save()


def get_shildren(qs_children):
    res = []
    for comment in qs_children:
        c = {
            'id': comment.id,
            'text': comment.text,
            'timestamp': comment.timestamp.strftime('%Y-%m-%d %H:%m'),
            'author': comment.author,
            'parent_id': comment.get_parent
        }
        if comment.comment_children.exists():
            c['children'] = get_shildren(comment.comment_children.all())
        res.append(c)
    return res


def create_comments_tree(qs):
    res = []
    for comment in qs:
        c = {
            'id': comment.id,
            'text': comment.text,
            'timestamp': comment.timestamp.strftime('%Y-%m-%d %H:%m'),
            'author': comment.author,
            'parent_id': comment.get_parent
        }
        if comment.comment_children:
            c['children'] = get_shildren(comment.comment_children.all())
        if not c['parent_id']:
            res.append(c)
    return res