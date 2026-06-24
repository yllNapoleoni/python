import streamlit as st
import requests
import pandas as pd

# The URL where our FastAPI server is running
API_URL = "http://localhost:8000/books/"

st.set_page_config(page_title="Library Manager", page_icon="📚")
st.title("📚 Personal Book Library")

# Sidebar navigation
menu = ["View Books", "Add Book", "Update Book", "Delete Book"]
choice = st.sidebar.selectbox("Menu", menu)

# --- VIEW (READ) ---
if choice == "View Books":
    st.subheader("Your Library")
    response = requests.get(API_URL)

    if response.status_code == 200:
        books = response.json()
        if books:
            # Display as a nice table using pandas
            df = pd.DataFrame(books)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No books found. Go to 'Add Book' to get started!")
    else:
        st.error("Failed to connect to backend.")

# --- ADD (CREATE) ---
elif choice == "Add Book":
    st.subheader("Add a New Book")
    with st.form("add_form", clear_on_submit=True):
        b_id = st.number_input("Book ID", min_value=1, step=1)
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.number_input("Publication Year", min_value=1000, max_value=2026, step=1)
        is_read = st.checkbox("I have read this book")

        submit = st.form_submit_button("Save Book")

        if submit:
            payload = {"id": b_id, "title": title, "author": author, "year": year, "is_read": is_read}
            res = requests.post(API_URL, json=payload)
            if res.status_code == 200:
                st.success(f"'{title}' added successfully!")
            else:
                st.error(f"Error: {res.json().get('detail')}")

# --- UPDATE ---
elif choice == "Update Book":
    st.subheader("Update an Existing Book")
    # Fetch current books to show available IDs
    current_books = requests.get(API_URL).json()
    if not current_books:
        st.warning("No books available to update.")
    else:
        # Let user select which book to update by ID
        book_ids = [book["id"] for book in current_books]
        selected_id = st.selectbox("Select Book ID to Update", book_ids)

        # Find current details to prepopulate form
        selected_book = next(book for book in current_books if book["id"] == selected_id)

        with st.form("update_form"):
            title = st.text_input("Title", value=selected_book["title"])
            author = st.text_input("Author", value=selected_book["author"])
            year = st.number_input("Publication Year", value=selected_book["year"], step=1)
            is_read = st.checkbox("I have read this book", value=selected_book["is_read"])

            submit = st.form_submit_button("Update Book")

            if submit:
                payload = {"id": selected_id, "title": title, "author": author, "year": year, "is_read": is_read}
                res = requests.put(f"{API_URL}{selected_id}", json=payload)
                if res.status_code == 200:
                    st.success("Book updated successfully!")
                else:
                    st.error(f"Error: {res.json().get('detail')}")

# --- DELETE ---
elif choice == "Delete Book":
    st.subheader("Delete a Book")
    b_id = st.number_input("Enter Book ID to Delete", min_value=1, step=1)

    if st.button("Delete"):
        res = requests.delete(f"{API_URL}{b_id}")
        if res.status_code == 200:
            st.success(f"Book ID {b_id} deleted successfully.")
        else:
            st.error(f"Error: {res.json().get('detail')}")