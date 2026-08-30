# Arquitetura do Sistema — CRM Sales Management

## 1. Objetivo

O CRM Sales Management será desenvolvido utilizando uma arquitetura modular, organizada em camadas e preparada para futura expansão.

O sistema será executado inicialmente em ambiente local, mas a arquitetura deverá permitir posteriormente sua implantação em um servidor e utilização por múltiplos usuários.

A arquitetura busca priorizar:

- Segurança.
- Organização.
- Manutenibilidade.
- Testabilidade.
- Escalabilidade.
- Separação de responsabilidades.

---

## 2. Arquitetura Geral

A aplicação será dividida inicialmente em três componentes principais:

```text
┌─────────────────────────────┐
│          Frontend           │
│                             │
│  Interface do CRM / Kanban  │
│  Dashboard / Formulários    │
└──────────────┬──────────────┘
               │
               │ HTTP / REST API
               ▼
┌─────────────────────────────┐
│          Backend            │
│                             │
│           Python            │
│          FastAPI            │
│                             │
│ API / Services / Security   │
└──────────────┬──────────────┘
               │
               │ SQLAlchemy
               ▼
┌─────────────────────────────┐
│          Database           │
│                             │
│         PostgreSQL          │
└─────────────────────────────┘