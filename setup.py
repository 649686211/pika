from distutils.core import setup
import os

try:
    os.stat("pika/spec.py")
except:
    import sys
    print >> sys.stderr, 'Autogenerated spec.py not found -- run make first!'
    sys.exit(1)

setup(name='pika',
      version='0.1',
      description='Pika Python AMQP Client Library',
      author='Tony Garnock-Jones',
      author_email='tonyg@rabbitmq.com',
      url='http://www.rabbitmq.com/',
      packages=['pika'],
      )
