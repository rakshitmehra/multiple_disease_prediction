import pickle
import streamlit as st
from streamlit_option_menu import option_menu

dia_model = pickle.load(open("./savedModels/diabetes.sav",'rb'))
heart_model = pickle.load(open("./savedModels/heart.sav",'rb'))
parkinsons_model = pickle.load(open("./savedModels/parkinsons.sav",'rb'))

with st.sidebar:
    
  selected = option_menu('Multiple Disease Prediction System',
                         ['Diabeties Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Disease Prediction'],
                         icons = ['activity', 'heart', 'person'],
                         default_index=0)
  
if(selected == 'Diabeties Prediction'):
    
        st.title('Diabetes Prediction Using ML')
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            Pregnancies = st.text_input('Number of Pregnanacies')
        with col2:
            Glucose = st.text_input('Glucose Level')
        with col3:
            BloodPressure = st.text_input('Blood Pressure Level')
        with col1:
            SkinThickness = st.text_input('Skin Thickness value')
        with col2:
            Insulin = st.text_input('Insulin Level')
        with col3:
            BMI = st.text_input('BMI value')
        with col1:
            DiabetiesPedigreeFunction = st.text_input('Diabeties Padgree Function value')
        with col2:
            Age = st.text_input('Age of a Person')
  
        diab_diagnosis = ''

        if st.button('Diabeties Test Result'):
            diab_prediction = dia_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetiesPedigreeFunction, Age]])
        
            if(diab_prediction[0]==1):
                diab_diagnosis = 'The person is Diabetic'
            else:
                diab_diagnosis = 'The person is not Diabetic'
        st.success(diab_diagnosis)

if(selected == 'Heart Disease Prediction'):
    
        st.title('Heart Disease Prediction Using ML')
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            age = st.text_input('Age')
        with col2:
            sex = st.text_input('Gender')
        with col3:
            cp = st.text_input('Chest Pain Types')
        with col1:
            trestbps = st.text_input('Resting Blood pressure')
        with col2:
            chol = st.text_input('Serum Cholestrol in mg/dl')
        with col3:
            fbs = st.text_input('fasting Blood Sugar > 120 mg/dl')
        with col1:
            restecg = st.text_input('Resting Electrographics Results')
        with col2:
            thalach = st.text_input('Maximum Heart Rate Achieved')
        with col3:
            exang = st.text_input('Exercise Induced Angina')
        with col1:
            oldpeak = st.text_input('ST Depression Induced by Exercise')
        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')
        with col3:
            ca = st.text_input('Major Vessels Coloured By Flourscopy')
        with col1:
            thal = st.text_input('thal: 0  = Normal, 1 = Fixed Defect, 2 = reversable Defect')
        
        heart_diagnosis = ''
  
        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
            
            if(heart_prediction[0]==1):
                heart_diagnosis = 'The person is having Heart Disease'
            else:
                heart_diagnosis = 'The person is not having Heart Disease'
        st.success(heart_diagnosis)
        
if(selected == 'Parkinsons Disease Prediction'):
    
        st.title('Parkinsons Disease Prediction Using ML')
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            fo = st.text_input('MVDP: Fo(Hz)')
        with col2:
            fhi = st.text_input('MVDP: Fhi(Hz)')
        with col3:
            flo = st.text_input('MVDP: Flo(Hz)')
        with col4:
            Jitter_percent = st.text_input('MVDP: Jitter(%)')
        with col5:
            Jitter_abs = st.text_input('MVDP: Jitter(Abs)')
        
        with col1:
            RAP = st.text_input('MVDP: RAP')
        with col2:
            PPQ = st.text_input('MVDP: PPQ')
        with col3:
            DDP = st.text_input('MVDP: DDP')
        with col4:
            Shimmer = st.text_input('MVDP: Shimmer')
        with col5:
            Shimmer_dB = st.text_input('MVDP: Shimmer(dB)')
            
        with col1:
            APQ3 = st.text_input('MVDP: APQ3')
        with col2:
            APQ5 = st.text_input('MVDP: APQ5')
        with col3:
            APQ = st.text_input('MVDP: APQ')
        with col4:
            DDA = st.text_input('Shimmer: DDA')
        with col5:
            NHR = st.text_input('NHR')
            
        with col1:
            HNR = st.text_input('MVDP: HNR')
        with col2:
            RPDE = st.text_input('RPDE')
        with col3:
            DFA = st.text_input('DFA')
        with col4:
            spread1 = st.text_input('spread1')
        with col5:
            spread2 = st.text_input('spread2')
            
        with col1:
            D2 = st.text_input('D2')
        with col2:
            PPE = st.text_input('PPE')
        
        parkinsons_diagnosis = ""
        
        if st.button("Parkinsons Test Results"):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            
            if(parkinsons_prediction[0] == 1):
                parkinsons_diagnosis = "The person has Parkinsons Disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinsons's Disease"
            
        st.success(parkinsons_diagnosis)