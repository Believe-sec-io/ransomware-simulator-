from pathlib import Path

from simulator import RansomwareSimulator


LAB_DIRECTORY = Path("lab/sample_files")
KEY_FILE = Path("lab/.simulation.key")


def save_key(key: bytes) -> None:
    KEY_FILE.parent.mkdir(parents=True, exist_ok=True)
    KEY_FILE.write_bytes(key)


def load_key() -> bytes | None:
    if not KEY_FILE.exists():
        return None

    return KEY_FILE.read_bytes()


def print_banner() -> None:
    print("\n" + "=" * 50)
    print("          RANSOMWARE SIMULATOR")
    print("=" * 50)
    print("Educational / isolated laboratory")
    print("=" * 50)


def print_menu() -> None:
    print("\n[1] Generate encryption key")
    print("[2] List laboratory files")
    print("[3] Encrypt a file")
    print("[4] Encrypt all laboratory files")
    print("[5] Decrypt a file")
    print("[6] Exit")


def create_simulator() -> RansomwareSimulator | None:
    key = load_key()

    if key is None:
        print("\n[!] No encryption key found.")
        print("[!] Generate a key first.")
        return None

    return RansomwareSimulator(str(LAB_DIRECTORY), key)


def generate_key() -> None:
    if KEY_FILE.exists():
        print("\n[!] A simulation key already exists.")
        return

    key = RansomwareSimulator(
        str(LAB_DIRECTORY),
        b"0" * 32
    ).crypto.generate_key()

    save_key(key)

    print("\n[+] Encryption key generated.")
    print(f"[+] Key stored in: {KEY_FILE}")


def list_files() -> None:
    simulator = create_simulator()

    if simulator is None:
        return

    files = simulator.list_files()

    if not files:
        print("\n[*] No eligible files found.")
        return

    print("\nLaboratory files:")

    for index, file_path in enumerate(files, start=1):
        print(f"  [{index}] {file_path}")


def encrypt_file() -> None:
    simulator = create_simulator()

    if simulator is None:
        return

    file_path = input("\nEnter the laboratory file path: ").strip()

    try:
        result = simulator.encrypt_file(file_path)
        print(f"\n[+] Simulation encryption completed: {result}")
    except Exception as error:
        print(f"\n[!] Error: {error}")


def encrypt_all() -> None:
    simulator = create_simulator()

    if simulator is None:
        return

    confirmation = input(
        "\nEncrypt all eligible laboratory files? [y/N]: "
    ).strip().lower()

    if confirmation != "y":
        print("[*] Operation cancelled.")
        return

    results = simulator.encrypt_all()

    print(f"\n[+] {len(results)} file(s) processed.")


def decrypt_file() -> None:
    simulator = create_simulator()

    if simulator is None:
        return

    file_path = input("\nEnter the .simlocked file path: ").strip()

    try:
        result = simulator.decrypt_file(file_path)
        print(f"\n[+] File restored: {result}")
    except Exception as error:
        print(f"\n[!] Error: {error}")


def main() -> None:
    LAB_DIRECTORY.mkdir(parents=True, exist_ok=True)

    print_banner()

    while True:
        print_menu()

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            generate_key()

        elif choice == "2":
            list_files()

        elif choice == "3":
            encrypt_file()

        elif choice == "4":
            encrypt_all()

        elif choice == "5":
            decrypt_file()

        elif choice == "6":
            print("\n[*] Simulator stopped.")
            break

        else:
            print("\n[!] Invalid option.")


if __name__ == "__main__":
    main()
