# Roadmap

Este documento organiza as etapas de evolução do projeto **Ia-Vet-Doc**.

O objetivo é desenvolver o projeto de forma gradual, começando pela documentação e por um protótipo simples, até chegar a uma solução com processamento de documentos, consulta contextual e integração com modelos de linguagem.

---

## Fase 1 — Estruturação inicial

- [x] Criar repositório no GitHub;
- [x] Criar README do projeto;
- [x] Definir problema central;
- [x] Documentar arquitetura conceitual;
- [ ] Criar roadmap técnico;
- [ ] Criar exemplo fictício de documento veterinário;
- [ ] Criar prompt inicial para consulta de documentos.

---

## Fase 2 — Protótipo local em Python

Nesta fase, o foco será criar um script simples para simular o fluxo inicial do projeto.

### Objetivos

- Receber um texto veterinário fictício;
- dividir o conteúdo em trechos menores;
- permitir busca por palavra-chave;
- retornar os trechos mais relevantes;
- organizar a resposta de forma simples.

### Entregáveis

- Arquivo `src/prototipo.py`;
- documento fictício em `exemplos/exemplo-laudo-ficticio.md`;
- comentários no código explicando cada etapa;
- atualização do README com instruções de uso.

---

## Fase 3 — Organização de documentos-fonte

Nesta fase, o projeto deverá evoluir para lidar melhor com textos técnicos.

### Objetivos

- Padronizar entrada de documentos;
- organizar seções como histórico, achados, conclusão e observações;
- identificar informações relevantes no texto;
- separar dados encontrados de interpretações;
- manter foco em revisão humana.

### Entregáveis

- Funções para limpeza de texto;
- funções para separação em trechos;
- arquivo de exemplo com documento estruturado;
- documentação do fluxo.

---

## Fase 4 — Consulta contextual

Nesta fase, o projeto deverá simular uma consulta mais próxima de um fluxo RAG.

### Objetivos

- Receber uma pergunta do usuário;
- buscar trechos relacionados ao tema da pergunta;
- montar um contexto com base no documento;
- preparar o conteúdo para envio a um modelo de linguagem;
- evitar respostas sem base no documento original.

### Entregáveis

- Busca por termos relevantes;
- organização de contexto;
- prompt estruturado;
- exemplos de perguntas e respostas esperadas.

---

## Fase 5 — Integração com API

Nesta fase, o projeto poderá ser conectado a uma API de modelo de linguagem.

### Objetivos

- Enviar contexto e pergunta para uma API externa;
- receber uma resposta estruturada;
- controlar instruções do sistema;
- registrar limitações e cuidados;
- evitar exposição de dados sensíveis.

### Entregáveis

- Arquivo de configuração;
- exemplo de chamada de API;
- tratamento básico de erros;
- instruções de segurança para uso de chaves.

---

## Fase 6 — Evolução para backend

Nesta fase, o projeto poderá ganhar uma API própria.

### Tecnologias possíveis

- Node.js;
- JavaScript ou TypeScript;
- API REST;
- rotas para envio de documentos;
- rotas para consulta;
- armazenamento de trechos.

### Possíveis endpoints

- `POST /documentos`
- `GET /documentos`
- `GET /documentos/:id`
- `POST /consultas`

---

## Fase 7 — Interface web simples

Nesta fase, o projeto poderá receber uma interface para facilitar o uso.

### Funcionalidades possíveis

- Campo para inserir documento;
- campo para pergunta;
- botão para consultar;
- área para resposta;
- aviso de revisão humana;
- histórico simples de consultas.

---

## Prioridades atuais

As próximas tarefas do projeto são:

1. Criar exemplo fictício de documento veterinário;
2. criar prompt inicial para consulta;
3. criar protótipo em Python;
4. simular busca por palavra-chave;
5. documentar o funcionamento no README.

---

## Observação

Este projeto tem finalidade educacional e de portfólio.

Ele não substitui avaliação profissional, não realiza diagnóstico automático e deve ser usado apenas como demonstração técnica de organização de documentos, automação e consulta assistida.
