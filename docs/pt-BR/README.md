# AISDD em Português

AISDD significa **AI Spec-Driven Development Framework**.

É um framework universal para desenvolver projetos de software com ajuda de Inteligência Artificial de forma mais previsível, rastreável e segura.

A ideia central é simples:

> A conversa com a IA é temporária.  
> O repositório é a fonte da verdade.

## Por que isso importa

Projetos longos feitos com IA costumam sofrer com:

- perda de contexto entre sessões;
- consumo alto de tokens;
- respostas alucinadas;
- regras de negócio inventadas;
- arquivos reescritos sem necessidade;
- regressões;
- falta de histórico de decisões;
- dificuldade para trocar de IA no meio do projeto.

O AISDD existe para evitar esse caos.

## Para quem serve

AISDD é útil para:

- desenvolvedores solo;
- equipes pequenas;
- projetos de longo prazo;
- projetos criados com ChatGPT, Claude, Gemini, Cursor, Windsurf, Copilot ou agentes locais;
- sistemas internos de empresas;
- apps, sistemas web, APIs, desktop apps e automações;
- qualquer projeto em que continuidade, documentação e controle importem.

## Comece por aqui

Escolha seu caso:

| Situação | Caminho recomendado |
|---|---|
| Tenho só uma ideia | Use o Project Definition Wizard |
| Já tenho um projeto | Use o Quick Start |
| Quero entender o método completo | Leia o manifesto e o guia de início |
| Quero validar se funciona na prática | Use as métricas de dogfooding |

Links principais:

- [`../PROJECT_DEFINITION.md`](../PROJECT_DEFINITION.md)
- [`../QUICK_START.md`](../QUICK_START.md)
- [`../GETTING_STARTED.md`](../GETTING_STARTED.md)
- [`../../framework/AISDD_MANIFESTO.md`](../../framework/AISDD_MANIFESTO.md)
- [`../DOGFOODING_METRICS.md`](../DOGFOODING_METRICS.md)

## Caminho mais simples para um projeto existente

Copie os templates de documentação para seu projeto:

```bash
mkdir -p docs
cp -R templates/docs/* seu-projeto/docs/
```

Depois preencha apenas quatro arquivos no começo:

| Arquivo | Para que serve |
|---|---|
| `docs/00_PROJECT_RULES.md` | Regras permanentes, stack, convenções e mudanças proibidas |
| `docs/04_NEXT_TASK.md` | Uma única tarefa executável |
| `docs/07_HANDOFF.md` | Resumo curto para continuidade entre sessões |
| `docs/09_FILE_INDEX.md` | Mapa dos principais arquivos e responsabilidades |

Os outros arquivos podem ficar com `TODO` no início.

## Prompt inicial recomendado

Use este prompt na IA escolhida:

```txt
Este projeto segue o AISDD.
Leia docs/START_HERE.md primeiro.
Execute apenas docs/04_NEXT_TASK.md.
Não invente arquivos, contratos, schemas, endpoints, tabelas ou regras de negócio.
Se faltar informação crítica, responda MISSING INFO.
Atualize a documentação afetada e docs/07_HANDOFF.md antes de finalizar.
```

## Começando só com uma ideia

Se o projeto ainda não existe, use o prompt:

```txt
templates/prompts/PROJECT_DEFINITION_WIZARD_PROMPT.md
```

A IA deve:

- fazer perguntas práticas;
- entender o problema;
- identificar usuários;
- mapear funcionalidades iniciais;
- registrar dúvidas e desconhecidos;
- gerar os documentos AISDD iniciais;
- definir a primeira tarefa pequena em `04_NEXT_TASK.md`.

## Níveis de adoção

| Nível | Quando usar | Esforço |
|---|---|---|
| Definition | Você tem só uma ideia | Responder perguntas guiadas |
| Starter | Você quer controle rápido | Preencher 4 arquivos |
| Standard | O projeto vai durar semanas ou meses | Completar os docs aos poucos |
| Mature | Várias IAs ou pessoas trabalham no projeto | ADRs, testes, métricas e validação |

## Regra anti-alucinação

A IA deve separar sempre:

- **FACTS** — fatos observados diretamente;
- **ASSUMPTIONS** — hipóteses assumidas;
- **UNKNOWNS** — informações ausentes;
- **RISKS** — riscos e possíveis regressões.

A IA não deve inventar silenciosamente:

- arquivos;
- módulos;
- tabelas;
- endpoints;
- contratos;
- regras de negócio;
- decisões de arquitetura;
- resultados de testes.

## Quando usar MISSING INFO

Se faltar uma informação crítica, a IA deve parar e responder:

```txt
MISSING INFO
```

Mas nem toda dúvida deve travar o trabalho.

| Tipo de informação ausente | Ação correta |
|---|---|
| Crítica | Parar com `MISSING INFO` |
| Assumível | Seguir com hipótese explícita |
| Cosmética | Usar padrão simples e documentar se necessário |

## Ciclo AISDD

Cada ciclo deve seguir:

1. Ler `docs/START_HERE.md`.
2. Carregar apenas o contexto necessário.
3. Executar uma única tarefa.
4. Validar critérios de aceite.
5. Atualizar documentação afetada.
6. Atualizar `docs/07_HANDOFF.md`.
7. Encerrar o ciclo.

## Estrutura universal

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

## Validação prática

O AISDD também recomenda medir se o método funciona de verdade.

Métricas sugeridas:

- taxa de atualização do handoff;
- taxa de atualização do log de decisões;
- estimativa de contexto/tokens;
- fricção do `MISSING INFO`;
- teste de continuidade entre IAs diferentes.

Antes de recalibrar regras centrais, o AISDD recomenda coletar pelo menos:

| Requisito | Mínimo |
|---|---:|
| Tarefas reais concluídas | 10 |
| Tipos diferentes de tarefa | 3 |
| Handoffs de sessão | 3 |
| Decisões estruturais | 2 |
| Teste de troca de IA | 1 |

## Estado desta tradução

Esta página é uma **porta de entrada em português brasileiro**.

Por enquanto, os documentos canônicos principais continuam em inglês para manter compatibilidade open-source internacional.

A tradução completa pode evoluir aos poucos conforme o framework amadurecer.

## Resumo em uma frase

AISDD é um método para fazer a IA desenvolver software com menos contexto perdido, menos alucinação, mais rastreabilidade e mais continuidade entre sessões, ferramentas e pessoas.