# Arquitetura Conceitual

Este documento descreve a arquitetura inicial planejada para o projeto **Ia-Vet-Doc**.

O objetivo é criar um fluxo capaz de receber documentos veterinários, organizar o conteúdo em partes menores e permitir consultas contextualizadas com apoio de modelos de linguagem.

---

## Visão geral do fluxo

```mermaid
flowchart TD
    A[Documento veterinário] --> B[Extração do texto]
    B --> C[Limpeza e organização]
    C --> D[Divisão em trechos]
    D --> E[Armazenamento dos trechos]
    E --> F[Consulta do usuário]
    F --> G[Busca dos trechos relevantes]
    G --> H[Envio do contexto para o modelo de linguagem]
    H --> I[Resposta estruturada]
    I --> J[Revisão humana]
