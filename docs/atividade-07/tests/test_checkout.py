from playwright.sync_api import Page
from pages.checkout_page import CheckoutPage

def test_finalizar_pedido_com_sucesso(page: Page) -> None:
    checkout = CheckoutPage(page)

    checkout.acessar_pagina_de_login()
    checkout.fazer_login(
        email="angelofonseca1997@gmail.com",
        senha="123",
    )
    checkout.escolher_restaurante("Restaurante Sabor 0")
    checkout.adicionar_primeiro_item_ao_carrinho()
    checkout.finalizar_pedido()

    checkout.validar_pedido_realizado()
