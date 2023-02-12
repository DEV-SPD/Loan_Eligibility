import pickle
import numpy as np
import streamlit as st

with open('Loan_Eligibility', 'rb') as f:
    model = pickle.load(f)


def loan_eligibility(input):
    np_array = np.array(input)
    reshaped_array = np_array.reshape(1, -1)
    a = model.predict(reshaped_array)
    if (a[0] == 0):
        return 'Sorry ,You are Not Eligible For Loan'
    else:
        return 'Granted'

def main():
    st.header("LOAN STATUS CHECK")
    st.info("USING FOLLOWING CODE FILL THE FORM")
    st.info('MALE/FEMALE--> 1/0')
    st.info('Graduate/Undergraduate--> 1/0')
    st.info('Married/Unmarried --> 1/0')
    st.info('Yes/No --> 1/0')
    st.info('Rural/Urban/SemiUrban --> 0/1/2')

    Gender = st.text_input("ENTER YOUR GENDER : ")
    MaritalStatus = st.text_input("ENTER YOUR MARITAL-STATUS : ")
    Dependents = st.text_input("ENTER YOUR DEPENDENTS : ")
    Education = st.text_input("ENTER YOUR EDUCATIONAL STATUS : ")
    Self_Employed = st.text_input("ARE YOU SELF EMPLOYED? : ")
    ApplicantIncome = st.text_input("ENTER YOUR INCOME : ")
    CoApplicantIncome = st.text_input("ENTER CO-APPLICANT INCOME : ")
    LoanAmount = st.text_input("ENTER LOAN AMOUNT : ")
    Loan_Amount_Term = st.text_input("ENTER LOAN AMOUNT TERM : ")
    Credit_History = st.text_input("ENTER CREDIT HISTORY : ")
    PropertyArea = st.text_input("ENTER LOCATION OF PROPERTY AREA : ")

    loan = ''

    if st.button('SUBMIT'):
        loan = loan_eligibility([Gender, MaritalStatus, Dependents, Education, Self_Employed, ApplicantIncome,
                                 CoApplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, PropertyArea])
        st.success(loan)


if __name__ == '__main__':
    main()