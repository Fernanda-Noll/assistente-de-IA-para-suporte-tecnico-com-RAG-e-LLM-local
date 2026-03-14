# 🤖 Assistente de IA para Suporte Técnico (RAG + LLM Local)

Assistente de Inteligência Artificial para suporte técnico e utilização de softwares, utilizando RAG (Retrieval-Augmented Generation) e LLM rodando localmente.

O sistema consulta uma base de conhecimento técnica e gera respostas contextualizadas para auxiliar usuários em tarefas de TI e troubleshooting.

---

# 📌 Visão Geral do Projeto

Este projeto demonstra a implementação de um pipeline completo de IA generativa com RAG, incluindo:

- Construção de uma base de conhecimento técnica
- Processamento e preparação de dados
- Geração de embeddings semânticos
- Criação de um banco vetorial
- Recuperação de contexto relevante
- Integração com LLM local
- Interface interativa para consulta

O objetivo é demonstrar como construir um assistente técnico baseado em documentação, utilizando modelos de linguagem locais e busca semântica.

---

# 🎯 Problema

Usuários frequentemente precisam de ajuda para:

- Utilizar softwares
- Resolver problemas de hardware ou software
- Encontrar informações específicas em documentações técnicas 

Documentações tradicionais são longas e difíceis de navegar.

Este projeto propõe uma solução de **IA conversacional capaz de consultar automaticamente a documentação técnica** e gerar respostas claras.

---

# 🧠 Solução

A aplicação utiliza Retrieval-Augmented Generation (RAG).

Esse método combina:

* **Busca semântica em documentos**
* **Geração de respostas por LLM**

## Fluxo da aplicação

### Construção da base vetorial

1. Documentos técnicos são carregados
2. O conteúdo é dividido em **chunks de texto**
3. São gerados **embeddings semânticos**
4. Os vetores são armazenados no **ChromaDB**

### Durante a consulta do usuário

5. O usuário faz uma pergunta
6. O sistema realiza **busca semântica**
7. Os documentos mais relevantes são recuperados
8. O contexto é enviado para a **LLM local**
9. A LLM gera uma **resposta baseada nos documentos recuperados**

---

# 📚 Base de Conhecimento

A base de conhecimento foi construída a partir de documentos com informações técnicas sobre diferentes sistemas e ferramentas utilizados em suporte de TI.

Para auxiliar na geração inicial do conteúdo, foi utilizado o **Google Gemini**, que ajudou na estruturação e organização dos materiais. Após essa etapa, todos os documentos passaram por um processo de **revisão e curadoria manual**, garantindo maior precisão e qualidade das informações.

Também foi realizado um processo de **preparação dos dados (data preprocessing)** para otimizar o desempenho do pipeline de RAG. Entre os ajustes realizados:

- remoção de tabelas e estruturas complexas
- reorganização de trechos de texto
- padronização da linguagem
- melhoria da coerência entre seções

Essas etapas são importantes pois **modelos de embedding funcionam melhor com texto contínuo e semanticamente consistente**, o que melhora:

- a qualidade da **busca semântica**
- a relevância dos **documentos recuperados**
- a precisão das **respostas geradas pela LLM**

Esse processo ajuda a aumentar a eficiência do sistema de **Retrieval-Augmented Generation (RAG)**.

### Documentos incluídos

**Adobe**

- Criado a partir das páginas oficiais do site da Adobe
- Contém informações sobre utilização das ferramentas

**Ecossistema Microsoft 365 Corporativo**

- Informações sobre uso de ferramentas do Microsoft 365

**Hardware e Troubleshooting**

- Conceitos de hardware
- Diagnóstico de problemas
- Dicas de troubleshooting

**Linux**

- Comandos básicos
- Utilização geral do sistema

**Windows**

- Utilização e gerenciamento do sistema operacional

---

# ⚙️ Tecnologias Utilizadas

### LLM Local

* **LM Studio**
* Modelo utilizado:

`lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF`

Configuração:

* Quantização: **Q4_K_M**
* Escolhido por ser **mais leve e rápido para execução local**

---

### Embeddings

Modelo utilizado:

`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

Motivo da escolha:

- Modelo multilíngue, com bom desempenho em português
- Boa qualidade para similaridade semântica
- Leve e eficiente para execução local

Esse modelo transforma trechos de texto em vetores semânticos (embeddings) que permitem ao sistema encontrar documentos com significado semelhante à pergunta do usuário, mesmo quando as palavras utilizadas são diferentes.

Biblioteca utilizada:

- **Hugging Face Sentence Transformers**

---

### Banco Vetorial

Utilizado:

- **LangChain**
- **ChromaDB**

Biblioteca:

```python
langchain_chroma
```

Responsável por:

- Armazenar os vetores
- Realizar busca semântica
- Recuperar documentos relevantes

---

### Interface

Framework utilizado:

- **Streamlit**

Responsável por:

- Interface do usuário
- Integração com backend
- Execução das consultas

---

# 📂 Estrutura do Projeto

```
RAG_IA/
│
├─ banco_vetorial/            # Persistência do Chroma (vetores)
│
├─ base_de_conhecimento/      # Documentos usados como base de conhecimento
│
├─ src/
│   ├─ services/
│   │   └─ conexao_lm_studio.py   # Conexão com a LLM no LM Studio
│   │
│   ├─ cria_bd_vetorial.py        # Script para gerar o banco vetorial
│   │
│   ├─ main.py                    # Interface principal em Streamlit
│   │
│   └─ script_prompt_ia.py        # Templates de prompt utilizados no RAG
│
├─ README.md                   # Descrição do projeto
│
└─ requirements.txt            # Bibliotecas necessárias para rodar o projeto.
```

---

# 🗄️ Criação do Banco Vetorial

Para gerar o banco de dados vetorial execute:

```bash
python src/cria_bd_vetorial.py
```

Esse script irá:

* Ler os documentos
* Dividir o conteúdo em chunks
* Gerar os embeddings
* Armazenar no **ChromaDB**

---

# 🚀 Executando o Projeto

### 1️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Iniciar o LM Studio

* Baixe o modelo:

```
lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF
```

* Inicie o servidor local.

---

### 3️⃣ Executar a aplicação

```bash
streamlit run src/main.py
```

---

# 💬 Exemplos de Uso

Abaixo estão alguns exemplos de perguntas feitas ao sistema e as respostas geradas.

<img src="Imagens das respostas/assinar documento salvo em pdf.png" alt="Imagem como assinar um documento salvo em PDF">

<img src="Imagens das respostas/computador lento.png" alt="Imagem computador está lento">

<img src="Imagens das respostas/outlook.png" alt="Imagem dúvida sobre o Outlook">

---

# 📈 Melhorias Futuras

* Melhorar a **qualidade dos prompts**
* Adicionar **mais documentos técnicos**
* Implementar **memória de conversa**
* Melhorar o **ranking de documentos recuperados**
* Implementar **avaliação automática das respostas**
* Adicionar **logs e monitoramento**

---

# 🎯 Possíveis Aplicações

Este tipo de solução pode ser utilizada para:

* **Suporte técnico interno**
* **Helpdesk corporativo**
* **Assistentes de TI**
* **Documentação inteligente**
* **Treinamento de equipes**

---

💡 Projeto desenvolvido para estudo e experimentação com **RAG, LLMs locais e IA aplicada ao suporte técnico**.

---

## ⭐ Contribuições

Sugestões e melhorias são bem-vindas.

---
