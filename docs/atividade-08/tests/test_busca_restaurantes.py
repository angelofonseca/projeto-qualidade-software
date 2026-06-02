from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect

scenarios("../features/busca_restaurantes.feature")

EMAIL = "angelofonseca1997@gmail.com"
SENHA = "123"

CARD = "a[href*='restaurant.html']"
BUSCA = "Buscar por culinária ou localização..."


def _fazer_login(page):
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.get_by_role("textbox", name="teste@teste.com").fill(EMAIL)
    page.get_by_role("textbox", name="Sua senha secreta").fill(SENHA)
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    # ESSENCIAL: espera a lista carregar antes de qualquer busca (mata a race condition)
    expect(page.locator(CARD).first).to_be_visible()


@given("que o usuário está logado")
def usuario_logado(page):
    _fazer_login(page)


def _buscar(page, termo: str):
    page.get_by_role("textbox", name=BUSCA).fill(termo)
    page.get_by_role("button", name="Buscar").click()


@when('o usuário pesquisa por "Centro"')
def pesquisa_centro(page):
    _buscar(page, "Centro")


@when('o usuário pesquisa por "Fast Food"')
def pesquisa_fast_food(page):
    _buscar(page, "Fast Food")


@when("o usuário realiza uma busca com o campo vazio")
def pesquisa_vazia(page):
    _buscar(page, "")


@then("o sistema deve exibir pelo menos um restaurante")
def exibe_restaurantes(page):
    expect(page.locator(CARD).first).to_be_visible()


@then("o sistema não deve exibir nenhum restaurante")
def nao_exibe_restaurantes(page):
    expect(page.locator(CARD)).to_have_count(0)


@then("o sistema deve manter a listagem completa de restaurantes")
def mantem_listagem(page):
    expect(page.locator(CARD)).to_have_count(15)