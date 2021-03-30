class Error:
  def __init__(self, err_name, details):
    self.err_name = err_name
    self.details = details
  def __str__(self):
    return f"{self.err_name}: {self.details}"

class IllegalCharError(Error):
  def __init__(self, details):
    super().__init__("Illegal character", details)

class UnexpectedSymbolError(Error):
  def __init__(self, details):
    super().__init__("Unexpected symbol", details)
