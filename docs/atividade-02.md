# Diagnóstico de Qualidade – Startup Local Eats

> Disciplina: Qualidade de Software  
> Aula 3 – Papéis, Responsabilidades e Práticas de QA  
> Integrantes: Angelo Fonseca

---

# 1. Diagnóstico da Situação Atual

## 1.1 Papéis atuais identificados

Liste quais papéis vocês acreditam que existem atualmente na startup.

- Desenvolvedor
- Gerente de produto/PO

---

## 1.2 Quem é responsável pela qualidade hoje?

Descreva como vocês acreditam que a qualidade está sendo tratada atualmente.

> Resposta: É provável que o desenvolvedor esteja encarregado da qualidade.

---

## 1.3 Problemas identificados

Liste os principais problemas relacionados à falta de organização da qualidade.

- Erros em produção
- Problemas com a configuração da API (Pedidos duplicados)
- Bugs

---

## 1.4 Impactos desses problemas

Explique quais são as consequências desses problemas para o sistema e para os usuários.

> Resposta: O sistema apresenta que não tem qualidade, além de ser ruim para a experiência do usuário, é ruim para o negócio.

---

## 1.5 A qualidade é responsabilidade de quem?

Explique se a qualidade deve ser responsabilidade de uma pessoa ou de toda a equipe.

> Resposta: Depende. Neste caso, como não tem uma pessoa encarregada de realizar testes de qualidade, deveria ser responsabilidade da equipe. Mas também se pode ter uma única pessoa ou um setor específico focado em testes e na qualidade do produto.

---

# 2. Papéis da Equipe Propostos

Definam quais papéis deveriam existir na equipe da Local Eats.

---

## 2.1 Lista de papéis

- Desenvolvedor
- QA
- DevOps
- PO

---

## 2.2 Descrição dos papéis

Dev

Responsabilidades:
- Implementar funcionalidades
- Corrigir bugs
- Criar testes automatizados

Relação com qualidade:
- Garantir qualidade do código
- Realizar testes unitários
- Participar de code reviews

---

QA

Responsabilidades:
- Planejar e executar testes
- Identificar e documentar defeitos
- Validar funcionalidades

Relação com qualidade:
- As funcionalidades são testadas pelo analista de qualidade antes de ir para produção.

---

PO

Responsabilidade:
- Priorizar backlog
- Definir valor de negócio

Relação com qualidade:
- Define o que é pronto
- Valida entregas

---

DevOps

Responsabilidades:
- Gerenciar deploy e infraestrutura
- Automatizar pipelines

Relação com qualidade:
- Garante estabilidade em produção
- Evita falhas em deploy


---

# 3. Práticas de QA Sugeridas

Sugira práticas que a startup pode adotar para melhorar a qualidade.

---

## 3.1 Lista de práticas

- testes manuais das funcionalidades
- registro e acompanhamento de bugs
- testes exploratórios
- revisão de funcionalidades antes da entrega
- validação dos requisitos


---

## 3.2 Explicação das práticas

- testes manuais
Consistem em validar manualmente as funcionalidades do sistema, simulando o uso real do usuário.

- registro e acompanhamento de bugs
Envolve documentar erros encontrados.

- testes exploratórios
Testes realizado aonde o testador explora o sistema livremente para encontrar bugs.

- revisão de funcionalidades antes da entrega
Garantia de que a funcionalidade se comporta como o esperado.

- validação dos requisitos
Verifica se os requisitos estão de acordo com as regras de negócio.

---

# 4. Anúncios de Contratação

A startup decidiu contratar novos profissionais. Crie anúncios de vagas.

> Mínimo: 2 vagas

---

## 4.1 Vaga 1 – Analista de Qualidade de Software (QA)

### Descrição da vaga
> A Local Eats busca um Analista de Qualidade para estruturar e fortalecer os processos de QA da plataforma de pedidos online.

### Responsabilidades
- Planejar e executar testes
- Identificar e registrar defeitos
- Criar cenários de teste
- Validar funcionalidades antes da produção


### Requisitos obrigatórios
- Conhecimento básico em testes de software
- Capacidade de análise crítica
- Boa comunicação


### Requisitos desejáveis
- Experiência com testes web
- Conhecimento em automação de testes
- Familiaridade com ferramentas de bug tracking

### Certificações desejáveis
- ISTQB CTFL

---

## 4.2 Vaga 2 – Engenheiro DevOps

### Descrição da vaga
> A Local Eats está em busca de um Engenheiro DevOps para estruturar e automatizar nossos processos de entrega e infraestrutura.

### Responsabilidades
- Implementar e manter pipelines de CI/CD
- Automatizar processos de build, teste e deploy
- Monitorar aplicações em produção
- Garantir alta disponibilidade e desempenho do sistema
- Gerenciar infraestrutura
- Apoiar a equipe na resolução de incidentes
- Trabalhar na prevenção de falhas em produção


### Requisitos obrigatórios
- Conhecimento em Linux
- Experiência com versionamento (Git)
- Noções de redes e infraestrutura
- Conhecimento em integração contínua (CI/CD)
- Capacidade de automação de processos

### Requisitos desejáveis
- Experiência com cloud (AWS)
- Conhecimento em Docker e containers
- Experiência com Kubernetes


### Certificações desejáveis
- AWS Certified DevOps Engineer

---

# 5. Conclusão da Equipe

Descreva brevemente:

- O que a equipe aprendeu com a atividade
- Principais dificuldades encontradas
- Principais melhorias propostas para a startup

> Resposta: A principal dificuldade está no processo de qualidade da startup, ocasionando falhas na aplicação. Dito isso, falta organização e estrutura de equipe para que isso aconteça.
Logo, as principais melhorias são de novos membros para conseguirem lidar com os problemas identificados com qualidade, e a partir disso uma melhor organização do papel de cada colaborador.