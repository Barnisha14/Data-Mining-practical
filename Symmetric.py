# palin function to check whether string palindrome or not
def palin(string): 

  # declare and initialize with the starting and ending indexes
  st = 0
  end = len(string)-1
  f = 0

  # loop comparing letters moving from start to end and from end to start
  while(st<end): 

    if (string[st]== string[end]): 
      
      st += 1
      end -= 1
      
    else: 
      f = 1
      break; 
  # if loop with f as condition    
  if f == 0: 
    print("The entered string is palindrome") 
  else: 
    print("The entered string is not palindrome") 
    
# symm function to check string symmetrical or not
def symm(string): 
  
  l = len(string) 
  flag = 0
  
  # to check length of string even or odd 
  # to calculate middle value accordingly
  if l%2 == 0: 
    mid = l//2 # for even length
  else: 
    mid = l//2 + 1 # for odd length
    
  s1 = 0  # starting for first portion of string
  s2 = mid # starting for rest portion of string after middle value
  
  while(s1 < mid and s2 < l): 
    
    if (string[s1] == string[s2]): # comparing from start of both portions 
                                  # of given string
      s1 = s1 + 1
      s2 = s2 + 1
    else: 
      flag = 1
      break
  

  if flag == 0: 
    print("The entered string is symmetrical") 
  else: 
    print("The entered string is not symmetrical") 
    
# Main code 
string = input("Enter the string: ")
palin(string) 
symm(string)