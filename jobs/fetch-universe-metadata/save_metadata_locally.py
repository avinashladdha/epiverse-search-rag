from fetch_universe_metadata import fetch_universe_metadata
import json

if __name__ == "__main__":
    processed_metadata = fetch_universe_metadata("epiverse-trace")

    with open("metadata.json", "w", encoding="utf-8") as f:
        json.dump(processed_metadata, f, indent = 4)