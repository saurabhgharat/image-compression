
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()
    
setup(
  name = 'image-compression',        
  packages = ['image-compression'],   
  version = '0.3',     
  license='MIT',        
  description = 'compress image without losing quality',  
  long_description=readme(),
  long_description_content_type='text/markdown'
  author = 'Saurabh Gharat',                   
  author_email = 'saurabhhgharat9@gmail.com',      
  url = 'https://github.com/saurabhgharat',   
  download_url = 'https://github.com/saurabhgharat/image-compression/archive/0.4.tar.gz',   
  keywords = ['compression', 'image', 'python','django'],   
  install_requires=[            
          'pillow'
          
      ],
  classifiers=[
    'Development Status :: '4 - Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
