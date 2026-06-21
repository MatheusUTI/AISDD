# Pacotes de Adoção AISDD

O repositório AISDD completo tem muitos arquivos porque ele contém o framework inteiro.

Um projeto que vai usar AISDD não deve copiar tudo de uma vez.

Use apenas o pacote de adoção que resolve sua dor atual.

## Regra principal

```txt
Não copie o repositório inteiro do AISDD para dentro do seu projeto.
Copie apenas o pacote que você precisa agora.
```

AISDD deve ser útil antes de ser completo.

## Qual pacote usar?

| Sua situação | Use este pacote | Objetivo |
|---|---|---|
| Quero começar hoje com mínimo esforço | Core Kit | Controlar a próxima tarefa da IA |
| Tenho um projeto simples já iniciado | Starter Kit | Adotar AISDD sem parar o desenvolvimento |
| Tenho um projeto complexo ou bagunçado | Recovery Kit | Mapear o estado real antes de codar |
| Tenho um projeto com regras importantes | Standard Kit | Manter produto, arquitetura e tarefas alinhados |
| Uso várias IAs, releases ou colaboradores | Mature Kit | Adicionar métricas, manutenção e governança |
| Estou evoluindo o próprio AISDD | Framework Maintainer Layer | Manter o framework sem quebrar usuários |

## Core Kit

Use quando quiser começar hoje.

Crie ou copie apenas:

```txt
docs/
├─ START_HERE.md
├─ 00_PROJECT_RULES.md
├─ 04_NEXT_TASK.md
├─ 07_HANDOFF.md
└─ 09_FILE_INDEX.md
```

Preencha só:

| Arquivo | O que escrever |
|---|---|
| `00_PROJECT_RULES.md` | Stack, regras permanentes, mudanças proibidas |
| `04_NEXT_TASK.md` | Uma única tarefa |
| `07_HANDOFF.md` | Resumo curto para a próxima sessão |
| `09_FILE_INDEX.md` | Arquivos principais e responsabilidades |

Pare aqui se isso já resolver sua dor.

## Starter Kit

Use em projeto existente simples.

Copie:

```txt
templates/docs/ → seu-projeto/docs/
```

Mas preencha primeiro apenas os arquivos do Core Kit.

Deixe o resto como TODO até precisar.

## Recovery Kit

Use em projeto existente complexo, confuso ou já mexido por várias sessões de IA.

A primeira rodada deve ser só leitura e mapeamento.

Documentos iniciais:

```txt
docs/
├─ 00_PROJECT_RULES.md
├─ 03_CURRENT_STATE.md
├─ 04_NEXT_TASK.md
├─ 07_HANDOFF.md
├─ 08_KNOWN_ISSUES.md
└─ 09_FILE_INDEX.md
```

Não refatore na primeira rodada.

Não tente corrigir tudo.

Primeiro descubra o estado real.

## Standard Kit

Use quando o projeto já tiver regras, arquitetura e riscos reais.

Aí sim você evolui para a estrutura completa:

```txt
docs/
├─ START_HERE.md
├─ 00_PROJECT_RULES.md
├─ 01_PRODUCT_SPEC.md
├─ 02_ARCHITECTURE.md
├─ 03_CURRENT_STATE.md
├─ 04_NEXT_TASK.md
├─ 05_ACCEPTANCE_CHECKS.md
├─ 06_DECISIONS_LOG.md
├─ 07_HANDOFF.md
├─ 08_KNOWN_ISSUES.md
├─ 09_FILE_INDEX.md
├─ 10_TEST_CHECKLIST.md
└─ 11_TEST_STRATEGY.md
```

Mas não preencha com chute.

Desconhecidos podem ficar como `UNKNOWNS` ou `TODO`.

## Mature Kit

Use quando o projeto ficar longo, tiver releases, múltiplas IAs ou colaboradores.

Adicione:

- métricas de dogfooding;
- Prompt Maturity Levels;
- auditoria de documentação;
- scripts de verificação;
- governança de mudanças.

## O que não fazer

Não faça:

- copiar o repositório inteiro do AISDD;
- preencher todos os documentos com suposições;
- usar Mature Kit antes do Core funcionar;
- misturar Recovery com refatoração na primeira tarefa;
- tratar exemplos e tutoriais como arquivos obrigatórios do seu projeto.

## Caminhos práticos

### Projeto novo pequeno

```txt
Core Kit → Starter Kit → Standard Kit se precisar
```

### Projeto existente simples

```txt
Starter Kit → Standard Kit se precisar
```

### Projeto existente bagunçado

```txt
Recovery Kit → Starter Kit → Standard Kit
```

### Projeto cheio de regra de negócio

```txt
Recovery Kit → Standard Kit → Mature Kit
```

## Regra final

AISDD deve reduzir a confusão da próxima tarefa.

Comece pelo menor pacote que faz isso acontecer.