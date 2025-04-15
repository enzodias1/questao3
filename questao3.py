import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, fetch_california_housing

st.set_page_config(page_title="Analisador de Dataset", layout="wide")

st.title("📊 Aplicação de Análise de Dados")

st.markdown(
    "<p style='text-align: center; font-size: 12px; color: gray;'>Feito por Enzo Rodrigues</p>",
    unsafe_allow_html=True
)

st.markdown("""
Este aplicativo permite que você:
- Faça upload de arquivos `.csv` ou `.xlsx`
- Visualize os dados em um formato de tabela
- Gere estatísticas descritivas, como média, mediana e desvio padrão
- Visualize diferentes tipos de gráficos, como histograma e scatter plot
- E também uma filtragem de dados!
""")

with st.expander("📁 Ou use um dataset de exemplo"):
    exemplo = st.radio("Escolha um dataset de exemplo:", ["Nenhum", "Iris", "California Housing"])
    if exemplo == "Iris":
        data = load_iris(as_frame=True)
        df = data.frame
    elif exemplo == "California Housing":
        data = fetch_california_housing(as_frame=True)
        df = data.frame
    else:
        df = None

st.sidebar.header("Upload do Dataset")
uploaded_file = st.sidebar.file_uploader("Envie um arquivo CSV ou Excel", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)


if df is not None:
    st.subheader("📄 Visualização do Dataset")
    st.dataframe(df, use_container_width=True)


    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    with st.expander("🔎 Filtragem de Dados"):
        col_to_filter = st.multiselect("Escolha colunas para filtrar", numeric_cols)
        df_filtered = df.copy()
        for col in col_to_filter:
            min_val, max_val = float(df[col].min()), float(df[col].max())
            range_vals = st.slider(f"Intervalo de {col}", min_val, max_val, (min_val, max_val))
            df_filtered = df_filtered[df_filtered[col].between(*range_vals)]

        st.dataframe(df_filtered, use_container_width=True)

    st.subheader("📈 Estatísticas Descritivas")
    st.write(df_filtered[numeric_cols].describe().T[['mean', '50%', 'std']].rename(columns={"50%": "median"}))

    st.subheader("📉 Visualização Gráfica")

    chart_type = st.selectbox("Escolha o tipo de gráfico:", ["Histograma", "Dispersão (Scatter Plot)", "Boxplot"])
    
    if chart_type == "Histograma":
        col = st.selectbox("Selecione a coluna para o histograma:", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df_filtered[col], kde=True, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Dispersão (Scatter Plot)":
        col_x = st.selectbox("Eixo X:", numeric_cols, key="x")
        col_y = st.selectbox("Eixo Y:", numeric_cols, key="y")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df_filtered, x=col_x, y=col_y, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Boxplot":
        col = st.selectbox("Selecione a coluna para o boxplot:", numeric_cols)
        fig, ax = plt.subplots()
        sns.boxplot(x=df_filtered[col], ax=ax)
        st.pyplot(fig)


else:
    st.info("📝 Faça o upload de um dataset ou escolha um de exemplo para começar.")
