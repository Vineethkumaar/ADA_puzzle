capacity = (8,5,3) # Max capacities of 3 jugs -> x,y,z
x = capacity[0]
y = capacity[1]
z = capacity[2]
memory = {} # to mark visited states
ans = [] # store solution path

def get_all_states(state):
  # Let the 3 jugs be called a,b,c
  a = state[0]
  b = state[1]
  c = state[2]
  if(a==4 or b==4):
      ans.append(state)
      return True
  if((a,b,c) in memory): # if current state is already visited earlier
      return False
  memory[(a,b,c)] = 1
  if(a>0):#empty jug a
      if(a+b<=y):#empty a into b
          if( get_all_states((0,a+b,c)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((a-(y-b), y, c)) ):
              ans.append(state)
              return True
      if(a+c<=z): #empty a into c
          if( get_all_states((0,b,a+c)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((a-(z-c), b, z)) ):
              ans.append(state)
              return True
  if(b>0):#empty jug b
      if(a+b<=x): #empty b into a
          if( get_all_states((a+b, 0, c)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((x, b-(x-a), c)) ):
              ans.append(state)
              return True
      if(b+c<=z):#empty b into c
          if( get_all_states((a, 0, b+c)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((a, b-(z-c), z)) ):
              ans.append(state)
              return True
  if(c>0):#empty jug c
      if(a+c<=x):#empty c into a
          if( get_all_states((a+c, b, 0)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((x, b, c-(x-a))) ):
              ans.append(state)
              return True
      if(b+c<=y):#empty c into b
          if( get_all_states((a, b+c, 0)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((a, y, c-(y-b))) ):
              ans.append(state)
              return True
  return False

initial_state = (8,0,0)
print("Solution: \n")
get_all_states(initial_state)
ans.reverse()
for i in ans:
  print(i)
