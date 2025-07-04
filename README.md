
# 🧬 Fruit Fly Foraging RL Dashboard

This Streamlit app visualizes reinforcement learning (RL) model outputs and integrates FlyWire connectome subgraphs to explore odor-guided foraging behavior in *Drosophila*.

## 📁 Project Structure

```
FruitFlyForagingDashboard/
├── data/
│   ├── reward.csv                # Mock RL reward data
│   └── flywire_subgraph.gpickle # Mock neuron subgraph
├── models/                       # (Optional) Trained models
├── outputs/                      # (Optional) Agent outputs or plots
├── streamlit_app.py              # Streamlit dashboard
└── README.md                     # Project instructions
```

## 🚀 Quickstart

1. Clone or unzip the project.
2. Install dependencies:
   ```bash
   pip install streamlit pandas matplotlib networkx pyvis
   ```
3. Run the dashboard:
   ```bash
   streamlit run streamlit_app.py
   ```

## 📂 How to Use

- Upload `reward.csv` to visualize reward dynamics from your RL model.
- Upload `flywire_subgraph.gpickle` to view a synaptic subgraph using PyVis.
- Adjust hunger, thirst, humidity, and odorant cue settings to simulate internal and environmental conditions.

## 🔧 Customization Tips

- Replace `data/reward.csv` with outputs from your actual PyTorch RL model.
- Generate real FlyWire subgraphs using your connectome parser and save them as `.gpickle`.
- Extend the app to add PCA plots, behavioral embeddings, or optogenetic overlays.

---

Made for computational neuroethology & connectomics-inspired AI ⚛️


## 🌀 Advanced Features

### 🎞️ Animations
- Store GIFs or MP4s of fly trajectories under `animations/`
- Embed with `st.video()` or `st.image()` for visual playback

### 🧭 Trajectories
- Save fly XY movement logs (e.g., from `flybody` or `DeepFly3D`) in `trajectories/`
- Future support: plot with Plotly or Matplotlib over gradient maps

### ⬆️ Model Uploads
- Upload your PyTorch `.pt` or `.pth` models via the dashboard
- Connect with backend logic to re-run trials

## 🧠 Coming Soon
- 3D fly connectome viewer using `neuroglancer` or `vtk.js`
- Dynamic RL retraining using sidebar inputs
- FlyWire synapse stats visualized by neuropil region

---

Made with 🧬 love and PyTorch RL 🧠


## 🖼️ Screenshots

![Dashboard Screenshot](docs/dashboard_screenshot.png)

## 🎥 Trajectory Demo

> This is a placeholder — replace with your own `.mp4` from fly tracking or RL rollout.

```html
<video width="100%" controls>
  <source src="docs/trajectory_demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
```

