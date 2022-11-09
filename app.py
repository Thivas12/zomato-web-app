import streamlit as st
import pickle as pkl
import warnings
warnings.filterwarnings("ignore")

model = pkl.load(open('model.pkl','rb'))


def prediction(online_order, book_table, votes, location, rest_type,
               cuisines, cost, menu_item):    
    prediction = model.predict([[online_order, book_table, votes, location, rest_type,
               cuisines, cost, menu_item]])  
    print(prediction)
    return(prediction)


 
st.title("Zomato Restaurant Rate Prediction")  
 
st.markdown(html_temp, unsafe_allow_html = True)  
online_order = st.number_input('Do you want to order online? ( 1: Yes , 0: No):', min_value=0.0, max_value=1.0, value=1.0) 
book_table = st.number_input('Do you want to book table? ( 1: Yes , 0: No):', min_value=0.0, max_value=1.0, value=1.0)
votes = st.number_input('Enter the votes:')
location = st.number_input('Enter the location:')
rest_type = st.number_input('Enter the rest type:')
cuisines = st.number_input('Enter the cuisines:')
cost = st.number_input('Enter the cost:')
menu_item = st.number_input('Enter the menu item:') 
result = " "  
        
if st.button ("Predict"):  
    result = prediction(online_order, book_table, votes, location, rest_type,
            cuisines, cost, menu_item)  
    st.success ('The output of the above is {}'.format(result))  

