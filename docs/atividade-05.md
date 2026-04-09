# Aula 6 – Planejamento e Execução de Testes


## 1. Plano de Testes

### 1.1 Objetivo

Validar as principais funcionalidades do sistema, garantindo que o usuário consiga utilizá-las.

### 1.2 Escopo

**O que será testado:**

- Listagem de restaurantes
- Busca de restaurantes por localização
- Filtro por categoria
- Navegação entre as páginas
- Favoritar

**O que NÃO será testado:**

- Testes de segurança e performance
- Responsividade
- Integração com sistemas externos

### 1.3 Funcionalidades selecionadas

- Listagem de todos restaurantes
- Busca por categoria
- Busca por localização
- Busca por nome
- Favoritos
- Navegação entre páginas

### 1.4 Estratégia de Testes

- **Tipos de teste aplicados:**
    Funcional, exploratório e de usabilidade.

- **Abordagem:** Testes manuais executados diretamente no navegador em formato Gherkin.

---

## 2. Casos de Teste



### CT-01 – Listagem de todos restaurantes

- **Pré-condição:** Usuário está na logado e na página home.
- **Dados de entrada:** Nenhum.
- **Passos (Gherkin):**

```gherkin
Dado que estou acessando o sistema LocalEats pela primeira vez
Quando a página inicial terminar de carregar
Então o sistema solicita login de usuário
E após realizar o cadastro o usuário é redirecionado para a Home
Então o sistema apresenta a seção Principal
E exibe uma lista de cards de restaurantes disponíveis
```

- **Resultado esperado:** A página carrega em até 5 segundos e exibe uma lista visível de restaurantes, sem mensagens de erro.

---

### CT-02 – Filtrar restaurantes por categoria "Japonesa"

- **Pré-condição:** Usuário logado está na Home Page com a lista de restaurantes carregada.
- **Dados de entrada:** Categoria selecionada = "Japonesa".
- **Passos (Gherkin):**

```gherkin
Dado que estou logado
E que estou na página Home com a lista de restaurantes carregada
Quando eu clicar no filtro de categoria "Japonesa"
Então o sistema apresenta apenas restaurantes da categoria japonesa
E os demais restaurantes não são exibidos na lista
```

- **Resultado esperado:** A lista é atualizada exibindo somente restaurantes japoneses. O filtro selecionado fica visualmente destacado.

---

### CT-03 – Buscar restaurantes por localização

- **Pré-condição:** Estar logado e existir pelo menos um restaurante no "Centro"
- **Dados de entrada:** Termo de busca = "Centro".
- **Passos (Gherkin):**

```gherkin
Dado que estou logado
E que estou na página Explorar
E que o campo de busca está visível
Quando eu digitar "Centro" no campo de busca
E clicar no botão "Buscar"
Então o sistema apresenta apenas restaurantes localizados no Centro
```

- **Resultado esperado:** A lista é filtrada e exibe apenas restaurantes localizados no termo buscado.

---

### CT-04 – Buscar restaurante pelo nome

- **Pré-condição:** Estar logado e na página de Explorar.
- **Dados de entrada:** Termo de busca pelo nome = "Sabor 1".
- **Passos (Gherkin):**

```gherkin
Dado que estou logado
E que estou na página Explorar
Quando eu digitar "Sabor 1" no campo de busca
E clicar no botão "Buscar"
Então o sistema apresenta uma mensagem informando que nenhum restaurante foi encontrado
```

- **Resultado esperado:** Mensagem "Nenhum restaurante encontrado" na tela.

---

### CT-05 – Favoritar e desfavoritar logo após

- **Pré-condição:** Usuário está logado.
- **Dados de entrada:** Nenhum.
- **Passos (Gherkin):**

```gherkin
Dado que estou logado
E que acessei a página de um restaurante
Quando eu clicar em "Favoritar"
Então o sistema carrega e apresenta a mensagem "Favoritado!"
Quando eu clicar em "Favoritado!"
Então o sistema carrega novamente mas não atualiza o estado do botão para Favoritar
```

- **Resultado esperado:** Restaurante fica favoritado "eternamente".

---

## 3. Execução dos Testes

| ID | Resultado (Passou/Falhou) | Evidência (descrição ou print) |
|----|-----------|-----------------------|
| CT-01 | Passou | A home carrega exibindo a seção principal e a lista de restaurantes. |
| CT-02 | Passou | Ao clicar em "Japonesa", a lista é filtrada e mostra apenas restaurantes dessa categoria. O botão fica destacado. |
| CT-03 | Passou | Ao buscar pela zona do restaurante, os restaurantes são filtrados corretamente. |
| CT-04 | Falhou | Ao buscar pelo nome, retorna que nenhum restaurante foi encontrado. |
| CT-05 | Falhou | Ao Favoritar o restaurante, não é possível reverter a alteração na mesma página. |

---

## 4. Análise dos Resultados

- **Total de testes executados:** 5
- **Testes que passaram:** 3
- **Testes que falharam:** 2

### Principais problemas encontrados

Algumas funcionalidades ainda não possuem uma implementação básica, piorando a experiência do usuário.

---

## 5. Reflexão no contexto do LocalEats

**O plano de testes ajudou a organizar melhor os testes?**
Sim. Ao definir escopo e as funcionalidades para testar ficou mais fácil de organizar as ideias.

**Algum problema só foi percebido durante a execução?**
Sim. Os dois teste que falharam só foram percebidos quando testados na prática.

**O que melhorariam no processo de testes?**
Faria testes automatizados e também testes de responsividade do sistema.

---

## 6. Conclusão Geral

O sistema apresenta uma base funcional boa: a navegação entre as páginas, listagem dos restaurantes, e os filtros por categoria respondem corretamente.

Porém, o sistema possui funcionalidades que não estão 100% implementadas, comprometendo a experiência do usuário pois são funcionalidades que possivelmente estão implementadas em grande parte das aplicações.