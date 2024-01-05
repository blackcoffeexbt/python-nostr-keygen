from nostr.key import PrivateKey

private_key = PrivateKey()

public_key = private_key.public_key

print ("Generated new nostr keys")
print("");
print("Private keys");
print("------------")
print(f"Private key bech32: {private_key.bech32()}")
print(f"Private key hex: {private_key.hex()}")
print("------------")
print("Public keys");
print(f"Public key bech32: {public_key.bech32()}")
print(f"Public key hex: {public_key.hex()}")