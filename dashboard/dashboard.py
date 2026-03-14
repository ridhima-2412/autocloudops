
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import time

st.set_page_config(page_title="AutoCloudOps Dashboard", layout="wide")

## Dashboard styling: dark theme

st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

h1,h2,h3,h4 {
    color: #e2e8f0;
}


.block-container {
    padding-top: 2rem;
}

.sidebar .sidebar-content {
    background-color: #020617;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

h1,h2,h3,h4 {
    color: #e2e8f0;
}

/* Custom metric value color for specific metrics */
[data-testid="stMetricValue"] {
    color: #38bdf8;
}

#total_instances_metric [data-testid="stMetricValue"],
#idle_instances_metric [data-testid="stMetricValue"],
#potential_savings_metric [data-testid="stMetricValue"] {
    color: #3b82f6 !important;
}

.block-container {
    padding-top: 2rem;
}

.sidebar .sidebar-content {
    background-color: #020617;
}

</style>
""", unsafe_allow_html=True)

## Sidebar navigation

st.sidebar.title("☁ AutoCloudOps")
st.sidebar.markdown("AI-Driven Cloud Optimization")

st.sidebar.divider()

st.sidebar.markdown("### Navigation")
st.sidebar.markdown("📊 Dashboard")
st.sidebar.markdown("🖥 Resource Metrics")
st.sidebar.markdown("⚙ Optimization Insights")

st.sidebar.divider()
st.sidebar.info("Hackathon Prototype")

## Dashboard title and description

st.title("☁ AutoCloudOps – AI Cloud Optimization Dashboard")
st.write("Real-time monitoring and optimization of cloud infrastructure using AI agents.")

## Simulated live metrics for demo

cloud_resources = [
    {"Instance": "EC2-1", "CPU Usage": random.randint(5,20), "Memory Usage": random.randint(10,30), "Status": "Idle"},
    {"Instance": "EC2-2", "CPU Usage": random.randint(60,90), "Memory Usage": random.randint(50,80), "Status": "Active"},
    {"Instance": "EC2-3", "CPU Usage": random.randint(10,30), "Memory Usage": random.randint(20,40), "Status": "Underutilized"},
]

df = pd.DataFrame(cloud_resources)

## Overview metrics

total_instances = len(df)
idle_instances = len(df[df["Status"] == "Idle"])
potential_savings = "$120"

col1, col2, col3 = st.columns(3)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<span style="color:#3b82f6;font-size:18px;font-weight:bold;">🖥 Total Instances</span>', unsafe_allow_html=True)
    st.markdown('<div id="total_instances_metric">', unsafe_allow_html=True)
    st.metric("", total_instances)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<span style="color:#3b82f6;font-size:18px;font-weight:bold;">⚠ Idle Instances</span>', unsafe_allow_html=True)
    st.markdown('<div id="idle_instances_metric">', unsafe_allow_html=True)
    st.metric("", idle_instances)
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<span style="color:#3b82f6;font-size:18px;font-weight:bold;">💰 Potential Monthly Savings</span>', unsafe_allow_html=True)
    st.markdown('<div id="potential_savings_metric">', unsafe_allow_html=True)
    st.metric("", potential_savings)
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

## Resource metrics table

st.subheader("📊 Cloud Resource Metrics")

st.dataframe(df, use_container_width=True)

st.divider()

## Instance resource cards

st.subheader("🖥 Instance Resource Overview")

cols = st.columns(len(cloud_resources))

for idx, resource in enumerate(cloud_resources):

    with cols[idx]:

        st.markdown(f"### {resource['Instance']}")

        st.metric("CPU Usage", f"{resource['CPU Usage']}%")
        st.metric("Memory Usage", f"{resource['Memory Usage']}%")

        status = resource["Status"]

        if status == "Idle":
            st.markdown(
                "<span style='color:#f59e0b;font-weight:bold;'>🟠 Idle</span>",
                unsafe_allow_html=True
            )

        elif status == "Active":
            st.markdown(
                "<span style='color:#22c55e;font-weight:bold;'>🟢 Active</span>",
                unsafe_allow_html=True
            )

        elif status == "Underutilized":
            st.markdown(
                "<span style='color:#3b82f6;font-weight:bold;'>🔵 Underutilized</span>",
                unsafe_allow_html=True
            )

st.divider()

## CPU utilization chart

st.subheader("📈 CPU Utilization")

fig, ax = plt.subplots(figsize=(7,3))

ax.bar(df["Instance"], df["CPU Usage"])

ax.set_ylabel("CPU %", color="#3b82f6", fontsize=12, fontweight="bold")  # blue
ax.set_title("Instance CPU Usage", color="#3b82f6", fontsize=14, fontweight="bold")

ax.tick_params(axis='y', colors="#3b82f6")
ax.tick_params(axis='x', colors="#e2e8f0")

ax.set_facecolor("#1e293b")
fig.patch.set_facecolor("#0f172a")

st.pyplot(fig)

st.divider()

## AI optimization recommendations

st.subheader("⚙ AI Optimization Recommendations")

recommendations = [
    ("🛑", "EC2-1 idle → Stop instance to save cost", "#f59e0b"),
    ("⬇", "EC2-3 underutilized → Downgrade instance type", "#3b82f6"),
    ("✅", "EC2-2 healthy → No action needed", "#22c55e")
]

for icon, text, color in recommendations:

    st.markdown(
        f"<span style='color:{color};font-size:17px;'>{icon} {text}</span>",
        unsafe_allow_html=True
    )

st.divider()

## Estimated cost impact

st.subheader("💰 Estimated Cost Impact")

st.metric("Potential Monthly Savings", "$120")

st.success("AI agents generated these optimization insights automatically.")

st.caption("AutoCloudOps – AI-driven cloud optimization prototype")

## Auto-refresh for live demo

time.sleep(5)
st.rerun()

