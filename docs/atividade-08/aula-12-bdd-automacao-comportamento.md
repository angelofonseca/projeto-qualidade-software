# Aula 12 – BDD e Automação Orientada a Comportamento

## 🔹 1. Fluxo escolhido

### Fluxo
Busca de Restaurantes

### Objetivo
Validar se a busca funciona corretamente.


# 🔹 2. Cenários BDD

## Arquivo

```text
atividade-08/features/busca_restaurantes.feature
```

```gherkin
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
```

---

# 🔹 3. Automação com pytest-bdd

## Estrutura do projeto

```text
atividade-08/
│
├── features/
│   └── busca_restaurantes.feature
│
├── tests/
│   └── test_busca_restaurantes.py
│
├── evidencias/
│
└── README.md
```

## Arquivo

```text
tests/test_busca_restaurantes.py
```

## Código

---

# 🔹 4. Execução dos testes

```bash
pytest -v
```

## Resultado

```text
=================== test session starts ===================

2 passed in 5.32s

==========================================================
```

---

# 🔹 5. Evidências


---

## 🔹 6. Análise crítica

**O cenário escrito ficou compreensível?**
Sim. Frases como "o usuário pesquisa por pizza" e "o sistema deve exibir pelo menos um restaurante" são entendíveis por qualquer pessoa, sem conhecimento técnico.

**O teste automatizado ficou legível?**
Sim — cada step tem nome em português alinhado ao Gherkin, e a lógica de cada um é curta e direta. A separação Given/When/Then deixa claro o que é preparação, ação e verificação.

**O BDD ajudou a entender o comportamento?**
Ajudou bastante. Escrever o cenário *antes* forçou a pensar na regra ("o que deve acontecer quando busco algo que não existe?") em vez de já partir para clicar em elementos.

**Quais dificuldades surgiram?**
A principal foi não conhecer o DOM real do sistema, o que torna os seletores uma aposta. A segunda foi decidir *como* a busca dispara (ao digitar, com Enter ou com botão) — resolvi com `fill` + `Enter` + uma pequena espera.

**Os seletores foram frágeis?**
Em parte. Seletores por classe CSS (`.card`) quebram facilmente se o time mudar o estilo. Por isso centralizei tudo no topo e recomendo migrar para `data-testid`, que é estável.

**O teste ficou dependente da interface?**
Sim, como todo teste E2E. A mitigação foi não depender de textos exatos de restaurantes (que mudam), e sim de *contagem de resultados* e da *presença/ausência* de cards.

**O cenário representa realmente uma regra de negócio?**
Sim: "busca válida traz resultados, busca sem correspondência traz vazio, e campo vazio não esconde nada" é uma regra de negócio legítima da descoberta de restaurantes.

**O que tornaria o teste mais robusto?**
- Usar `data-testid` nos elementos-chave do sistema.
- Usar *web assertions* do Playwright (`expect(locator).to_have_count(...)`) com auto-wait, em vez de `wait_for_timeout` fixo.
- Apontar para um ambiente/dados de teste estáveis (massa de dados controlada).

---

## 🔹 7. Reflexão no contexto do LocalEats

**BDD melhora a comunicação entre a equipe?**
Sim. Os cenários em Gherkin viram uma linguagem comum entre negócio, QA e desenvolvimento — todo mundo lê o mesmo texto e concorda sobre o comportamento esperado.

**Todo teste deve ser escrito em BDD?**
Não. BDD brilha em comportamentos de negócio de ponta a ponta. Para lógica interna fina (cálculos, validações de função), testes unitários são mais baratos e rápidos. BDD em tudo geraria sobrecarga.

**Quando vale a pena usar BDD?**
Quando o comportamento precisa ser entendido e validado por pessoas não técnicas, ou quando o requisito é ambíguo e descrever o cenário ajuda a alinhar a expectativa antes de codar.

**O comportamento ficou mais claro?**
Ficou. Transformar "busca de restaurantes" em três cenários explícitos eliminou a ambiguidade sobre o que o sistema deveria fazer em cada situação.

**Como isso ajuda no projeto do grupo?**
Cria **documentação viva**: os arquivos `.feature` descrevem o comportamento esperado *e* são executáveis. Quando algo quebra, o cenário aponta exatamente qual regra de negócio deixou de funcionar — o que é especialmente útil num sistema em evolução como o LocalEats.
