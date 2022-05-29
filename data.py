import pandas as pd

clean_block_data = pd.read_csv('clean_block_data.csv')

#test_clean_block_data = pd.read_csv('test_clean_block_data.csv')

supply = pd.read_csv('supply.csv')

supply_t = supply.transpose()

supply_t.rename({'0': 'details', '1': 'stats'}, axis=1, inplace=True)

halving = pd.read_csv('halvings.csv')
header = pd.read_csv('clean_blockheader.csv')

bitcoin_supply = [supply['issuance_remaining'][0], int(supply['total_amount'][0])]

bitcoin_supply_titles = ['Issuance Remaining', 'Circulating Supply']