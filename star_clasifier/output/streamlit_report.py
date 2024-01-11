import streamlit as st
import numpy as np
import plotly.graph_objects as go
import tensorflow as tf
import matplotlib.pyplot as plt

st.markdown('''
    # Star Classifier Report
    
    Welcome throughout this repot I will summarize the proces of
    my Star Classifier proyect.

''')

st.markdown('''
    ## Business understanding
    
    The SDSS has been searching for DataScientist and they ask you to join their team.

    For this job you need to gather data from de SDSS survey and create a star classifier system.

    In this project I will follow the **CRISP-DM model**

    The CRoss Industry Standard Process for Data Mining (CRISP-DM) is a process model that serves as the base for a data science process. It has six sequential phases:

    - Business understanding – What does the business need?
    - Data understanding – What data do we have / need? Is it clean?
    - Data preparation – How do we organize the data for modeling?
    - Modeling – What modeling techniques should we apply?
    - Evaluation – Which model best meets the business objectives?
    - Deployment – How do stakeholders access the results?

''')

st.markdown('''
    ## Data understanding – What data do we have / need? Is it clean?

    ### Collect initial data
    I couldn't create a connection between the ipynb and the SDSS 
    RestApi to retrevie the data becasue is not available any more, 
    what I can do to gather the data is to consult the Cassjob 
    online data base and download it in csv.

    ![query](star_clasifier\images\query.png)
    ![result]("star_clasifier\images\result.png")

''')
