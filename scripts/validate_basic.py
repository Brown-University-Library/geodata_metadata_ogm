# -*- coding: utf-8 -*-
"""
Basic metadata validation

Frank Donnelly GIS and Data Librarian
Brown University Library
Aug 16, 2022 / rev Aug 16, 2022
"""

from jsonschema import validate
from shutil import copy
import yaml,json,os

# Move up one level from scripts folder, 
# so you can move down to schemas and samples folders
os.chdir(os.path.dirname(os.getcwd()))

schemafile=os.path.join('schemas','brown_aardvark_schema.json')
metafile=os.path.join('sample_metadata','un_icsc_rpid_metadata.yaml')
mdfile=os.path.join('sample_metadata',
                    os.path.basename(metafile).split('.')[0]+'.md')

with open(schemafile) as readfile:
    schema = json.load(readfile)

with open(metafile, 'r') as readfile:
    metadata = yaml.safe_load(readfile)

try:
    validate(metadata, schema)
    print('Validation successful, created markdown copy')
    copy(metafile,mdfile)
except Exception as e:
    print('Validation failed for',metafile,'against',schemafile)
    print(e.message)