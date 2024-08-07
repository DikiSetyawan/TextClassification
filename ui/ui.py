import sys
import datetime
import os
import csv


import streamlit as st

def main():
    st.title("Text Classification Data Input")
    st.write("Please input your text and category:")

    text = st.text_input("Text:")
    categories = []  # Replace with your actual categories
    category = st.selectbox("Category:", categories) # Get categories from preprocess

    if st.button("Submit"):
        data = [text, category, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]  # Use preprocess.input_data for data preparation

        # Save data to CSV
        file_path = "/home/sat/diki/topicClassification/data/data.csv"
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Text", "Category", "Timestamp"])  # Header
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

        st.write("Data submitted successfully!")

if __name__ == "__main__":
    main()
