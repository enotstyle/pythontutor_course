n = input()
k = n[n.find('h')+1:n.rfind('h')]
print(n[:n.find('h')+1] + k.replace('h', 'H') + n[n.rfind('h'):])