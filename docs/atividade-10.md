# Aula 15 – Modelos de Maturidade

## Integrantes
- Angelo


# 1. Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não |
|-----------|-----|----------|-----|
| Os requisitos são documentados? | | | X |
| Existe controle de mudanças? | | X | |
| Há atividades de teste definidas? | X | | |
| Os defeitos são registrados? | | X | |
| O processo de desenvolvimento é conhecido por toda a equipe? | X | | |
| As tarefas são planejadas e acompanhadas regularmente? | | | X |
| Existe padronização para implementação de funcionalidades? | | X | |
| Os testes são executados antes da entrega das funcionalidades? | X | | |
| Há revisão de código ou validação por outro integrante da equipe? | | | X |
| A equipe utiliza ferramentas para gerenciamento das atividades? | | X | |
| Os artefatos do projeto (requisitos, testes, código) são organizados e versionados? | | X | |
| Existe rastreabilidade entre requisitos e funcionalidades? | | | X |
| A equipe realiza retrospectivas ou reuniões de melhoria? | | | X |
| Existem métricas para acompanhar a qualidade? | | | X |

### Nível de maturidade estimado

Nível do CMMI: 1 ~ 2

Nível do MPS.BR: G

### Justificativa

O projeto começou como um MVP desenvolvido às pressas, com foco na funcionalidade acima de tudo.
<br>
Isso caracteriza um processo nível 1 CMMI.

O único ponto forte da equipe é a prática de testes, que já estão definidos. Hoje, a qualidade é verificada somente nessa etapa.

Por outro lado, faltam praticamente todas as práticas que caracterizariam o nível 2.
<br>
Ex: Controle de mudanças, documentação de requisitos, rastreabilidade...
---

# 2. Lacunas Identificadas

| Lacuna | Impacto |
|---------|----------|
| Foco no MVP | Processo dependente do esforço individual e difícil de escalar |
| Ausência de documentação de requisitos | Falta de organização do processo |
| Ausência de controle de mudanças | Mudanças entram sem avaliação |
| Qualidade verificada somente nos testes | Defeitos só aparecem no fim do fluxo, gerando retrabalho |
| Ausência de code review | Aumenta a chance de defeitos passarem despercebidos |
| Sem ferramenta de gestão de tarefas (ex.: Trello) | Tarefas não são planejadas nem acompanhadas regularmente |
| Sem rastreabilidade | Não se sabe qual código atende a qual requisito |
| Sem métricas de qualidade | Impossível medir a evolução da aplicação |

---

# 3. Propostas de Melhoria

| Melhoria | Benefício |
|-----------|-----------|
| Organizar o papel de cada colaborador | Define responsabilidades e dá estrutura à equipe |
| Planejar as tarefas | Tarefas planejadas e acompanhadas regularmente |
| Adotar Code Review via Pull Request | Reduz defeitos e melhora o acompanhamento das tarefas |
| Definir um controle de mudanças | Maior previsibilidade e menos retrabalho |
| Documentar requisitos | Reduz ambiguidade e cria documentação viva |
| Padronizar e organizar o fluxo de trabalho | Processo repetível e conhecido por todos |
| Definir métricas básicas de qualidade | Permite acompanhar a evolução do projeto |

---

## Conclusão

O LocalEats apresenta nível CMMI baixo, entre 1 e 2. Já o MPS.BR é nível G.

A aplicação está funcional, porém, somente com foco no produto e pouca organização de processo.

Adotando gestão de tarefas, code review, controle de mudanças, documentação de requisitos e versionamento organizado, a equipe alcançaria o nível 2. O único ponto positivo que podemos ver é a realização de testes e o pequeno acompanhamento dos mesmos.