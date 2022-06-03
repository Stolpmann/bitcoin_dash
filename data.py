import pandas as pd

clean_block_data = pd.read_csv('clean_block_data.csv')

#test_clean_block_data = pd.read_csv('test_clean_block_data.csv')

supply = pd.read_csv('data/supply_pie_data.csv')

hash = pd.read_csv('data/networkhashps.csv')

supply_clean = pd.read_csv('data/supply_clean.csv')

supply_t = supply.transpose()

supply_t.rename({'0': 'details', '1': 'stats'}, axis=1, inplace=True)

halving = pd.read_csv('halvings.csv')
header = pd.read_csv('clean_blockheader.csv')

bitcoin_supply = [supply['Issuance Remaining'][0], int(supply['Circulating Supply'][0])]

bitcoin_supply_titles = ['Issuance Remaining', 'Circulating Supply']