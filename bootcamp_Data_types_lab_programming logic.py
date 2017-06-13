def data_type(value=None):
  '''
  This function takes in a single argument and checks what data type is the argument
  then it outputs based on the requirements
  '''
  if type(value)==str:
      if len(value) > 0:
          return len(value)
  elif value ==None:
      return 'no value'
  elif isinstance(value,bool) == True:
    return value
  elif type(value) == int:
    if value < 100:
      return 'less than 100'
    elif value >100:
      return 'more than 100'
    else:
      return 'equal to 100'
  try:
      if type(value) == list:
          return value[2]
      
  except IndexError:
      return 'None'
      

            
    
  
      
    
        
            
      
    

  
    
