class StringUtility:
  def __init__(self, string = ''):
    ''''''
    self.original = string
  
  def __str__(self):
    ''''''
    return self.original
  
  def vowels(self):
    ''''''
    return ("many" if (sum([self.original.count(i) for i in "aeiouAEIOU"])>= 5) else str(sum([self.original.count(i) for i in "aeiouAEIOU"])))
  
  def bothEnds(self):
    ''''''
    return '' if (len(self.original) <= 2) else (self.original[0:2] + self.original[-2:])
  
  def fixStart(self):
    '''
    '''
    return self.original if len(self.original)<=1 else self.original[0]+ (self.original.replace(self.original[0], "*"))[1:]
  
  def asciiSum(self):
    ''''''
    return sum([ord(i) for i in self.original])
  
  def cipher(self):
    ''''''
    #find ord + length, if length > ord(z) or ord(Z) - find the difference from ord(z) and add that to ord(a) or ord(A). Use lists
    empty = ''
    for i in self.original:
      neword = 0
      #PROF NOTES: instead of manually writing in the ascii values, let python do the work for you
      # try changing ALL the hard-coded ascii value to function calls and your code will work
      # for example, below would become
      #     if chr('a')<=ord(i)<=chr('z'):
      if ord('a')<=ord(i)<=ord('z'):
        neword = ord(i) + len(self.original)
        for x in range(ord('a'),ord('z')+1):
          if (neword-x)%26==0:
            neword = x
        empty = empty + chr(neword)
      elif ord('A') <= ord(i) <= ord('Z'):
        neword = ord(i) + len(self.original)
        for x in range(ord('A'),ord('Z')+1):
          if (neword-x)%26==0:
            neword = x
        empty = empty + chr(neword)
      else:
        empty = empty + i
    return empty

    #it might be wrapping around twice because it is so long!!!!!!

  
