Feature: Busca de restaurantes
  Como um usuário do LocalEats
  Quero pesquisar restaurantes por nome ou tipo de culinária
  Para encontrar rapidamente um lugar para comer

  Scenario: Busca válida retorna resultados
    Given que o usuário está logado e está na página inicial do LocalEats
    When o usuário pesquisa por "Centro"
    Then o sistema deve exibir pelo menos um restaurante

  Scenario: Busca por termo inexistente retorna lista vazia
    Given que o usuário está na página inicial do LocalEats
    When o usuário pesquisa por "Fast Food"
    Then o sistema não deve exibir nenhum restaurante

  Scenario: Campo de busca vazio mantém a listagem completa
    Given que o usuário está na página inicial do LocalEats
    When o usuário realiza uma busca com o campo vazio
    Then o sistema deve manter a listagem completa de restaurantes
