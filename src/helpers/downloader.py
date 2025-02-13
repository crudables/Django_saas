import requests
from pathlib import Path


def download_to_local(url: str, outpath: Path, parent_mkdir = True):
    
    if  not isinstance(outpath,Path):
        raise ValueError(f"{outpath} must be a valid pathlib.Path object")
    
    if parent_mkdir:
        outpath.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        outpath.write_bytes(response.content)
        return True
    
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return False