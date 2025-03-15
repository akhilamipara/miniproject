import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

if 'camp_data' not in st.session_state:
    st.session_state.camp_data = pd.DataFrame(columns=['Organizer', 'Blood Group', 'Units Collected', 'Camp Date'])

st.title("Blood Donation Camp Management System")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ Add Camp"):
        st.session_state.selected_tab = "Add Camp"

with col2:
    if st.button("📋 Manage Camp"):
        st.session_state.selected_tab = "Manage Camp"

with col3:
    if st.button("📊 Blood Collection Summary"):
        st.session_state.selected_tab = "Blood Collection Summary"

if 'selected_tab' not in st.session_state:
    st.session_state.selected_tab = "Add Camp"

if st.session_state.selected_tab == "Add Camp":
    st.markdown("## ➕ Add New Camp")
    
    with st.form('camp_form'):
        organizer_name = st.text_input("Enter the organizer's name:")
        blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        selected_blood_group = st.selectbox("Select blood group:", blood_groups)
        units_collected = st.number_input("Enter units of blood collected:", value=1, min_value=1, step=1)
        camp_date = st.date_input("Select the date of the camp:")
        agree = st.checkbox("I agree that the information provided is accurate.")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not organizer_name:
            st.warning("Please enter the organizer's name.")
        elif not agree:
            st.warning("You must agree that the information provided is accurate.")
        else:
            new_data = pd.DataFrame({
                'Organizer': [organizer_name],
                'Blood Group': [selected_blood_group],
                'Units Collected': [units_collected],
                'Camp Date': [camp_date]
            })
            st.session_state.camp_data = pd.concat([st.session_state.camp_data, new_data], ignore_index=True)
            st.success(f" Camp organized by {organizer_name} on {camp_date} recorded successfully!")

elif st.session_state.selected_tab == "Manage Camp":
    st.markdown("## 📋 Manage Blood Donation Camps")
    
    if not st.session_state.camp_data.empty:
        edited_data = st.session_state.camp_data.copy()
        
        for index, row in st.session_state.camp_data.iterrows():
            col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 2, 1, 1])  
            
            with col1:
                organizer = st.text_input("Organizer", value=row["Organizer"], key=f"org_{index}")
            with col2:
                blood_group = st.text_input("Blood Group", value=row["Blood Group"], key=f"bg_{index}", disabled=True)
            with col3:
                units = st.number_input("Units", value=row["Units Collected"], min_value=1, step=1, key=f"units_{index}")
            with col4:
                camp_date = st.date_input("Camp Date", value=row["Camp Date"], key=f"date_{index}")
            with col5:
                edit_btn = st.button("✏️", key=f"edit_{index}")
            with col6:
                delete_btn = st.button("🗑️", key=f"delete_{index}")

            if edit_btn:
                edited_data.at[index, "Organizer"] = organizer
                edited_data.at[index, "Units Collected"] = units
                edited_data.at[index, "Camp Date"] = camp_date
                st.success(f"✅ Row {index + 1} updated!")

            if delete_btn:
                edited_data = edited_data.drop(index)
                st.success(f"🗑️ Row {index + 1} deleted!")

        st.session_state.camp_data = edited_data.reset_index(drop=True)
    
    else:
        st.info("No recorded camps to display.")

elif st.session_state.selected_tab == "Blood Collection Summary":
    st.markdown("## 📊 Blood Collection Summary")
    
    if not st.session_state.camp_data.empty:
        summary_data = st.session_state.camp_data.groupby('Blood Group')['Units Collected'].sum().reset_index()
        fig, ax = plt.subplots()
        ax.bar(summary_data['Blood Group'], summary_data['Units Collected'], color='maroon')
        ax.set_xlabel('Blood Group', fontsize=12)
        ax.set_ylabel('Units Collected', fontsize=12)
        ax.set_title('Units of Blood Collected by Blood Group', fontsize=14)
        st.pyplot(fig)
    else:
        st.info(" No data available to display.")
