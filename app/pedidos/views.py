from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import  ListView
from django.views.generic import DetailView
from .models import Pedido, LineaPedido
from carrito.carrito import Carrito


# Create your views here.
@login_required(login_url='/autenticacion/acceder')
def procesar_pedido(request):
    pedido = Pedido.objects.create(usuario_id=request.user.id, completado=True)
    carrito = Carrito(request)
    lineaspedidos = list()
    for key, value in carrito.carrito.items():
        lineaspedidos.append(
            LineaPedido(
                producto_id=key,
                cantidad=value["cantidad"],
                pedido=pedido
            )
        )
    LineaPedido.objects.bulk_create(lineaspedidos)

    enviar_email_pedido(
        pedido=pedido,
        lineaspedidos=lineaspedidos,
        username=request.user.username,
        email_usuario=request.user.email
    )

    messages.success(request, "El pedido se ha credo correctamente")
    return redirect("list_products")


def enviar_email_pedido(**kwargs):
    subject = "Gracias por tu pedido"
    html_message = render_to_string("emails/nuevo_pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineaspedidos": kwargs.get("lineaspedidos"),
        "username": kwargs.get("username")
    })

    plain_message = strip_tags(html_message)
    from_email = "gudyblancoyhogar@gmail.com"
    to = kwargs.get("email_usuario")
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

class listapedido(ListView):
    model = Pedido
    ordering = ['-id']
    template_name = "pedidos/listado.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario_id=self.request.user.id)

class detallepedido(DetailView):
    model = Pedido
    template_name = "pedidos/detallepedido.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario_id=self.request.user.id)