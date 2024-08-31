import secrets
from eth_utils import to_checksum_address

def generate_random_wallet():
    # Generate 20 random bytes (160 bits)
    random_bytes = secrets.token_bytes(20)
    
    # Convert to an Ethereum address with checksum
    return to_checksum_address(random_bytes.hex())

def save_wallets_to_file(filename, wallet_addresses):
    with open(filename, 'w') as f:
        for address in wallet_addresses:
            f.write(address + '\n')

def main():
    try:
        # Ask the user how many wallet addresses they want to generate
        num_wallets = int(input("Enter the number of random Ethereum wallet addresses to generate: "))
        
        if num_wallets <= 0:
            print("Please enter a positive integer.")
            return
        
        # Generate the specified number of random Ethereum addresses
        wallet_addresses = [generate_random_wallet() for _ in range(num_wallets)]
        
        # Save to a file
        save_wallets_to_file('wallets.txt', wallet_addresses)
        
        print(f"Generated {num_wallets} Ethereum wallet addresses and saved to wallets.txt")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
