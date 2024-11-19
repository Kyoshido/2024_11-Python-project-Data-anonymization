##############################################################################
##############################################################################
##############################################################################

"""
Generate new data using synthezizer provided by Mostly AI.
"""

# Load packages
import pandas as pd
from mostlyai import MostlyAI
import random # for random.seed()

# Load data
path = 'data/data_v2.parquet'
df = pd.read_parquet(path)

# Mostly Ai synthetizer ------------------------------------------------------

# initialize client
# api_key = ""
mostly = MostlyAI(
    api_key = api_key, 
    base_url = 'https://app.mostly.ai'
)

# train a generator
config = {
    "name": "Machiavellianism dataset",
    "tables": [
        {
            "name": "Mach",
            "data": df, 
            "model_configuration": {
                "value_protection": False,
                "rare_category_replacement_method": "CONSTANT",
                "privacy_mode": "BALANCED",
                "preserve_relationships": True
            }
        }
    ]
}
g = mostly.train(
    config = config
)

# generate a synthetic dataset
n_size = df.shape[0]
seed = random.seed(202409)
synth = mostly.generate(generator = g, 
                        seed = seed,
                        size = n_size
)

# Extract configuration
config = synth.config()
# config

# Extract synthetic data
synth_data = synth.data()

# Save ----------------------------------------------------------------------

# Save config
config_path = f"config_MostlyAI.txt"
with open(config_path, 'w', encoding='utf-8') as file:
    file.write(str(config))

# Save to csv
synth_path = f"synth/synth_MostlyAI.csv"
synth_data.to_csv(synth_path, 
                 index=False)

# Save to parquet 
synth_data.to_parquet('synth/synth_MostlyAI.parquet')

##############################################################################
##############################################################################
##############################################################################