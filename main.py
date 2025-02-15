import streamlit as st
import pandas as pd

# Title of the post
st.title("What is a Pandas DataFrame?")

# Introduction section
st.write("""
In the world of data science and data analysis, one of the most powerful and commonly used tools is **Pandas**, 
a Python library designed for data manipulation and analysis. At the heart of Pandas lies the **DataFrame**, a 
two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).
If you're working with data, understanding Pandas DataFrames is essential!
""")

# What is a DataFrame section
st.subheader("What is a DataFrame?")
st.write("""
A **Pandas DataFrame** is a **table-like data structure** that consists of rows and columns, very similar to a table 
in a relational database, an Excel spreadsheet, or an SQL table. It’s a versatile structure that allows us to store 
and manipulate large datasets easily.

A DataFrame can be thought of as a dictionary of **Series** (one-dimensional labeled arrays) where each Series 
represents a column in the DataFrame. These columns can hold different types of data, such as integers, strings, 
floating-point numbers, or even Python objects.
""")

# Example: Creating a DataFrame
st.subheader("Creating a DataFrame")
st.write("""
There are several ways to create a DataFrame in Pandas. Here's an example of creating a DataFrame from a dictionary:
""")

# Create sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create DataFrame
df = pd.DataFrame(data)

st.write("Here's an example of a simple Pandas DataFrame:")

# Display the DataFrame in the Streamlit app
st.write(df)

# DataFrame Structure section
st.subheader("DataFrame Structure")
st.write("""
A DataFrame has the following components:
1. **Index**: The row labels, which can be integers or any other type of label you assign to the rows. By default, an integer index starting from 0 is used.
2. **Columns**: The column labels (headers) that represent the different variables in your dataset.
3. **Data**: The actual data values in the form of rows and columns.
""")

# Manipulating DataFrames section
st.subheader("Manipulating DataFrames")
st.write("""
Once you have your DataFrame, you can easily manipulate and analyze your data. Here are some common operations:

- **Selecting data**: You can access specific columns or rows using indexing.
""")
st.code("""
# Access a single column
df['Name']

# Access multiple columns
df[['Name', 'Age']]
""")
st.write("""
- **Filtering data**: You can filter rows based on conditions.
""")
st.code("""
# Filter rows where Age is greater than 30
df[df['Age'] > 30]
""")
st.write("""
- **Sorting data**: You can sort data based on one or more columns.
""")
st.code("""
# Sort by Age
df.sort_values(by='Age')
""")
st.write("""
- **Handling missing data**: Pandas provides powerful functions to handle missing or null data, such as filling or dropping missing values.
""")
st.code("""
# Fill missing values with 0
df.fillna(0, inplace=True)
""")

# Use Cases section
st.subheader("Pandas DataFrame Use Cases")
st.write("""
- **Data Cleaning**: DataFrames make it easy to clean and preprocess data for analysis.
- **Data Wrangling**: You can reshape, filter, and merge data to prepare it for analysis.
- **Statistical Analysis**: With Pandas, you can quickly calculate summary statistics such as means, medians, and standard deviations.
- **Visualization**: Pandas integrates well with visualization libraries like Matplotlib and Seaborn to create charts and graphs from your data.
""")

# Conclusion section
st.subheader("Conclusion")
st.write("""
Pandas DataFrames are an essential data structure in the world of data analysis and manipulation. Their flexibility 
and power make them a go-to tool for handling structured data in Python. Whether you're cleaning, exploring, or 
visualizing data, the DataFrame will be at the heart of your analysis workflow.

Ready to start working with DataFrames in your own projects? Give it a try, and you'll quickly see how invaluable 
they can be for your data analysis tasks!
""")
