import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/students"

st.set_page_config(page_title="Student Dashboard", layout="centered")

st.title("🎓 Student CRUD Dashboard")

if "edit_id" not in st.session_state:
    st.session_state.edit_id = None


# ---------------- FORM ----------------
st.subheader("➕ Create / ✏️ Update Student")

name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120)
email = st.text_input("Email")

col1, col2 = st.columns(2)

# CREATE
with col1:
    if st.button("Create"):
        res = requests.post(API_URL, json={
            "name": name,
            "age": int(age),
            "email": email
        })

        if res.status_code == 200:
            st.success("Student created")
            st.rerun()
        else:
            st.error("Error creating student")

# UPDATE
with col2:
    if st.button("Update"):
        if st.session_state.edit_id is None:
            st.warning("Click Edit on a student first")
        else:
            res = requests.put(
                f"{API_URL}/{st.session_state.edit_id}",
                json={
                    "name": name,
                    "age": int(age),
                    "email": email
                }
            )

            if res.status_code == 200:
                st.success("Student updated")
                st.session_state.edit_id = None
                st.rerun()
            else:
                st.error("Update failed")


st.divider()

# ---------------- LIST ----------------
st.subheader("📋 Students")

data = requests.get(API_URL).json()

for s in data:
    col1, col2, col3 = st.columns([4, 1, 1])

    with col1:
        st.write(f"**{s['name']}** | Age: {s['age']} | {s['email']}")

    with col2:
        if st.button("Edit", key=f"e{s['id']}"):
            st.session_state.edit_id = s["id"]
            st.rerun()

    with col3:
        if st.button("Delete", key=f"d{s['id']}"):
            requests.delete(f"{API_URL}/{s['id']}")
            st.rerun()