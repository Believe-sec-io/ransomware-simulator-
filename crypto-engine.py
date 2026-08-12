from pathlib import Path
from cryptography.fernet import Fernet


class CryptoEngine:
    """Handles encryption and decryption for the ransomware simulator."""

    def __init__(self, key: bytes):
        self.cipher = Fernet(key)

    @staticmethod
    def generate_key() -> bytes:
        """Generate a new encryption key."""
        return Fernet.generate_key()

    def encrypt_file(self, file_path: str) -> str:
        """Encrypt a single file and create a .simlocked copy."""
        path = Path(file_path)

        if not path.is_file():
            raise FileNotFoundError(f"File not found: {path}")

        data = path.read_bytes()
        encrypted_data = self.cipher.encrypt(data)

        output_path = path.with_name(path.name + ".simlocked")
        output_path.write_bytes(encrypted_data)

        return str(output_path)

    def decrypt_file(self, file_path: str) -> str:
        """Decrypt a .simlocked file and restore its original name."""
        path = Path(file_path)

        if not path.is_file():
            raise FileNotFoundError(f"File not found: {path}")

        if not path.name.endswith(".simlocked"):
            raise ValueError("File does not have the .simlocked extension.")

        encrypted_data = path.read_bytes()
        decrypted_data = self.cipher.decrypt(encrypted_data)

        original_path = Path(str(path)[:-len(".simlocked")])
        original_path.write_bytes(decrypted_data)

        return str(original_path)
