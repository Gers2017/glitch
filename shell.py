from glitch import run

while True:
  text = input("glitch >>> ")
  if text == "exit()":
    break
  result, errStr = run(text)
  if errStr : 
    print(errStr)
    break
  else: print(result)
  