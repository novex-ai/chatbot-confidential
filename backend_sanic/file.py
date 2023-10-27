from datetime import datetime
from pathlib import Path
import re

from nanoid import generate  # type: ignore


def make_stored_filename(raw_filename: str) -> str:
    stored_filename = re.sub(r"[^a-zA-Z0-9_\-\.]", "-", raw_filename)
    stored_path = Path(stored_filename)
    raw_stem = stored_path.stem
    now = datetime.now()
    timestamp_str = now.strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
    new_stem = f"{timestamp_str}-{raw_stem}-{generate(size=8)}"
    stored_path = stored_path.with_stem(new_stem)
    return stored_path.name
