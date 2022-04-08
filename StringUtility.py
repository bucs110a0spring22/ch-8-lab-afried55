class StringUtility:
  def __init__(self, string = ''):
    '''
    This function initializes a StringUtility object
    args: self (StringUtility object), string (str)
    '''
    self.original = string
  
  def __str__(self):
    '''
    This function sets a string that is returned when a StringUtility object is turned into a string.
    args: self (StringUtility object)
    returns: self.original (str)
    '''
    return self.original
  
  def vowels(self):
    '''
    This function counts the vowels in a string and returns this number as a string of the number or 'many'.
    args: self (StringUtility object)
    returns: str'''
    return ("many" if (sum([self.original.count(i) for i in "aeiouAEIOU"])>= 5) else str(sum([self.original.count(i) for i in "aeiouAEIOU"])))
  
  def bothEnds(self):
    '''This function returns a string made of the first 2 and last 2 chars of the original string, unless the string length is less than or equal to 2.
    args: self (StringUtility object)
    returns: str'''
    return '' if (len(self.original) <= 2) else (self.original[0:2] + self.original[-2:])
  
  def fixStart(self):
    '''This function makes a string where all occurrences of it's first char have been changed to '*', but does not change the first char itself
    args: self (StringUtility object)
    returns: str
    '''
    return self.original if len(self.original)<=1 else self.original[0]+ (self.original.replace(self.original[0], "*"))[1:]
  
  def asciiSum(self):
    '''Computes the sum of all ascii values in the string
    args: self (StringUtility object)
    returns: int
    '''
    return sum([ord(i) for i in self.original])
  
  def cipher(self):
    '''Encodes a string by incrementing all letters by the length of the string
    args: self (StringUtility object)
    returns: cipherString (str)'''
    cipherString = ''
    for i in self.original:
      newOrd = ord(i) + len(self.original)
      if ord('a')<=ord(i)<=ord('z'):
        for x in range(ord('a'),ord('z')+1):
          if (newOrd-x)%26==0:
            cipherString = cipherString + chr(x)
      elif ord('A') <= ord(i) <= ord('Z'):
        for x in range(ord('A'),ord('Z')+1):
          if (newOrd-x)%26==0:
            cipherString = cipherString + chr(x)
      else:
        cipherString = cipherString + i
    return cipherString


  
