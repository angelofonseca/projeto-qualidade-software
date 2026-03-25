# Estratégia Inicial de Testes – LocalEats

## 1. Funcionalidades
- Login
- Pesquisa com filtros
- Visualizar cardápio
- Favoritar e comentar restaurantes
- Recomendações de conteúdo com base no perfil do usuário

---

## 2. Níveis de Teste

### Funcionalidade: Login
- Unitário: validar senha e campos obrigatórios
- Integração: verificar comunicação com banco
- Sistema: usuário faz login completo
- Aceitação: usuário entra no sistema sem erro

### Funcionalidade: Pesquisa com filtros
- Unitário: valida se filtro específico retorna corretamente
- Integração: testa a requisição de busca
- Sistema: Usuário acessa o campo de busca e filtros, adiciona filtro, confirma busca, o sistema faz a busca e retorna dados de acordo.
- Aceitação: buscar restaurantes, filtrar por categoria, melhores avaliados, destaques, nome.

### Funcionalidade: Visualizar cardápio
- Unitário: Testa se após selecionar restaurante e o cardápio, disponibiliza página do cardápio.
- Integração: Testa se ao selecionar um restaurante, é enviada uma requisição para a API solicitando informações do restaurante, como o cardápio.
- Sistema: Usuário pesquisa e acessa um restaurante, o sistema faz a busca e mostra a página do restaurante, usuário acessa a aba de cardápio e o cardápio é disponibilizado.
- Aceitação: Visualizar cardápio, informações adicionais sobre os pratos do restaurante, preços.

### Funcionalidade: Favoritar e comentar restaurantes
- Unitário: Testa se a função de adicionar comentário salva corretamente o texto e associa ao restaurante e ao usuário.
- Integração: Testa se ao comentar ou favoritar, a aplicação envia os dados corretamente para a API e salva no banco de dados.
- Sistema: Usuário acessa um restaurante, adiciona um comentário e/ou favorita, o sistema registra e exibe o comentário na página do restaurante.
- Aceitação: Usuário consegue comentar em restaurantes, visualizar comentários de outros usuários e favoritar restaurantes.

### Funcionalidade: Recomendações com base no perfil do usuário
- Unitário: Testa se o algoritmo de recomendação retorna restaurantes com base nas preferências do usuário (ex: histórico).
- Integração: Testa se o sistema coleta corretamente os dados do usuário (histórico, favoritos) e envia para o serviço de recomendação.
- Sistema: Usuário acessa a plataforma, o sistema analisa seu perfil e exibe recomendações personalizadas na tela inicial.
- Aceitação: Usuário recebe sugestões de restaurantes relevantes com base em seu perfil, histórico e preferências.

---

## 3. Prioridades e Riscos

Alta prioridade:
- Login → sem o login, o usuário não armazena dados e não consegue fazer diversas ações

- Pesquisa de busca → Sem ela o usuário não consegue procurar um restaurante.
- Cardápio → Sem o cardápio o usuário não visualiza informações básicas.

Justificativa:
Falhas nessas áreas impedem que o usuário visualize as informações básicas que o sistema oferece.

Baixa prioridade: 
- Favoritos → não impede uso da aplicação.

Justificativa: Apesar de não conseguir favoritar, não compromete o uso básico da aplicação.

Onde um erro causaria maior impacto?
- Um erro na API da listagem dos restaurantes, é a partir dela que o usuário parte para outras ações, como, visualizar a página inicial e subsequentemente fazer buscas, favoritar, visualizar fotos.

---

## 4. Pirâmide de Testes

- Maior foco: Testes unitários e regras de negócio.
Justificativa: Rápidos de fazer, baratos e fáceis de manter.

- Médio foco: Testes de integração
Justificativa: Validam a comunicação entre diferentes partes do sistema como A API - DB. São mais lentos e complexos que os unitários, mas essenciais para garantir que os módulos funcionem corretamente em conjunto.

- Menor foco: Testes de sistema e aceitação.
Justificativa: Testam a aplicação como um todo e são mais custosos e os de aceitação pois são testes que são possíveis com o uso de usuários, no mundo real.

---

## 5. Testes em Produção

O sistema deveria usar testes em produção?

- Sim

Exemplo 1: testar nova funcionalidade de recomendação e monitorar se a nova funcionalidade realmente se adapta ao usuário.
Exemplo 2: monitorar lentidão e identificar os motivos, para saber se se deve a algum erro no código ou alguma possível melhoria.