from setuptools import find_packages
import setuptools 

import os

# Read the contents of your README file
def read_readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("Warning: README.md not found.")
        return ''

# Read the requirements from the requirements.txt file
def read_requirements():
    req_file = 'requirements.txt'
    try:
        with open(req_file, 'r') as f:
            return f.read().splitlines()
    except UnicodeDecodeError:
        # If UTF-8 decoding fails, try with 'utf-8-sig' for BOM-encoded files
        try:
            with open(req_file, 'r', encoding='utf-8-sig') as f:
                return f.read().splitlines()
        except UnicodeDecodeError:
            # If that fails too, try with 'latin1'
            with open(req_file, 'r', encoding='latin1') as f:
                return f.read().splitlines()
    except FileNotFoundError:
        print(f"Warning: {req_file} not found. Proceeding without specified requirements.")
        return []

setuptools.setup(
    name='Summarizer',
    version='0.1.0',
    description='A Python library for summarizing code responses and handling JSON data.',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='Dhruv Soni (Dhruv-net)',
    author_email='soni0682@gmail.com',
    url='https://github.com/yourusername/Summarizer',  # Replace with your actual repo URL
    packages=find_packages(exclude=['tests*']),
    install_requires=read_requirements(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    include_package_data=True,
    zip_safe=False,
)