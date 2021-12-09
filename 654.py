import streamlit as st

# w= float(input（'請輸人體重(KG)？“））
W = st.number_input（‘請輸人體重(KG)？‘)
h = st.number_input（'請輸人身高(M)？'）
confirm_input = st.button( ‘輪人確認”）

if confirm input:
    bmi=w/(h*h)
    #print('"BMI為',bmi)
    st.write('BMI為',bmi）
    if (bmi < 18):
        st.write('體重過輕，）
    elif (bmi < 24）：
        st.write('體重正常，）
    elif (bmi ＜ 27）：
        st.write('體重過重'）
    else:
        st.write('體重肥胖'）
