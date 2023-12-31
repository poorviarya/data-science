import pandas as pd
import statsmodels.api as sm

churn = pd.read_csv(r"C:\DSPR_Data_Sets\Website Data Sets\churn")
churn_ind = pd.get_dummies(churn['Churn'], drop_first = True)

X = pd.DataFrame(churn_ind)
X = sm.add_constant(X)
X.columns = ['const', 'Churn_True']

y = pd.DataFrame(churn[['CustServ Calls']])
poisreg01 = sm.GLM(y, X.astype(float), family = sm.families.Poisson()).fit()
print(poisreg01.summary())
