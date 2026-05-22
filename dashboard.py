import streamlit as st
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import diagnostics

st.set_page_config(page_title="Student Grade Tracker", layout="wide")
st.title("🎓 Student Performance Tracker & Report Card")
st.write("Track student marks, view progress charts, and get study recommendations.")
st.markdown("---")

st.subheader("Student Details & Marks Entry")
student_name = st.text_input("Enter student name", "")

input_col1, input_col2, input_col3, input_col4 = st.columns(4)

with input_col1:
    math = st.slider("Math", 0, 100, 0)

with input_col2:
    science = st.slider("Science", 0, 100, 0)

with input_col3:
    english = st.slider("English", 0, 100, 0)

with input_col4:
    history = st.slider("History", 0, 100, 0)

st.markdown("---")

df = diagnostics.calculate_metrics(math, science, english, history)
metrics = diagnostics.generate_insights(df)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Results Overview")
    st.metric(label="Overall Percentage", value=f"{metrics['avg_grade']:.1f}%")

with col2:
    st.subheader("Marks per Subject")
    fig, ax = plt.subplots(figsize=(6, 3.5))
    colors = ['#4CAF50' if g >= 75 else '#FF9800' if g >= 60 else '#F44336' for g in df["Grade"]]
    
    ax.bar(df["Subject"], df["Grade"], color=colors, width=0.5)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Marks")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    st.pyplot(fig)

st.markdown("---")
st.subheader("Performance Review")

if st.button("Generate Recommendations", type="primary"):
    if not student_name.strip():
        st.warning("Please enter a student name first!")
    else:
        with st.spinner("Analyzing marks..."):
            st.markdown(f"### Report for **{student_name}**")
            st.write(f"🌟 **Strongest Subject:** Doing excellent work in **{metrics['highest_sub']}**.")
            
            low_g = metrics['lowest_grade']
            low_s = metrics['lowest_sub']
            
            if low_g < 70:
                st.error(f"Attention Needed: {low_s} marks are low at {low_g}%.")
                st.write(f"**Recommendation:** Spend 30 minutes daily reviewing foundational topics in {low_s} before the next exams.")
            elif low_g < 85:
                st.warning(f"Room for Improvement: {low_s} has slight gaps at {low_g}%.")
                st.write(f"**Recommendation:** Solve extra practice problems in {low_s} to help bring this score up.")
            else:
                st.success("Great Job: Performing well across all subjects!")
                st.write("**Recommendation:** Try advanced study materials to stay challenged and ahead of the class.")
