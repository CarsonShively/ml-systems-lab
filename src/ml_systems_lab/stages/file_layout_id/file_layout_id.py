from ml_systems_lab.config import STAGING
from ml_systems_lab.stages.file_layout_id.file_layout_spec import VALID_EXTENSIONS, IGNORED_EXTENSIONS, IGNORED_FILENAMES, FileLayout, EXTENSION_TO_FIELD, VALID_LAYOUTS
from ml_systems_lab.stages.file_layout_id.invalid_files_error import InvalidFilesError
from ml_systems_lab.stages.file_layout_id.unsupported_layout_error import UnsupportedLayoutError
from pathlib import Path
from collections import defaultdict

def file_layout_id() -> str:
    staging = Path(STAGING)
    
    invalid_files = []
    valid_files = defaultdict(int)
    
    for file in staging.rglob("*"):
        if not file.is_file():
            continue
        
        if file.suffix in IGNORED_EXTENSIONS or file.name in IGNORED_FILENAMES:
            continue
        elif file.suffix in VALID_EXTENSIONS:
            valid_files[file.suffix] += 1
        else:
            invalid_files.append(file.name)
        
    if invalid_files:
        raise InvalidFilesError(invalid_files=invalid_files)     

    layout_values = {}
    
    for extension, count in valid_files.items():
        field = EXTENSION_TO_FIELD[extension]
        if count == 1:
            layout_values[field] = "one"
        else:
            layout_values[field] = "multiple"
            
    layout = FileLayout(**layout_values)
    
    for layout_id, valid_layout in VALID_LAYOUTS.items():
        if layout == valid_layout:
            return layout_id
    
    raise UnsupportedLayoutError(layout)