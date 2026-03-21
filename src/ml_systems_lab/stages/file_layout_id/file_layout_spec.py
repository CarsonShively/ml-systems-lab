from dataclasses import dataclass
from typing import Literal

IGNORED_EXTENSIONS = {".md"}

IGNORED_FILENAMES = {"LICENSE"}

VALID_EXTENSIONS = {".json"}

EXTENSION_TO_FIELD = {
    ".json": "json"
}

CountState = Literal["none", "one", "multiple"]

@dataclass(frozen=True)
class FileLayout:
    json: CountState = "none"
    
VALID_LAYOUTS = {
    "single_json": FileLayout(json="one"),
    "multiple_json": FileLayout(json="multiple")
}