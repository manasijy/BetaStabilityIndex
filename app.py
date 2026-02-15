import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from calculator import calculate_si_beta
from presets import PRESETS


st.set_page_config(
    page_title="Titanium Beta Stability Calculator",
    layout="wide"
)

st.title("Titanium Alloy Beta Stability Index Calculator")


# Sidebar
st.sidebar.header("Options")

mode = st.sidebar.radio(
    "Select Mode",
    ["Single Alloy", "Batch (CSV Upload)"]
)


# Elements list
elements = [
    "Mo","V","W","Nb","Ta","Fe","Cr","Ni","Mn","Co",
    "Al","Sn","Zr","C","O","N"
]


############################################
# SINGLE ALLOY MODE
############################################

if mode == "Single Alloy":

    preset_name = st.sidebar.selectbox(
        "Choose Preset",
        list(PRESETS.keys())
    )

    preset = PRESETS[preset_name]

    st.header("Composition (wt%)")

    cols = st.columns(4)

    composition = {}

    for i, element in enumerate(elements):

        default = preset.get(element, 0.0)

        composition[element] = cols[i % 4].number_input(
            element,
            value=float(default),
            step=0.1
        )


    if st.button("Calculate"):

        mo_eq, al_eq, si = calculate_si_beta(composition)

        st.success("Calculation Complete")

        col1, col2, col3 = st.columns(3)

        col1.metric("Mo equivalent", f"{mo_eq:.3f}")
        col2.metric("Al equivalent", f"{al_eq:.3f}")
        col3.metric("SIβ", f"{si:.3f}")

        # Plot
        fig, ax = plt.subplots()

        ax.bar(
            ["Mo_eq", "Al_eq", "SI_beta"],
            [mo_eq, al_eq, si]
        )

        ax.set_title("Beta Stability Metrics")

        st.pyplot(fig)


############################################
# CSV MODE
############################################

else:

    st.header("Batch Calculation")

    uploaded = st.file_uploader(
        "Upload CSV file",
        type="csv"
    )

    if uploaded:

        df = pd.read_csv(uploaded)

        mo_list = []
        al_list = []
        si_list = []

        for _, row in df.iterrows():

            comp = row.to_dict()

            mo, al, si = calculate_si_beta(comp)

            mo_list.append(mo)
            al_list.append(al)
            si_list.append(si)

        df["Mo_eq"] = mo_list
        df["Al_eq"] = al_list
        df["SI_beta"] = si_list

        st.dataframe(df)

        st.download_button(
            "Download Results",
            df.to_csv(index=False),
            "beta_stability_results.csv"
        )

        # Plot distribution
        fig, ax = plt.subplots()

        ax.hist(df["SI_beta"], bins=20)

        ax.set_title("SIβ Distribution")

        st.pyplot(fig)
