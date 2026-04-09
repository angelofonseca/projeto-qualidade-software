# 🧪 Aula 5 – Testes Funcionais vs Estruturais  

## 🎯 1. Funcionalidade escolhida

**Funcionalidade selecionada:**  
Busca de restaurantes

**Descrição da funcionalidade:**  
A funcionalidade de busca permite que o usuário pesquise restaurantes com base em nome, tipo de comida ou localização. O sistema retorna uma lista de resultados relevantes conforme os critérios informados.

**O que o usuário espera:**  
O usuário espera encontrar rapidamente restaurantes que correspondam com a sua busca, com resultados corretos, relevantes e organizados.

---

## 🔍 2. Testes Caixa-Preta (Visão do Usuário)

**Quais testes vocês fariam sem conhecer o código?**

### 🔹 Cenários de teste

- Cenário 1:  
  Entrada: Buscar por "pizza"  
  Esperado: Lista de restaurantes que servem pizza

- Cenário 2:  
  Entrada: Buscar por um nome exato de restaurante  
  Esperado: Retorno do restaurante específico

- Cenário 3:  
  Entrada: Campo de busca vazio  
  Esperado: Exibir lista padrão de restaurantes

- Cenário 4:  
  Entrada: Buscar por termo inexistente  
  Esperado: Retorna mensagem de "Nenhum resultado encontrado"

- Cenário 5:  
  Entrada: Buscar por localização (ex: Pelotas)
  Esperado: Listagem dos restaurantes somente de Pelotas

---

### 🔹 Possíveis erros identificados

- Resultados irrelevantes ou incorretos  
- Busca não retornando resultados existentes  
- Sistema demorando muito para responder  
- Erro ao tratar busca vazia 

---

## 🔧 3. Testes Caixa-Branca (Visão do Sistema)

**Como essa funcionalidade poderia estar implementada internamente?**

### 🔹 Lógica hipotética (pseudo-código ou descrição)

```pseudo
função buscarRestaurantes(termo):
    se termo estiver vazio:
        retornar lista de restaurantes populares

    resultados = bancoDeDados.buscar(
        onde nome OU categoria OU localização contém termo
    )

    se resultados estiver vazio:
        retornar "nenhum resultado encontrado"

    ordenar resultados por relevância

    retornar resultados
```

### 🔹 Situações a serem testadas

- **Situação 1:**  
  Verificar se a condição de termo vazio está sendo tratada corretamente  

- **Situação 2:**  
  Validar se a busca no banco usa corretamente os campos (ex: nome, categoria, localização)  

- **Situação 3:**  
  Testar a ordenação (ex: relevância ou proximidade)  

---

### 🔹 Possíveis erros identificados

- Condição de busca mal implementada (ex: não busca em todos os campos)  
- Falha na ordenação dos resultados  
- Problemas de desempenho em consultas ao banco  
- Erros em validações

---

## ⚖️ 4. Comparação entre as abordagens

**Qual a principal diferença entre testar sem ver o código e com acesso ao código?**

A principal diferença é a perspectiva:

- Na caixa-preta é testado o sistema do ponto de vista do usuário, sem acesso a implementação.  
- Na caixa-branca se tem acesso a lógica interna do sistema, verificando como ele foi construído.  

---

**Que tipo de problema cada abordagem ajuda a encontrar?**

**Caixa-preta:**

- Problemas de funcionalidade  
- Erros de comportamento  
- Falhas na experiência do usuário  
- Resultados incorretos visíveis  

**Caixa-branca:**

- Erros na lógica do código  
- Falhas em condições (if/else)  
- Problemas de cobertura de código  
- Bugs internos  

---

## 💡 5. Reflexão no contexto do LocalEats

**Qual abordagem parece mais importante neste momento do projeto?**

A abordagem de caixa-preta, pois o sistema já apresenta problemas visíveis para o usuário, como resultados incorretos e comportamentos inesperados.

---

**Apenas uma abordagem seria suficiente? Por quê?**

Não. A caixa-preta ajuda a identificar os problemas, mas a caixa-branca é necessária para entender a causa deles, logo, as duas abordagens são complementares.

## 🚀 Conclusão

_Resuma o que o grupo aprendeu com a atividade_

A diferença entre testes caixa-preta e caixa-branca. E a importância de utilizar as duas em conjunto.