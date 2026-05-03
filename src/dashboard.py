import streamlit as st
import pandas as pd
import os

st.title("OTA Vehicle Test Simulator Dashboard")

if not os.path.exists("data/test_report.csv"):
    st.error("No test report found. Please run the simulation first.")
else:
    df = pd.read_csv("data/test_report.csv")
    
    col1, col2, col3, col4 = st.columns(4)
    
    total_tests = len(df)
    successes = len(df[df['status'] == 'UPDATED'])
    failures = len(df[df['status'] == 'FAILED'])
    failure_rate = (failures / total_tests) * 100 if total_tests > 0 else 0
    
    col1.metric("Total Tests", total_tests)
    col2.metric("Updated", successes)
    col3.metric("Failed", failures)
    col4.metric("Failure Rate", f"{failure_rate:.1f}%")
    
    st.subheader("Test Results Breakdown")
    st.dataframe(df)
    
    st.subheader("Results by Status")
    status_counts = df['status'].value_counts().reset_index()
    status_counts.columns = ['status', 'count']
    st.bar_chart(status_counts.set_index('status'))
    
    if failures > 0:
        st.subheader("Failure Details")
        st.table(df[df['status'] == 'FAILED'][['ecu', 'failure_reason', 'old_version', 'new_version']])