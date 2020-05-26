programfile=open('/ws/mnist_for_docker.py','r')
code=programfile.read()
if 'keras' in code:
  if 'Conv2D' or 
'Convolution2D' in code:
    print('kerasCNN')
  else:
    print('not kerasCNN')
 else:
    ('code is not of deep learning')        