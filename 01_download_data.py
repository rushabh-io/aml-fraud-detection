# 01_download_data.py
# This script downloads the IBM AML dataset from Kaggle

import os
import subprocess

print("📥 Downloading IBM AML Dataset...")
print("This is a large file (~400MB for HI-Small) — please be patient\n")

# Download from Kaggle
subprocess.run([
    "kaggle", "datasets", "download",
    "ealtman2019/ibm-transactions-for-anti-money-laundering-aml",
    "--path", "./aml_data"
])

# Unzip the downloaded file
print("\n📦 Unzipping files...")
subprocess.run([
    "python", "-c",
    """
import zipfile, os
with zipfile.ZipFile('./aml_data/ibm-transactions-for-anti-money-laundering-aml.zip', 'r') as z:
    z.extractall('./aml_data')
print("Done! Files are in ./aml_data/")
os.listdir('./aml_data')
    """
])

print("\n✅ You should see these files:")
print("   HI-Small_Trans.csv        ← the transactions (start here!)")
print("   HI-Small_Patterns.txt     ← ground truth fraud patterns")
print("   HI-Medium_Trans.csv       ← use later when HI-Small works")
print("   HI-Large_Trans.csv        ← production scale (180M rows)")