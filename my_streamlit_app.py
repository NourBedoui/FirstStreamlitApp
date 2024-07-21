import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title(':red[Hello Wilders, welcome to my application!] :sunglasses:')

url = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df = pd.read_csv(url)
st.write(df)

for continent in df['continent'].unique():
    st.button(label=continent, key=f"button_{continent}")

st.header(':blue[Description statistique des données]')
describe = df.describe()
st.write(describe)

st.header(':blue[Analyse de corrélation]')
correlation = df.select_dtypes(include=['number']).corr()
fig, ax = plt.subplots(figsize=(10, 8))

cax = ax.matshow(correlation, vmin=-1, vmax=1)
fig.colorbar(cax)
ax.set_xticks(np.arange(len(correlation.columns)))
ax.set_yticks(np.arange(len(correlation.index)))
ax.set_xticklabels(correlation.columns, ha='left', fontsize=12)
ax.set_yticklabels(correlation.index, fontsize=12)

for (i, j), val in np.ndenumerate(correlation.values):
    ax.text(j, i, f'{val:.2f}', ha='center', va='center', color='black', fontsize=13)

plt.title('Matrice de corrélation des variables numériques', fontsize=16, pad=20)
plt.tight_layout()
st.pyplot(fig)

st.header(':blue[Analyse de distribution]')

numeric_columns = df.select_dtypes(include=['number']).columns
selected_column = st.selectbox('Choisissez une variable numérique pour l\'analyse de distribution', options=numeric_columns)

plt.figure(figsize=(12, 6))
sns.histplot(df[selected_column], kde=True)
plt.ylabel('Nombre de voitures')
plt.title(f'Distribution de {selected_column}')
st.pyplot(plt)

categorical_columns = df.select_dtypes(include=['object']).columns
if categorical_columns.size > 0:
    st.header('Répartition par Catégorie')

    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='continent', hue='continent')
    plt.ylabel('Nombre de voitures')
    st.pyplot(plt) 