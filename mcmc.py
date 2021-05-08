from scipy import stats
import arviz as az
import numpy as np
import matplotlib.pyplot as plt
import pymc3 as pm
import seaborn as sns
import pandas as pd
from theano import shared
from sklearn import preprocessing
df=pd.read_csv("cyano_train.csv")
df.head()
with pm.Model() as model:
    mu = pm.Uniform('mu', lower=10, upper=20)
    sigma = pm.HalfNormal('sigma',sd=10)
    y = pm.Normal('y', mu=mu, sd=sigma, observed=df['Turb'].values)
    trace_g = pm.sample(1000, tune=1000)
az.plot_trace(trace_g)
