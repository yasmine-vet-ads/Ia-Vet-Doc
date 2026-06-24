# Ia-Vet-Doc

Projeto experimental de IA aplicada para organização, consulta e estruturação de documentos veterinários, como laudos, históricos clínicos, artigos, referências técnicas e materiais de apoio à tomada de decisão.

Este projeto faz parte do meu portfólio técnico como estudante de Análise e Desenvolvimento de Sistemas, conectando minha experiência anterior em Medicina Veterinária, Diagnóstico por Imagem, documentação técnica e dados clínicos com desenvolvimento, automação e processamento de documentos.

---

## Objetivo

Criar um protótipo capaz de receber documentos-fonte veterinários, organizar o conteúdo em trechos e permitir consultas assistidas por modelos de linguagem.

A proposta é evoluir o projeto gradualmente, aplicando conceitos como:

- IA aplicada;
- documentos-fonte;
- RAG — Retrieval-Augmented Generation;
- chunking;
- embeddings;
- busca contextual;
- automação de fluxos;
- APIs;
- documentação técnica.

---

## Problema

Na rotina veterinária, muitos dados importantes ficam distribuídos em laudos, históricos clínicos, artigos científicos, protocolos, exames e documentos técnicos.

Isso dificulta a recuperação rápida de informações relevantes e pode tornar processos mais manuais, repetitivos e sujeitos à perda de contexto.

Este projeto propõe explorar como a tecnologia pode apoiar a organização, consulta e estruturação dessas informações, sem substituir a avaliação profissional.

---

## Público-alvo

- Médicos-veterinários;
- estudantes de Medicina Veterinária;
- profissionais de diagnóstico por imagem;
- pesquisadores;
- clínicas e hospitais veterinários;
- projetos de HealthTech, VetTech e inovação aplicada.

---

## Status do projeto

🚧 Projeto em desenvolvimento.

Atualmente, o repositório possui:

- documentação inicial do problema;
- arquitetura conceitual;
- roadmap técnico;
- exemplo fictício de documento veterinário;
- prompt inicial para consulta de documentos;
- protótipo simples em Python.

---

## Funcionalidades planejadas

- Upload ou inserção manual de documentos veterinários;
- leitura e organização de documentos-fonte;
- divisão do conteúdo em trechos menores;
- extração de informações relevantes;
- consulta contextual a partir dos documentos enviados;
- geração de respostas com base no conteúdo fornecido;
- registro dos prompts utilizados;
- documentação do fluxo de funcionamento;
- futura integração com APIs de LLMs;
- futura interface web simples.

---

## Stack em estudo

- Python;
- JavaScript/TypeScript;
- Node.js;
- APIs REST;
- Git e GitHub;
- modelos de linguagem;
- RAG;
- embeddings;
- automação de processos.

Minha linguagem de maior afinidade atualmente é Python, principalmente para automação, análise de dados e prototipação. Também estou estudando JavaScript/TypeScript para desenvolvimento web, APIs e futuras integrações com LLMs.

---

## Estrutura do repositório

```text
Ia-Vet-Doc/
│
├── docs/
│   ├── problema.md
│   ├── arquitetura.md
│   └── roadmap.md
│
├── exemplos/
│   └── exemplo-laudo-ficticio.md
│
├── prompts/
│   └── prompt-consulta-documentos.md
│
├── src/
│   └── prototipo.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Arquitetura conceitual

Fluxo inicial previsto:

1. Entrada de documento-fonte;
2. limpeza e organização do texto;
3. divisão do conteúdo em trechos;
4. armazenamento dos trechos;
5. consulta do usuário;
6. recuperação dos trechos mais relevantes;
7. envio do contexto para um modelo de linguagem;
8. geração de resposta estruturada;
9. exibição da resposta com base no conteúdo fornecido;
10. revisão humana.

---

## Como executar o protótipo

A primeira versão do projeto possui um protótipo simples em Python localizado em:

```text
src/prototipo.py
```

Esse protótipo simula um fluxo inicial de organização e consulta de documentos veterinários.

Atualmente, ele realiza as seguintes etapas:

1. Recebe um documento veterinário fictício;
2. limpa e organiza o texto;
3. divide o conteúdo em trechos menores;
4. busca trechos relacionados a termos definidos;
5. exibe os resultados encontrados no terminal.

### Requisitos

- Python 3 instalado;
- não há dependências externas obrigatórias nesta fase.

### Como rodar

Clone o repositório:

```bash
git clone https://github.com/yasmine-vet-ads/Ia-Vet-Doc.git
```

Acesse a pasta do projeto:

```bash
cd Ia-Vet-Doc
```

Execute o protótipo:

```bash
python src/prototipo.py
```

Em alguns ambientes, pode ser necessário usar:

```bash
python3 src/prototipo.py
```

### Saída esperada

O script exibe no terminal a pergunta simulada e os trechos do documento que possuem relação com os termos buscados.

Exemplo de pergunta usada no protótipo:

```text
Quais alterações urinárias e renais aparecem no documento?
```

O objetivo desta etapa é demonstrar o conceito inicial de recuperação de contexto usando busca simples por palavras-chave.

---

## Documentação do projeto

A documentação está organizada na pasta `docs/`:

- [`docs/problema.md`](docs/problema.md): descreve o problema que o projeto busca explorar;
- [`docs/arquitetura.md`](docs/arquitetura.md): apresenta a arquitetura conceitual;
- [`docs/roadmap.md`](docs/roadmap.md): organiza as etapas futuras do projeto.

---

## Exemplo de documento

O projeto possui um documento fictício para testes:

- [`exemplos/exemplo-laudo-ficticio.md`](exemplos/exemplo-laudo-ficticio.md)

Esse arquivo simula um laudo veterinário e serve como base para testar leitura, divisão em trechos, busca por informações e consulta contextual.

---

## Prompt inicial

O prompt inicial está disponível em:

- [`prompts/prompt-consulta-documentos.md`](prompts/prompt-consulta-documentos.md)

Ele foi criado para orientar respostas baseadas apenas no documento-fonte, evitando criação de informações não presentes no texto original.

---

## Exemplo de uso futuro

O usuário poderá enviar um laudo veterinário fictício ou documento técnico e perguntar, por exemplo:

> Quais são os principais achados descritos neste documento?

> Organize este conteúdo em tópicos técnicos para revisão.

> Quais informações clínicas são relevantes para acompanhamento do caso?

> Há informações renais ou urinárias descritas no texto?

---

## Cuidados éticos

Este projeto tem finalidade educacional e experimental.

As respostas geradas por modelos de linguagem não substituem a avaliação de um médico-veterinário, não devem ser usadas como diagnóstico automático e precisam ser revisadas por profissional habilitado.

Documentos reais devem ser anonimizados antes de qualquer uso, removendo dados de tutores, pacientes, clínicas e profissionais.

---

## Roadmap resumido

- [x] Definir problema e objetivo do projeto;
- [x] criar estrutura inicial do repositório;
- [x] documentar proposta e arquitetura;
- [x] criar roadmap técnico;
- [x] criar exemplo fictício de documento veterinário;
- [x] criar prompt inicial de consulta;
- [x] criar protótipo simples em Python;
- [ ] melhorar o protótipo para ler arquivos externos;
- [ ] simular consulta contextual com base no documento;
- [ ] implementar integração com API de LLM;
- [ ] evoluir para API com Node.js ou TypeScript;
- [ ] criar interface web simples.

---

## Próximas melhorias

- Ler automaticamente arquivos `.md` ou `.txt`;
- permitir que o usuário digite uma pergunta no terminal;
- organizar os resultados em formato mais próximo de uma resposta técnica;
- separar funções em módulos;
- criar testes simples;
- adicionar exemplo de API REST futura;
- documentar endpoints planejados;
- estudar integração com embeddings e vector store.

---

## Diferencial do projeto

Este projeto une tecnologia e conhecimento de domínio.

A proposta não é apenas testar IA de forma genérica, mas aplicar esses conceitos a um problema real da área veterinária: a organização e consulta de documentos técnicos e clínicos.

Essa abordagem conecta minha trajetória em saúde, diagnóstico por imagem, documentação técnica e dados com minha formação atual em Análise e Desenvolvimento de Sistemas.

---

## Autora

Yasmine Santos  
Estudante de Análise e Desenvolvimento de Sistemas — IFRS  
Médica-veterinária especialista em Diagnóstico por Imagem  
GitHub: [yasmine-vet-ads](https://github.com/yasmine-vet-ads)
