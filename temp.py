
 # conda update -n base -c defaults conda
#  conda install scikit-learn
#Example
from sklearn.datasets import load_iris
import pandas as pd
from Basefun import py2doc
iris= datasets.load_iris()
df=pd.DataFrame(iris.data).head()
mydoc= py2doc(df=df ,title="International System of Units",save=False)
mydoc= py2doc(df=df, doc=mydoc ,title="International System of Units",save=False)
mydoc= py2doc(df=df, doc=mydoc ,title="International System of Units",save=False)
py2doc(df=df, doc=mydoc ,title="International Sys", caption="Table One")
