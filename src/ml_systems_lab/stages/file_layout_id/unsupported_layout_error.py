from ml_systems_lab.stages.file_layout_id.file_layout_spec import FileLayout
from dataclasses import asdict

class UnsupportedLayoutError(Exception):
    def __init__(self, unsupported_layout: FileLayout):
        self.unsupported_layout = unsupported_layout
        
        parts = []
        for type, count in asdict(unsupported_layout).items():
            parts.append(f"{type}={count}")
        
        message = f"Unsupported file layout: {', '.join(parts)}"
        super().__init__(message)