
# 📊 Aplicativo Interativo de Análise de Dados com Streamlit

Este é um projeto web interativo desenvolvido com **Streamlit** que permite carregar, visualizar e explorar dados de maneira simples e intuitiva. Com ele, você pode fazer o upload de arquivos CSV ou Excel, visualizar tabelas, gerar estatísticas descritivas e criar gráficos diversos — tudo sem escrever uma linha de código!

---

## 📌 Funcionalidades

- Upload de datasets nos formatos `.csv` e `.xlsx`
- Visualização de dados em tabela interativa
- Estatísticas descritivas automáticas (média, mediana, desvio padrão)
- Criação de gráficos:
  - Histograma
  - Gráfico de dispersão (*scatter plot*)
  - Gráfico de barras
- Filtros dinâmicos e personalizáveis
- Dataset de exemplo incluso

---

## 🚀 Como rodar o projeto localmente

### 1. Clone ou baixe o repositório

Você pode [baixar o ZIP clicando aqui](#) ou clonar com Git:

```bash
git clone https://github.com/enzodias1/questao3.git
```

### 2. Acesse a pasta do projeto

```bash
cd questao3
```

### 3. Crie e ative um ambiente virtual

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as dependências

Instale os pacotes necessários manualmente:

```bash
pip install streamlit pandas matplotlib seaborn scikit-learn openpyxl
```

### 5. Execute a aplicação

```bash
streamlit run questao3.py
```

### 6. Acesse no navegador

A aplicação será aberta automaticamente, ou acesse manualmente:

```
http://localhost:8501
```

---

## Dataset de exemplo incluso
Você pode começar mesmo sem ter um arquivo próprio! Basta selecionar a opção "Usar dataset de exemplo" no menu da aplicação. Os datasets disponíveis são:

🌸 Iris Dataset

🏠 California Housing Dataset

---

## 🛠 Tecnologias utilizadas

- Python 3
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- scikit-learn

---

## 👤 Autor

<p style="text-align: center; font-size: 13px; color: gray">
Feito com 💻 por **Enzo Rodrigues**
</p>

