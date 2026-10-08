import pandas as pd
import streamlit as st

st.title("Employee basic details")

if "employees" not in st.session_state:
    st.session_state.employees = []

with st.form("employee_form"):
    name = st.text_input("Enter your first & last name:")
    age = st.slider("Enter the age:", min_value=1, max_value=100, value=25)
    city = st.selectbox("Select your city:", ["Delhi", "Gurgaon", "Noida"])
    submitted = st.form_submit_button("Add employee")

if submitted:
    if name.strip():
        st.session_state.employees.append(
            {"Name": name.strip(), "Age": age, "City": city}
        )
    else:
        st.error("Please enter a name before adding the employee.")

if st.session_state.employees:
    df = pd.DataFrame(st.session_state.employees)
    st.subheader("Employee data")
    st.dataframe(df, use_container_width=True)

    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download all employee data",
        data=csv_data,
        file_name="employee_data.csv",
        mime="text/csv",
    )
else:
    st.info("Add an employee to create the downloadable data.")
