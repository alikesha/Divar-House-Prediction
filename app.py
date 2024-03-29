import streamlit as st
import utils 
import numpy as np
import pandas as pd
import joblib

columns = ['Area',	'Room'	,'Parking', 'Warehouse'	,'Elevator', 'Address']
       #     'Shahran', 'Pardis', 'Shahrake Qods', 'Shahrake Gharb',
       # 'North Program Organization', 'Andisheh', 'West Ferdows Boulevard',
       # 'Narmak', 'Saadat Abad', 'Zafar', 'Islamshahr', 'Pirouzi',
       # 'Shahrake Shahid Bagheri', 'Moniriyeh', 'Velenjak', 'Amirieh',
       # 'Southern Janatabad', 'Salsabil', 'Zargandeh', 'Feiz Garden',
       # 'Water Organization', 'ShahrAra', 'Gisha', 'Ray', 'Abbasabad',
       # 'Ostad Moein', 'Farmanieh', 'Parand', 'Punak', 'Qasr-od-Dasht',
       # 'Aqdasieh', 'Pakdasht', 'Railway', 'Central Janatabad',
       # 'East Ferdows Boulevard', 'Pakdasht KhatunAbad', 'Sattarkhan',
       # 'Baghestan', 'Shahryar', 'Northern Janatabad', 'Daryan No',
       # 'Southern Program Organization', 'Rudhen', 'West Pars', 'Afsarieh',
       # 'Marzdaran', 'Dorous', 'Sadeghieh', 'Chahardangeh', 'Baqershahr',
       # 'Jeyhoon', 'Lavizan', 'Shams Abad', 'Fatemi',
       # 'Keshavarz Boulevard', 'Kahrizak', 'Qarchak',
       # 'Northren Jamalzadeh', 'Azarbaijan', 'Bahar',
       # 'Persian Gulf Martyrs Lake', 'Beryanak', 'Heshmatieh',
       # 'Elm-o-Sanat', 'Golestan', 'Shahr-e-Ziba', 'Pasdaran',
       # 'Chardivari', 'Gheitarieh', 'Kamranieh', 'Gholhak', 'Heravi',
       # 'Hashemi', 'Dehkade Olampic', 'Damavand', 'Republic', 'Zaferanieh',
       # 'Qazvin Imamzadeh Hassan', 'Niavaran', 'Valiasr', 'Qalandari',
       # 'Amir Bahador', 'Ekhtiarieh', 'Ekbatan', 'Absard', 'Haft Tir',
       # 'Mahallati', 'Ozgol', 'Tajrish', 'Abazar', 'Koohsar', 'Hekmat',
       # 'Parastar', 'Lavasan', 'Majidieh', 'Southern Chitgar', 'Karimkhan',
       # 'Si Metri Ji', 'Karoon', 'Northern Chitgar', 'East Pars', 'Kook',
       # 'Air force', 'Sohanak', 'Komeil', 'Azadshahr', 'Zibadasht',
       # 'Amirabad', 'Dezashib', 'Elahieh', 'Mirdamad', 'Razi', 'Jordan',
       # 'Mahmoudieh', 'Shahedshahr', 'Yaftabad', 'Mehran', 'Nasim Shahr',
       # 'Tenant', 'Chardangeh', 'Fallah', 'Eskandari', 'Shahrakeh Naft',
       # 'Ajudaniye', 'Tehransar', 'Nawab', 'Yousef Abad',
       # 'Northern Suhrawardi', 'Villa', 'Hakimiyeh', 'Nezamabad',
       # 'Garden of Saba', 'Tarasht', 'Azari', 'Shahrake Apadana', 'Araj',
       # 'Vahidieh', 'Malard', 'Shahrake Azadi', 'Darband', 'Vanak',
       # 'Tehran Now', 'Darabad', 'Eram', 'Atabak', 'Sabalan', 'SabaShahr',
       # 'Shahrake Madaen', 'Waterfall', 'Ahang', 'Salehabad', 'Pishva',
       # 'Enghelab', 'Islamshahr Elahieh', 'Ray - Montazeri',
       # 'Firoozkooh Kuhsar', 'Ghoba', 'Mehrabad', 'Southern Suhrawardi',
       # 'Abuzar', 'Dolatabad', 'Hor Square', 'Taslihat', 'Kazemabad',
       # 'Robat Karim', 'Ray - Pilgosh', 'Ghiyamdasht', 'Telecommunication',
       # 'Mirza Shirazi', 'Gandhi', 'Argentina', 'Seyed Khandan',
       # 'Shahrake Quds', 'Safadasht', 'Khademabad Garden', 'Hassan Abad',
       # 'Chidz', 'Khavaran', 'Boloorsazi', 'Mehrabad River River',
       # 'Varamin - Beheshti', 'Shoosh', 'Thirteen November', 'Darakeh',
       # 'Aliabad South', 'Alborz Complex', 'Firoozkooh', 'Vahidiyeh',
       # 'Shadabad', 'Naziabad', 'Javadiyeh', 'Yakhchiabad']

model = joblib.load('finalized_model.joblib')
st.title('What is your ideal house Price?  :🏠')

Area = st.text_input("Input area" , "1234")
Room = st.selectbox("Choose number of room", [0,1,2,3,4,5])
Parking = st.slider("Do you want parking (1(YES) | NO(0))",1,0)
Warehouse = st.slider("Do you want Warehouse (1(YES) | NO(0))", 1,0 )
Elevator = st.slider("Do you want Elevator (1(YES) | NO(0))", 1,0)
Address = st.selectbox("""Chosoose area""" , ['Shahran', 'Pardis', 'Shahrake Qods', 'Shahrake Gharb',
       'North Program Organization', 'Andisheh', 'West Ferdows Boulevard',
       'Narmak', 'Saadat Abad', 'Zafar', 'Islamshahr', 'Pirouzi',
       'Shahrake Shahid Bagheri', 'Moniriyeh', 'Velenjak', 'Amirieh',
       'Southern Janatabad', 'Salsabil', 'Zargandeh', 'Feiz Garden',
       'Water Organization', 'ShahrAra', 'Gisha', 'Ray', 'Abbasabad',
       'Ostad Moein', 'Farmanieh', 'Parand', 'Punak', 'Qasr-od-Dasht',
       'Aqdasieh', 'Pakdasht', 'Railway', 'Central Janatabad',
       'East Ferdows Boulevard', 'Pakdasht KhatunAbad', 'Sattarkhan',
       'Baghestan', 'Shahryar', 'Northern Janatabad', 'Daryan No',
       'Southern Program Organization', 'Rudhen', 'West Pars', 'Afsarieh',
       'Marzdaran', 'Dorous', 'Sadeghieh', 'Chahardangeh', 'Baqershahr',
       'Jeyhoon', 'Lavizan', 'Shams Abad', 'Fatemi',
       'Keshavarz Boulevard', 'Kahrizak', 'Qarchak',
       'Northren Jamalzadeh', 'Azarbaijan', 'Bahar',
       'Persian Gulf Martyrs Lake', 'Beryanak', 'Heshmatieh',
       'Elm-o-Sanat', 'Golestan', 'Shahr-e-Ziba', 'Pasdaran',
       'Chardivari', 'Gheitarieh', 'Kamranieh', 'Gholhak', 'Heravi',
       'Hashemi', 'Dehkade Olampic', 'Damavand', 'Republic', 'Zaferanieh',
       'Qazvin Imamzadeh Hassan', 'Niavaran', 'Valiasr', 'Qalandari',
       'Amir Bahador', 'Ekhtiarieh', 'Ekbatan', 'Absard', 'Haft Tir',
       'Mahallati', 'Ozgol', 'Tajrish', 'Abazar', 'Koohsar', 'Hekmat',
       'Parastar', 'Lavasan', 'Majidieh', 'Southern Chitgar', 'Karimkhan',
       'Si Metri Ji', 'Karoon', 'Northern Chitgar', 'East Pars', 'Kook',
       'Air force', 'Sohanak', 'Komeil', 'Azadshahr', 'Zibadasht',
       'Amirabad', 'Dezashib', 'Elahieh', 'Mirdamad', 'Razi', 'Jordan',
       'Mahmoudieh', 'Shahedshahr', 'Yaftabad', 'Mehran', 'Nasim Shahr',
       'Tenant', 'Chardangeh', 'Fallah', 'Eskandari', 'Shahrakeh Naft',
       'Ajudaniye', 'Tehransar', 'Nawab', 'Yousef Abad',
       'Northern Suhrawardi', 'Villa', 'Hakimiyeh', 'Nezamabad',
       'Garden of Saba', 'Tarasht', 'Azari', 'Shahrake Apadana', 'Araj',
       'Vahidieh', 'Malard', 'Shahrake Azadi', 'Darband', 'Vanak',
       'Tehran Now', 'Darabad', 'Eram', 'Atabak', 'Sabalan', 'SabaShahr',
       'Shahrake Madaen', 'Waterfall', 'Ahang', 'Salehabad', 'Pishva',
       'Enghelab', 'Islamshahr Elahieh', 'Ray - Montazeri',
       'Firoozkooh Kuhsar', 'Ghoba', 'Mehrabad', 'Southern Suhrawardi',
       'Abuzar', 'Dolatabad', 'Hor Square', 'Taslihat', 'Kazemabad',
       'Robat Karim', 'Ray - Pilgosh', 'Ghiyamdasht', 'Telecommunication',
       'Mirza Shirazi', 'Gandhi', 'Argentina', 'Seyed Khandan',
       'Shahrake Quds', 'Safadasht', 'Khademabad Garden', 'Hassan Abad',
       'Chidz', 'Khavaran', 'Boloorsazi', 'Mehrabad River River',
       'Varamin - Beheshti', 'Shoosh', 'Thirteen November', 'Darakeh',
       'Aliabad South', 'Alborz Complex', 'Firoozkooh', 'Vahidiyeh',
       'Shadabad', 'Naziabad', 'Javadiyeh', 'Yakhchiabad'])


def predict(): 
    row = np.array([Area , Room, Parking, Warehouse, Elevator, Address]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict(X)

    print(f"Your house price is : {prediction:.3f}")

trigger = st.button('Predict', on_click=predict)
