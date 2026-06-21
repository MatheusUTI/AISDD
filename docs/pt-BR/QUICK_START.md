# AISDD Quick Start em Português

Adote o AISDD sem parar o desenvolvimento do projeto.

O objetivo não é documentar tudo antes de programar.

O objetivo é dar à IA contexto persistente suficiente para trabalhar com segurança.

## Caminho de 5 minutos

### 1. Copie o template de documentação

A partir do repositório AISDD, copie:

```txt
templates/docs/
```

Para dentro do seu projeto como:

```txt
docs/
```

### 2. Preencha apenas quatro arquivos primeiro

Você não precisa completar todos os documentos antes de usar o AISDD.

Comece com:

| Arquivo | O que escrever |
|---|---|
| `00_PROJECT_RULES.md` | Stack, mudanças proibidas, convenções permanentes |
| `04_NEXT_TASK.md` | Uma tarefa clara e única |
| `07_HANDOFF.md` | Resumo curto do estado atual |
| `09_FILE_INDEX.md` | Principais arquivos e o que cada um faz |

Deixe os outros arquivos com `TODO` até que eles sejam necessários.

### 3. Use um prompt inicial

```txt
Este projeto segue o AISDD.
Leia docs/START_HERE.md primeiro.
Execute apenas docs/04_NEXT_TASK.md.
Não invente arquivos, contratos, endpoints, tabelas ou regras de negócio.
Se faltar informação crítica, responda MISSING INFO.
Atualize a documentação afetada e docs/07_HANDOFF.md antes de finalizar.
```

### 4. Mantenha cada ciclo pequeno

Boa tarefa:

```txt
Adicionar validação ao formulário de cliente.
```

Tarefa ruim:

```txt
Refatore o app, melhore a UI, adicione autenticação, corrija bugs e otimize tudo.
```

## Regra Starter

AISDD Starter significa:

- copiar a estrutura completa de docs;
- preencher apenas o mínimo necessário;
- executar uma tarefa;
- atualizar o handoff;
- melhorar a documentação aos poucos.

## Quando preencher os outros documentos

| Documento | Preencha quando |
|---|---|
| `01_PRODUCT_SPEC.md` | As regras do produto começarem a importar |
| `02_ARCHITECTURE.md` | Existirem múltiplos módulos ou contratos |
| `03_CURRENT_STATE.md` | O projeto já tiver implementação relevante |
| `05_ACCEPTANCE_CHECKS.md` | Regressões começarem a ser risco |
| `06_DECISIONS_LOG.md` | Uma decisão estrutural for tomada |
| `08_KNOWN_ISSUES.md` | Surgirem bugs ou limitações recorrentes |
| `10_TEST_CHECKLIST.md` | Você precisar de checagens manuais repetíveis |
| `11_TEST_STRATEGY.md` | Testes automatizados ou release começarem a importar |

## Ciclo mínimo

Para cada tarefa:

1. Atualize `04_NEXT_TASK.md`.
2. Peça para a IA executar a tarefa.
3. Revise o resultado.
4. Atualize `07_HANDOFF.md`.
5. Faça commit.

## Promessa principal

AISDD deve tornar o desenvolvimento com IA mais seguro sem virar burocracia pesada.