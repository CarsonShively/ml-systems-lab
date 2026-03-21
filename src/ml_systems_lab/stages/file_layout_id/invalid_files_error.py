class InvalidFilesError(Exception):
    def __init__(self, invalid_files: list[str]):
        self.invalid_files = invalid_files
        message = f"Invalid files: {', '.join(invalid_files)}"
        super().__init__(message)
        