# Statistical Methods by Python.



## Call in R
`
library(reticulate)
source_python('https://raw.githubusercontent.com/nedamhd/PyStat/master/Basefun.py')
options(reticulate.pandas_use_nullable_data_types = TRUE)

myres = py2doc(df=as.data.frame(df1), 
               title="International Sys", save = FALSE,
               caption="Table One")

py2doc(df=as.data.frame(df2), doc = myres,
               title="International Sys", 
               caption="Table One")
`
