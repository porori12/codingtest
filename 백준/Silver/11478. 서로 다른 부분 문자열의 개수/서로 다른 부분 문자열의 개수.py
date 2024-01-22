String = input()
total_String = set()


for i in range(len(String)):
    for j in range(i, len(String)):
        total_String.add(String[i:j+1])
        
        
print(len(total_String))