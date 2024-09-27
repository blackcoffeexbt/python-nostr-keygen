from nostr.key import PrivateKey

private_key = PrivateKey()

public_key = private_key.public_key

print ("Generated new nostr keys")
print("");
print("Private keys");
print("------------")
print(f"**bech32** {private_key.bech32()}")
print(f"**hex** {private_key.hex()}")
print("Public keys");
print("----");
print(f"**bech32** {public_key.bech32()}")
print(f"**hex** {public_key.hex()}")
