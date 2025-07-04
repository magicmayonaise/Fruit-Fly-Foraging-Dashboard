import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("🔮 Fruit Fly Foraging RL Dashboard")
st.markdown("""
Explore how Drosophila connectomic data drives odor-modulated foraging behavior. This dashboard integrates outputs from your
RL model and FlyWire-derived subgraphs.
""")

# --- Section 1: Load RL output data ---
st.header("🌿 RL Agent Performance")

rl_file = st.file_uploader("Upload RL reward CSV (e.g. reward.csv)", type="csv")
if rl_file:
    rl_df = pd.read_csv(rl_file)
    st.subheader("Reward Over Time")
    st.line_chart(rl_df.iloc[:, -1], use_container_width=True)

    st.subheader("Summary Stats")
    st.dataframe(rl_df.describe())

# --- Section 2: Load FlyWire subgraph ---
st.header("🧬 Neuron Subgraph Viewer (FlyWire)")

graph_file = st.file_uploader("Upload FlyWire neuron graph (.gpickle)", type="gpickle")
if graph_file:
    G = nx.read_gpickle(graph_file)
    nt = Network(height="500px", width="100%", bgcolor="#ffffff", font_color="black")
    nt.from_nx(G)
    nt.save_graph("fly_graph.html")
    HtmlFile = open("fly_graph.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=550, scrolling=True)

# --- Section 3: Circuit Overview and Behavioral Conditions ---
st.header("💡 Circuit Metadata & Context")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 💧 Internal State")
    hunger = st.slider("Hunger level", 0.0, 1.0, 0.5)
    thirst = st.slider("Thirst level", 0.0, 1.0, 0.5)

with col2:
    st.markdown("### ☀️ Environment")
    humidity = st.slider("Humidity gradient", 0.0, 1.0, 0.3)
    odorant = st.selectbox("Odorant cue present?", ["None", "Vinegar", "Ethanol", "Pheromone"])

st.success("Use inputs above to drive simulation trials and re-train RL agents.")

# --- Footer ---
st.markdown("""
---
Built with ❤️ for computational neuroethology and connectomic modeling.
""")
