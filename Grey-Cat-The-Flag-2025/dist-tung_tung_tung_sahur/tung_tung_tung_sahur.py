from Crypto.Util.number import getPrime, bytes_to_long

flag = "grey{flag_here}"

e = 3
p, q = getPrime(512), getPrime(512) # Generate two random 512-bit primes
print("p = ", p)
print("q = ", q)
N = p * q 
print("N = ", N)
m = bytes_to_long(flag.encode())
print("m = ", m)
C = pow(m,e)

assert C < N 
while (C < N):
    C *= 2
    print("Tung!")

# now C >= N

while (C >= N):
    C -= N 
    print("Sahur!")


print(f"{e = }")
print(f"{N = }")
print(f"{C = }")