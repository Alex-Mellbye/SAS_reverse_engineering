
######################## proc freqs fra SAS med flere variabler  ################################

proc freq data=df;
table var1*var2;
run;

# I Python:
display(pd.crosstab(df.var1, columns=df.var2).stack())

# eller denne:
display(pd.crosstab([df.var1, df.var2],  columns='Antall', margins=False))
