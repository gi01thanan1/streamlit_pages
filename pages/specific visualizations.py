import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
#df = px.data.tips()
df = pd.read_csv("pages/used_cars.csv")
graph=['averagev price/brand','average price/top 10 types','miles per gallon/type','price/miles per gallon']
graph_choice = st.selectbox(label="Choose graph", options=graph)

def func1():
    plt.figure(figsize=(12, 6))
    df.groupby('brand')['msrp'].mean().sort_values(ascending=False).plot(kind='bar', color='orange')
    plt.title('Average Price per Brand')
    plt.xlabel('Brand')
    plt.ylabel('Average Price ($)')
    plt.grid(True)
    st.pyplot(plt)
def func2():
    top_types = df.groupby('type')['msrp'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_types.values, y=top_types.index, palette='RdYlGn')
    plt.title('Top 10 Most Expensive types')
    plt.xlabel('Average Price ($)')
    plt.ylabel('type')
    plt.grid(True)
    st.pyplot(plt)
def func3():
    plt.figure(figsize=(12, 6))
    sns.barplot(x='type', y='miles_per_gallon', data=df)
    plt.title('average miles per gallon per each type')
    plt.xlabel('type')
    plt.ylabel('miles per gallon')
    plt.grid(True)
    st.pyplot(plt)
def func4():
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df,x="miles_per_gallon",y="msrp",hue="type")
    plt.title("efficiency with price")
    plt.xlabel('miles_per_gallon')
    plt.ylabel('price($)')
    st.pyplot(plt)

draw_graph = {'averagev price/brand':func1, "average price/top 10 types":func2,"miles per gallon/type":func3,"price/miles per gallon":func4}
draw_graph[graph_choice]()




