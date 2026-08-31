import sys,time
while 1:
 s=input('>>> ')
 if s in ('q','quit','exit'):
  sys.exit()
 try:
  v=eval(s,{},{})
  print(v)
 except Exception:
  print('error')
