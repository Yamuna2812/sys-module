import sys 
print("Total arguments:",len(sys.argv))

for i in range (len(sys.argv)):
    print(f"Argument{i}={sys.argv[i]}")
    