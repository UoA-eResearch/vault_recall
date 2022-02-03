#!/usr/bin/env python3

from glob import glob
from tqdm import tqdm
import pandas as pd # CSV operations
import sys
import time
import os

files = sys.argv[1:]

try:
    # Read prior recall status results, if they exist
    df = pd.read_csv("~/recall_progress.csv")
except:
    df = pd.DataFrame()

if not files:
    # If the user doesn't specify which files to check recall status for, just go get updated status for the existing files known in recall_progress.csv
    files = df.filepath.unique()

print(f"Checking {len(files)} files")

rows = []
for f in files:
    stat = os.stat(f)
    current_size_bytes = stat.st_blocks * 512
    actual_size_bytes = stat.st_size
    pct = round(current_size_bytes/actual_size_bytes*100, 2)
    print(f"{f}: {current_size_bytes/1000/1000}MB / {actual_size_bytes/1000/1000}MB ({pct}%)")
    rows.append({
        "filepath": f,
        "timestamp": pd.Timestamp.now(),
        "current_size_bytes": current_size_bytes,
        "actual_size_bytes": actual_size_bytes
    })
df.append(rows).to_csv("~/recall_progress.csv", index=False)
