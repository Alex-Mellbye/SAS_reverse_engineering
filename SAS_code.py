###################### SAS Proc freq med 'where' statement ########################

# SAS

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
