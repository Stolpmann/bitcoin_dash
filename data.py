import pandas as pd
import numpy as np
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
utxo = clean_block_data['utxo_increase']
utxo_cumulative = utxo.cumsum()
utxo_cumulative.to_csv("data/utxo_cumulative.csv")
utxo = pd.read_csv('data/utxo_cumulative.csv')

output_type = ['Pubkey/Script Hash', 'SegWit Hash']

nonsw_txs = clean_block_data['txs'] - clean_block_data['swtxs']
sum_nonsw_txs = np.sum(nonsw_txs)
sum_sw_txs = np.sum(clean_block_data['swtxs'])

output_type_data = [sum_nonsw_txs, sum_sw_txs]