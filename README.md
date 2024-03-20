# Step-by-Step Guide: Building a Simple Calculator with Streamlit

In this guide, we'll walk through the process of building a basic calculator application using Python and Streamlit. Streamlit is a powerful library for building interactive web applications with minimal code. Let's get started!

## Step 1: Setting Up Your Environment

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Install Streamlit using pip:

   ```bash
   pip install streamlit
   ```

*alternative: [streamlit sandbox](https://samdobson-streamlit-sandbox-app-za85j0.streamlit.app/)*
   

## Step 2: Creating the Project Structure

1. Create a new directory for your project:

   ```bash
   mkdir simple-calculator
   cd simple-calculator
   ```
   

2. Inside the project directory, create a new Python script for the calculator application. Let's name it calculator.py.

## Step 3: Writing the Calculator Code

1. Open `calculator.py` in your favorite text editor or IDE.

2. Import the necessary libraries:

   ```python
   import streamlit as st
   ```
   

3. Define the Streamlit app layout:

   ```python
   st.title('Simple Calculator')
   ```
   

4. Add input fields for numbers and operators:
   ```python
   num1 = st.number_input('Enter the first number:')
   operator = st.selectbox('Select operator:', ['+', '-'])
   num2 = st.number_input('Enter the second number:')
   ```
   

5. Add a button to perform the calculation:
    ```python
    if st.button('Calculate'):
        result = None
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        
        st.write(f'Result: {result}')
    ```
   
## Step 4: Running the Application

1. Save your changes to `calculator.py`.

2. Open your terminal and navigate to the project directory (simple-calculator).

3. Run the Streamlit application:

```python
streamlit run calculator.py
```
   
4. Once the application is running, open your web browser and navigate to the provided URL (usually http://localhost:8501).

## Step 5: Adding Subtraction, Multiplication, and Division (Tasks)

1. *Task 1: Multiplication*: Implement the multiplication functionality by adding a conditional block for the `*` operator.

2. *Task 2: Division*: Implement the division functionality by adding a conditional block for the `/` operator. Make sure to handle division by zero error.


## Step 6: Testing the Application

1. Use the input fields and buttons to perform calculations. Enter numbers and select operators to build your expression, and click the "Calculate" button to see the result.

2. Test different scenarios to ensure the calculator behaves as expected.

## Step 7: Customization and Enhancements

1. Feel free to customize the layout and styling of the calculator application using Streamlit's features.

2. You can add more advanced features or functionalities to the calculator based on your requirements and preferences.

3. Explore Streamlit's documentation for more ideas and possibilities.

Congratulations! You've successfully built a simple calculator application using Python and Streamlit.
