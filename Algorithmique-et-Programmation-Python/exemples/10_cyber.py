"""Analyse locale uniquement : aucun paquet émis et aucune capture réseau."""

from scapy.all import IP, UDP, Raw
from cryptography.fernet import Fernet, InvalidToken

packet = (
    IP(src="192.0.2.10", dst="192.0.2.20")
    / UDP(sport=12000, dport=12001)
    / Raw(b"temperature=24.5")
)
decoded = IP(bytes(packet))
assert decoded[UDP].dport == 12001
print(decoded.summary())
vault = Fernet(Fernet.generate_key())
token = vault.encrypt(b"temperature=24.5")
assert vault.decrypt(token) == b"temperature=24.5"
altered = bytearray(token)
altered[len(altered) // 2] ^= 1
try:
    vault.decrypt(bytes(altered))
except InvalidToken:
    print("Altération détectée")
else:
    raise AssertionError("Le token altéré aurait dû être rejeté")
