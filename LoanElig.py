import streamlit as st
import pickle

pickle_in=open('LoanElig.pkl','rb')
clf=pickle.load(pickle_in)

#st.markdown(unsafe_allow_html=True)
st.title('LOAN ELIGIBILITY')

a=st.selectbox('Enter Gender',('Male','Female'))
b=st.selectbox('Martial Status',('Married','Unmarried'))
c=st.number_input('Enter applicant income')
d=st.number_input('Enter Loan amount')
e=''
if a=='Male':
    a=0
else:
    a=1
if b=='Married':
    b=1
else:
    b=0
    
if st.button('PREDICT'):
    e=clf.predict([[a,b,c,d]]).squeeze()
    if e==0:
        st.success('Not Approved')
    else:
        st.success('Approved')

