import pandas as pd

mappingDF = pd.read_csv('mapping.csv')
accountDF = pd.read_csv('account.csv')

cds = mappingDF.set_index('CDS').to_dict()
print(cds)

accountDF.columns = accountDF.columns.to_series().map(cds['CDM'])
print(accountDF.columns)

export_csv = accountDF.to_csv(r'convert.csv', index=None, header=True)
