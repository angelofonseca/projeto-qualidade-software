from playwright.sync_api import Page, expect

class CheckoutPage:
    URL_LOGIN = "https://local-eats-unisenac.vercel.app/static/login.html"

    def __init__(self, page: Page) -> None:
        self.page = page

        self.campo_email = page.get_by_role(
            "textbox", name="teste@teste.com"
        )
        self.campo_senha = page.get_by_role(
            "textbox", name="Sua senha secreta"
        )
        self.botao_entrar = page.locator("#loginForm").get_by_role(
            "button", name="Entrar"
        )
        self.botao_adicionar_item = page.get_by_role(
            "button", name=" Adicionar"
        ).first
        self.botao_finalizar_pedido = page.get_by_role(
            "button", name="Finalizar Pedido"
        )
        self.botao_ver_detalhes = page.get_by_role(
            "button", name="Ver Detalhes"
        )

    def acessar_pagina_de_login(self) -> None:
        """Abre a tela de login do LocalEats."""
        self.page.goto(self.URL_LOGIN)

    def fazer_login(self, email: str, senha: str) -> None:
        """Realiza o login com as credenciais fornecidas."""
        self.campo_email.fill(email)
        self.campo_senha.fill(senha)
        self.botao_entrar.click()

    def escolher_restaurante(self, nome: str) -> None:
        """Abre o cardápio do restaurante com o nome especificado."""
        self.page.get_by_role("link", name=nome).click()

    def adicionar_primeiro_item_ao_carrinho(self) -> None:
        """Adiciona o primeiro item disponível do cardápio ao carrinho."""
        self.botao_adicionar_item.click()

    def finalizar_pedido(self) -> None:
        """Conclui o pedido."""
        self.botao_finalizar_pedido.click()

    def validar_pedido_realizado(self) -> None:
        expect(self.botao_ver_detalhes).to_be_visible()
