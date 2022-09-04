from django.urls import path
from django.conf.urls.static import static
from tesi2 import settings
from app1.views import index, contato, cliente, produto, pedido, produto_list

app_name = 'app1'

urlpatterns = [
    path('', index),
    path('contato', contato, name='contato'),
    path('cliente', cliente, name='cliente'),
    path('produto', produto, name='produto'),
    path('pedido', pedido, name='pedido'),
    path('produto_list', produto_list, name='produto_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)