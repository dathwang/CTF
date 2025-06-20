from Crypto.Util.number import long_to_bytes

N = 140435453730354645791411355194663476189925572822633969369789174462118371271596760636019139860253031574578527741964265651042308868891445943157297334529542262978581980510561588647737777257782808189452048059686839526183098369088517967034275028064545393619471943508597642789736561111876518966375338087811587061841

C = 49352042282005059128581014505726171900605591297613623345867441621895112187636996726631442703018174634451487011943207283077132380966236199654225908444639768747819586037837300977718224328851698492514071424157020166404634418443047079321427635477610768472595631700807761956649004094995037741924081602353532946351

# Reverse the "Sahur" part
C += N

# Reverse the "Tung" part
while(C % 2 == 0):
    C //= 2

# C = pow(m,e) | e = 3
# This part means C = m^e = m^3

# Now C = m^3 => Get m and decode -> get the flag!
m_cubed = C

def cubicRoot(n):
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if mid**3 < n:
            low = mid + 1
        else:
            high = mid
    return low if low**3 == n else low - 1

m = cubicRoot(m_cubed)

# Convert to flag
flag = long_to_bytes(m).decode()
print(flag)
