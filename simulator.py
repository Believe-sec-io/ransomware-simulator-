from pathlib import Path
from typing import List

from crypto_engine import CryptoEngine


class RansomwareSimulator:
    """Safe ransomware simulation restricted to a dedicated lab directory."""

    ALLOWED_EXTENSION = ".simlocked"

    def __init__(self, lab_directory: str, key: bytes):
        self.lab_directory = Path(lab_directory).resolve()
        self.crypto = CryptoEngine(key)

        self.lab_directory.mkdir(parents=True, exist_ok=True)

    def _validate_path(self, file_path: Path) -> Path:
        """Ensure the target stays inside the configured lab directory."""
        resolved = file_path.resolve()

        try:
            resolved.relative_to(self.lab_directory)
        except ValueError:
            raise PermissionError(
                "Security restriction: file is outside the laboratory directory."
            )

        if not resolved.is_file():
            raise FileNotFoundError(f"File not found: {resolved}")

        return resolved

    def list_files(self) -> List[Path]:
        """Return regular files inside the lab directory."""
        return [
            path
            for path in self.lab_directory.rglob("*")
            if path.is_file() and not path.name.endswith(self.ALLOWED_EXTENSION)
        ]

    def encrypt_file(self, file_path: str) -> str:
        """Encrypt one file after validating the lab restriction."""
        path = self._validate_path(Path(file_path))

        if path.name.endswith(self.ALLOWED_EXTENSION):
            raise ValueError("The file is already simulated as encrypted.")

        return self.crypto.encrypt_file(str(path))

    def decrypt_file(self, file_path: str) -> str:
        """Decrypt one simulated encrypted file."""
        path = self._validate_path(Path(file_path))

        if not path.name.endswith(self.ALLOWED_EXTENSION):
            raise ValueError("Only .simlocked files can be decrypted.")

        return self.crypto.decrypt_file(str(path))

    def encrypt_all(self) -> List[str]:
        """Encrypt all eligible files in the laboratory."""
        encrypted = []

        for path in self.list_files():
            try:
                result = self.encrypt_file(str(path))
                encrypted.append(result)
            except Exception as error:
                print(f"[!] Could not process {path.name}: {error}")

        return encrypted
