import pandas as pd
import requests
from pathlib import Path

dataset_url = "https://data.gov.lv/dati/api/3/action/package_show"
resp = requests.get(dataset_url, params={"id": "personu-vardi"})
resources = resp.json()["result"]["resources"]

out_dir = Path("personu_vardi_data")
out_dir.mkdir(exist_ok=True)

files = []

for r in resources:
    url = r["url"]
    filename = url.split("/")[-1]
    path = out_dir / filename

    print(f"Downloading {filename}...")

    content = requests.get(url).content
    path.write_bytes(content)

    files.append(path)