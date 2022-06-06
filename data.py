import pandas as pd

# Mining View Data

supply = pd.read_csv('data/supply_pie_data.csv')

hash = pd.read_csv('data/networkhashps.csv')

supply_clean = pd.read_csv('data/supply_clean.csv')

halving = pd.read_csv('halvings.csv')

header = pd.read_csv('clean_blockheader.csv')

bitcoin_supply = [supply['Issuance Remaining'][0], int(supply['Circulating Supply'][0])]

bitcoin_supply_titles = ['Issuance Remaining', 'Circulating Supply']

# Timechain View Data

clean_block_data = pd.read_csv('clean_block_data.csv')

utxo = pd.read_csv('data/utxo_cumulative.csv')

output_type = ['Pubkey Hash', 'Script Hash', 'SegWit v0 Pubkey Hash', 'SegWit v0 Script Hash']

output_type_data = [supply['Issuance Remaining'][0], int(supply['Circulating Supply'][0])]
