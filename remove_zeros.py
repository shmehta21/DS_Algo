l = [{'a': 1, 'b': 0}, {'c': 2, 'd': 3}, {'c': 2, 'd': 3}, {'g': 8, 'h': 1}, {'g': 8, 'h': 1}, {'i': 0, 'j': 1}]
for item in l:
  vals = item.values()
  if 0 in vals or None in vals:
  	l.remove(item)
  
  	
  	 

print(f'Result list -- {l}')