# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

LOGGER = get_logger(__name__)


def run():

    st.write("# Andrew Burk's ECON 8320 Semester Project")

    st.markdown(
        """
        This dashboard will allow you to examine demographic variables
        based on union membership.

        In order to do this chose a metro area from the drop down
        and the line graphs will be populated with the chosen city's
        information.

        The demographics chosen for this demonstration are:
        - PEERNLAB union member,y/n
        - HEFAMINC Household-total family income in past 12 month
        - HETENURE Household-own/rent living quarters;
        - HRHTYPE Household-type of family/single individual;
        - PEEDUCA Demographics-highest level of school completed;
        - PRFTLF Labor Force-full time/part-time;
        - PTERNH1O Earnings-hourly pay rate, excluding overtime

        Data is from Current Population Survey from the US Census

    """
    )
    #read the csv
    df = pd.read_csv("https://github.com/andrewburk2024/andrew-burk-sem-proj/raw/main/CENSUS_CPS_DATA.csv")
    
    #creating a list of unique metro areas for dropdown
    df_dropdown = df["Metro Area"].unique()
    #sorting the unique list
    df_dropdown_sort = df_dropdown.sort()
    #creating dropdown list in streamlit and placing into variable for use in graphs
    option = st.selectbox(label = "Metro Area", options = df_dropdown)
    
    #union labeling
    union_labels = {
        1: "Union Member",
        2: "Non-Union Member"
    }

    #buiding union membership line graph looking at HEFAMINC
    df_selected_metro1 = df[df['Metro Area'] == option]
    family_income = {
    1: "Less Than $5,000",
    2: "5,000 To 7,499",
    3: "7,500 To 9,999",
    4: "10,000 To 12,499",
    5: "12,500 To 14,999",
    6: "15,000 To 19,999",
    7: "20,000 To 24,999",
    8: "25,000 To 29,999",
    9: "30,000 To 34,999",
    10: "35,000 To 39,999",
    11: "40,000 To 49,999",
    12: "50,000 To 59,999",
    13: "60,000 To 74,999",
    14: "75,000 To 99,999",
    15: "100,000 To 149,999",
    16: "150,000 or More"
    }  
    
    title1u = f"Union Member Total Family Income in Past 12 Months for {option}"
    title1nu = f"Non-Union Member Total Family Income in Past 12 Months for {option}"
    #matching union codes with labels
    df_selected_metro1["PEERNLAB"] = df_selected_metro1["PEERNLAB"].map(union_labels)
    #matching incomes with labels
    df_selected_metro1["HEFAMINC"] = df_selected_metro1["HEFAMINC"].map(family_income)
    
    union_data1 = df_selected_metro1[df_selected_metro1['PEERNLAB'] == 'Union Member']
    non_union_data1 = df_selected_metro1[df_selected_metro1['PEERNLAB'] == 'Non-Union Member']
    
    #fig1u is union membership incomes (split them because became messy when combined)
    fig1u = px.histogram(union_data1, x='Year', color='HEFAMINC', 
                      title=title1u, labels={'Year': 'Year', 'HEFAMINC': 'Total Family Income'},
                      category_orders={'HEFAMINC': list(family_income.values())})
    
    fig1nu = px.histogram(non_union_data1, x='Year', color='HEFAMINC', 
                      title=title1nu, labels={'Year': 'Year', 'HEFAMINC': 'Total Family Income'},
                      category_orders={'HEFAMINC': list(family_income.values())})
    
    st.plotly_chart(fig1u)
    st.plotly_chart(fig1nu)

    #buiding union membership line graph looking at HETENURE
    df_selected_metro = df[df['Metro Area'] == option]
    title1u = f"Union Member Total Family Income in Past 12 Months for {option}"
    title1nu = f"Non-Union Member Total Family Income in Past 12 Months for {option}"


    
    #buiding union membership line graph looking at HRHTYPE
    df_selected_metro = df[df['Metro Area'] == option]

    #buiding union membership line graph looking at PEEDUCA
    df_selected_metro = df[df['Metro Area'] == option]

    #buiding union membership line graph looking at PRFTLF
    df_selected_metro = df[df['Metro Area'] == option]

    #buiding union membership line graph looking at PTERNH1O
    df_selected_metro = df[df['Metro Area'] == option]

if __name__ == "__main__":
    run()