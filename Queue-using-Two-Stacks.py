"""
Title     : Queue using Two Stacks
Domain    : Python
Author    : Fredy
"""

# stackpush - 
# stackdelete -


q = int(input())
stackpush = []
stackdelete = []
for i in range(q):
  t = list(input().split())
  # equeue
  if t[0] == '1':
    stackpush.append(t[1])
    
    
  # dequeue
  elif t[0] == '2':
    if not stackdelete:
      while stackpush:
        stackdelete.append(stackpuush.pop())
    stackdelete.pop()
  
  
    
