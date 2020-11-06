#!/usr/bin/env python
# coding: utf-8

# # Iter2.09 Experiment Results - g13t8

# ## Summary
# We utlilsed the SciPy library to derive to perform the statistical test.
# For our experiment design, we conducted a within subject design with 20 participants. It follows a non-normal distribution as seenn in the histogram. and the indepedent variable used is a ratio data type.

# ## <span style='background:yellow'> 1.  Time Taken <span>

# We chose to use the <span style='background:yellow'> Wilcoxon paired sampled test</span> and will be using a 5% level of significant for the test. The reasons are as follows:
# - The data does not follow a normal distribution
# - The experiment is a within subject design
# - Time taken is a ratio data type

# ## Hypothesis
# Let **_A_** be the distribution for time taken by the participants to finish tasks using Version A. <br>
# Let **_B_** be the distribution for time taken by the participants to finish tasks using Version B.
# > H$_{0}$ : A = B <br> 
# > H$_{1}$ : A ≠ B

# ### 1. Analysing the DataFrame
# Let **vA_time** and **vB_time** represent the time taken for participants to complete the task using Version A and Version B respectively. <br>

# In[1]:


import pandas as pd
from pprint import pprint
import numpy as np

budd_df = pd.read_excel('budd.xlsx', sheet_name='overview')

# dataframe
# display(budd_df)

display(budd_df.describe())


# ### 2. Analysing the distribution
# The histogram does not has the shape of a normal curve <br>
# Thus, we can derive that it follows a **non-normal distribution**.

# In[2]:


import plotly.graph_objects as go

# vA_time
vA_time = np.array(budd_df['vA_time'])

figA = go.Figure(data=[go.Histogram(
    x=vA_time,
    cumulative_enabled=False,
    nbinsx=8,
    ybins=dict(start=0, end=4, size=0.5)
)])

figA.update_layout(
    title_text="Version A's Time Taken", # title of plot
    xaxis_title_text='Time Taken', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
)

figA.show()


# vB time taken
vB_time = np.array(budd_df['vB_time'])

figB = go.Figure(data=[go.Histogram(
    x=vB_time,
    cumulative_enabled=False,
    nbinsx=4,
    ybins=dict(start=0, end=4, size=0.5)
)])

figB.update_layout(
    title_text="Version B's Time Taken", # title of plot
    xaxis_title_text='Time Taken', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1, # gap between bars of the same location coordinates
    xaxis={'range': [0,120]}
)

figB.show()


# ### 3. Interpretation of Results

# In[3]:


import scipy.stats as stats
vA = stats.shapiro(budd_df['vA_time'])
vB = stats.shapiro(budd_df['vB_time'])
print(vA)
print(vB)


# In[4]:


result = stats.wilcoxon(budd_df['vA_time'], budd_df['vB_time'])
print(result)


# ## Conclusion
# <p style='font-weight=20px'>Since <span style='background:yellow'> $p$ = 0.006 is less than 0.05</span>, we <span style='background:yellow'> reject the null hypothesis </span>.<br> We conclude that there is sufficient evidence to claim that <span style='background:yellow'>the mean time taken is not equal between Version A and Version B</span>, at 5% significant level.</p>
