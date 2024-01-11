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
    ![result](star_clasifier\images\result.png)

''')

st.markdown('''
    # Star Classifier Report
    
    Welcome throughout this repot I will summarize the proces of
    my Star Classifier proyect.

''')


x = np.linspace(0, 50, 51)
y = x + 15 * np.random.randn(len(x))
st.write(y)

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=x, y=y, mode='markers')
)

st.plotly_chart(fig)

st.markdown('''
    ## Modelado de datos
    En los datos se observa un comportamiento lineal,
    por lo que se realiza un ajuste de una linea recta 
    con una regresion lineal simple.
    
    $$y = m*x + b$$
    
''')

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=(1,)))
model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mse')

history = model.fit(x, y, epochs=2000, verbose=0)

st.write('Perdida final:', history.history['loss'][-1])

x_loss = np.linspace(1, len(history.history['loss']),
                     len(history.history['loss']))
y_loss = history.history['loss']


fig = plt.figure()
plt.plot(x_loss, y_loss)
st.pyplot(fig)

y_pred = model.predict(x)
y_pred = y_pred.reshape(-1)
#st.write('Prediccion:', y_pred)

fig_2 = go.Figure()
fig_2.add_trace(go.Scatter(x=x, y=y, mode='markers'))
fig_2.add_trace(go.Scatter(x=x, y=y_pred, mode='lines'))
st.plotly_chart(fig_2)