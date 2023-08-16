# -*- coding: utf-8 -*-
"""
Batch metadata validation

Frank Donnelly GIS and Data Librarian
Brown University Library
Aug 16, 2022 / rev July 12, 2023
"""

from jsonschema import validate
from shutil import copy
import yaml,json,os

# Move up to the base folder 
# so you can move down to schemas and samples folders
os.chdir(os.path.join('..','..','..'))

schemafile=os.path.join('metadata','ogm','schemas','brown_aardvark_schema.json')
metafolder=os.path.join('data_public','ossdb','metadata')


with open(schemafile) as readfile:
    schema = json.load(readfile)

for f in os.listdir(metafolder):
    if f.endswith('.yaml'):
        metafile=os.path.join(metafolder,f)
        with open(metafile,'r') as readfile:
            metadata = yaml.safe_load(readfile)
            try:
                validate(metadata, schema)
                mdfile=os.path.join(metafolder,
                                    os.path.basename(metafile).split('.')[0]+'.md')
                copy(metafile,mdfile)
                print('Validation successful, created markdown copy for',os.path.basename(metafile))
            except Exception as e:
                print('Validation failed for',os.path.basename(metafile),'against',os.path.basename(schemafile))
                print(e.message)