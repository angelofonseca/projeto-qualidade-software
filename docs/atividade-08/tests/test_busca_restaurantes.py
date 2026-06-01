from pytest_bdd import scenarios, given, when, then

scenarios('../features/busca_restaurantes.feature')

@given('que o usuário está na página inicial do LocalEats')   # texto IGUAL ao da feature
def acessar_pagina(page):
    page.goto('https://local-eats-unisenac.vercel.app/')

@when('o usuário busca por "Centro" na barra de pesquisa')
def busca_restaurantes(page):
    page.get_by_placeholder("Buscar").fill("Centro")
    page.get_by_role("button", name="Buscar").click()

@then('o sistema exibe pelo menos um restaurante com essa localidade')
def retorna_restaurantes(page):
    assert page.get_by_role("heading", name="Restaurante").count() > 0