
import numpy as np
import pickle
import streamlit as st
newmodel = pickle.load(open('C:/Users/ELCOT/Downloads/healthins.sav', 'rb'))


def pred(inputdata):
    newarr = np.asarray(inputdata)
    rearr = newarr.reshape(1, -1)
    prediction = newmodel.predict(rearr)
    return prediction


def main():
    st.title('Health Insurance Predictor')
    #input variables
    age = st.text_input('Age')
    gender = st.radio("Gender", ('Male', 'Female'))
    if(gender =='Male'):
        newg=0
    else:
        newg=1
    try:
        height = st.text_input('Height(in metres)')
        weight = st.text_input('Weight(in Kg)')
        bmi = float(weight)/(float(height)*float(height))
    except:
        print('')
    children = st.text_input('Number Of Children')
    smoker = st.radio('Are you a Smoker',('Yes','No'))
    if (smoker == 'Yes'):
        news = 0
    else:
        news = 1
    
    try:
        result = ""
        if st.button('submit'):
            
            result = pred([age,newg,bmi,children,news])*77.69
            st.write("Rs.")    
            st.success(int(result))
    except:
        print('')
        
if __name__ =='__main__':
    main()
