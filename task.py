import re 
with open ("file.log", 'r') as f:
   content=f.read()
   x=re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
   print(set(x))
with open ("result.log", 'w') as f:
   for email in set(x):
      f.write(email + '\n')