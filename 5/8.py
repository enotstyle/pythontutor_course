n = input()
k = (n[n.find('h')+1:n.rfind('h')])
print(n[:n.find('h')+1] + k[::-1] + n[n.rfind('h'):])