from internal.errors import Error, UnexpectedSymbolError
from internal.tokens import DIGITS, EMPTY, KEYWORDS, OPERATORS, SYMBOLS, TYPES

def try_get_token(char):
  if char in OPERATORS.keys(): 
    return (OPERATORS[char], char)
  elif char in SYMBOLS.keys():
    return (SYMBOLS[char], char)
  else:
    return None

class Lexer:
  def __init__(self, text):
    self.text = text
    self.pos = -1
    self.char = None
    self.advance()
  
  def advance(self):
    self.pos += 1
    self.char = self.text[self.pos] if self.pos < len(self.text) else None

  def get_number(self):
    num_str = ""
    dot_count = 0
    while self.char != None and self.char in DIGITS + ".":
      # check for decimal
      if self.char == ".":
        if dot_count == 1: break
        dot_count += 1
        num_str += "."
      # add digit
      else:
        num_str += self.char
      self.advance()
          
    if dot_count == 0:
      return (TYPES["int"], int(num_str))
    else:
      return (TYPES["float"], float(num_str))
  
  def get_keyword(self):
    keyword_str = ""
    bad_keyword = False

    while self.char != None and not self.char in EMPTY and not self.char in SYMBOLS and not self.char in OPERATORS:
      keyword_str += self.char
      self.advance()
    
    if keyword_str in KEYWORDS.keys() and not bad_keyword:
      return (KEYWORDS[keyword_str], keyword_str)
    else:
      return (UnexpectedSymbolError(f"{keyword_str} is not an expected symbol"), keyword_str)

  def get_tokens(self):
    tokens = []
    while self.char != None:
      if self.char in EMPTY:
        self.advance()
        continue
      
      # try to get OPERATORS and symbols
      tkn = try_get_token(self.char)
      if tkn: 
        tokens.append(tkn)
        self.advance()
      # get numbers
      elif self.char in DIGITS:
        tokens.append(self.get_number())
      else:
        # try to get keyword
        keyword_tkn = self.get_keyword()
        if keyword_tkn[0] != Error:
          tokens.append(keyword_tkn)
        else:
          return [], keyword_tkn
      
    return tokens, None
'''
RUN
'''
def run(text):
  lexer = Lexer(text)
  tokens, error = lexer.get_tokens()
  return tokens, error

