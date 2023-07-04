###################### SAS put ###########################

# SAS

data df;
set df;
var1 = put(var2, 4.)
run;

# Python

df['var1'] = df['var2'].str.slice(0, 4)

# .str.slice() klipper ut karakterer fra en string variabel






####################### SAS merge #############################

# SAS

Data merged;
merge df1 (in=A) df2 (in=B);
by var;
run;

# Python

merged = pd.merge(df1, df2, on='var', how='inner')

# Hva vi har på 'how=' er viktig! 'Left' betyr at vi matcher på df1, mens 'right' betyr at vi gjør det på det andre. 
# Inner og outer matcher på begge datasett men endrer rekkefølgen på rader

# SAS

Data merged;
merge df1 (in=A) df2 (in=B);
by var;
if A;
run;


# Python

merged = pd.merge(df1, df2, on='var', how='left')

# Her (linja over) brukte jeg 'left' fordi SAS kommandoen har en 'if A;' linje som spesifiserer at vi matcher på df1. 
# Se denne nettsida her for mer info; https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html


###################### SAS Proc freqs statement ########################

# SAS - multiple conditions on one variable

proc freq data=df;
where col1 in ('1', 'a', '4', 'yh');
table col2;
run;

# Python

values = ['1', 'a', '4', 'yh']
display(df.loc[df['col1'].isin(values)]['col2'].value_counts())

# The Python "isin.()" function works the same as the SAS 'in'


# SAS - conditions on multiple variables

proc freq data=df;
where col1='' and col2 in ('A') and col3 < 3;
table col4 / list missing;
run;

# Python

display(df.loc[(df['col1'].isnull())&(df['col2']=='A')&(df['col3']<3)]['col4'].value_counts(dropna=False))


# SAS - singel condition

proc freq data=df;
where col1='';
table col2;
run;


# Here I run a Python versjon of the SAS proc freq command with a where statement (in this case where col1 is missing).
# I input the name of the dataset (v02001b), and the two relevant variables [pandas.series] ('avgjpers' and 'statusrollekid').

def frek_ved_missing(df, col1, col2):

    display(df.loc[df[col1].isnull()][col2].value_counts(dropna=False))

frek_ved_missing(v02001b, 'avgjpers', 'statusrollekid')

# If I do not wish to make a function I can also write it directly like so:

display(df.loc[df['col1'].isnull()]['col2'].value_counts(dropna=False))

# If I wish to have more conditions I can write it like this;

display(df.loc[(df['col1'].isnull()) & (df['col2'].notna())]['col3'].value_counts(dropna=False))

# In this code I am applying a 'mask' - i.e. Im not changing the data directly but creating a temporary copy on which I run the value_counts() command.
# A filter if you like. 
# And its all contained within the [ ] of the .loc function. 




######################## proc freqs fra SAS med flere variabler  ################################

proc freq data=df;
table var1*var2;
run;

# I Python:
display(pd.crosstab(df.var1, columns=df.var2).stack())

# eller denne:
display(pd.crosstab([df.var1, df.var2],  columns='Antall', margins=False))



######################## Lage nytt datasett med macro ##############################

når man skal legge 'aaret' til df'en. Men dette er også problematisk i SAS fordi et eller annet med globals.

globals()[f"df_{aaret}"] = kat



