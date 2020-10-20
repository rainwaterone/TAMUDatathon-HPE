import streamlit as st
import numpy as np
import pandas as pd

st.title("TAMU Datathon")

df = pd.read_excel("https://urban-data-catalog.s3.amazonaws.com/drupal-root-live/2020/06/08/NHGIS_District_data.xlsx")
df['Poverty'] = df['Children 5-17 (SAIPE Estimate)']*df['% Poverty (SAIPE Estimate)']
df['Number of Single Parents'] = df['Children 5-17 (SAIPE Estimate)']*df['% Single Parent Estimate']
df['Number of Vulnerable Household'] = df['Children 5-17 (SAIPE Estimate)']*df['% HHs With Vulnerable Job Estimate']
df['Number of Children without_Internet'] = df['Children 5-17 (SAIPE Estimate)']*df['% No Computer or Internet Estimate']

df.columns = ['School ID', 'State', 'District', 'Children', '% Poverty', '% Single Parent', 'Single Parent Estimate Error',
             '% Vulnerable Household', 'Vulnerable Household Error', '% Crowded Condition', 'Crowded Condition Error',
             '% No Computer', 'No Computer Error', '% Children with disability', 'Children with Disability Error',
             'Ling. Isolated Children',' Isolated Children Error', 'Poverty','Number of Single Parents',
             'Number of Vulnerable Household', 'Number of Children without Internet']


list_of_param = ['Poverty', 'Number of Single Parents', 'Number of Children without Internet', 'Number of Vulnerable Household']
attributes = st.multiselect( "Choose Parameters",list_of_param, ['Poverty'] )

st.write("Filter the data: ")
if st.checkbox('By State'):
    df_State = 100*df.groupby('State')[attributes].sum()
    #plot.figure()
    st.bar_chart(df_State)

    st.write(
        "Here is the data: "
        )


elif st.checkbox('USA'):

    st.write(
        "Here is the data: "
        )




# Filter by state
# working on this
