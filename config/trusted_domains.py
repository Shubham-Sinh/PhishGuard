from pathlib import Path


def load_trusted_domains():
    file_path = Path(__file__).parent / "trusted_domains.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        domains = {
            line.strip().lower()
            for line in file
            if line.strip()
        }

    return domains