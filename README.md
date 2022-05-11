# GeoData@SciLi Metadata Scripts

This repository contains a collection of scripts used for creating, updating, and validating XML metadata records for datasets produced by GeoData@SciLi at Brown University. We use a subset of Dublin Core elements and terms that align closely with the OpenGeoMetadata Aardvark schema.

* bwgis_dap.md: data application profile, describes the metadata standards we use
* bwgis_dc_schema.xsd: schema for validating our metadata
* bwgis_dc_template.xml:  blank xml file with place holders
* bwgis_dc_validate.py: script for validating metadata records against our schema, using the xmlschema module
* bwgis_dcxml.css: stylesheet for our metadata records
* update_xml_funcs.py: generic functions for updating metadata, designed to be read into scripts written for specific projects
* xml_copier_one_to_many.py: script that copies one metadata file and makes multiple copies using a different suffix for a range of years
* xml_copier_one_to_one.py: script that makes a copy of each metadata file in a folder and renames it using a suffix for a new year or month-year
* cleaning folder
  * prefix_scrub.py: script for removing DC namespace prefixes and declarations from an xml metadata record
* project folder
  * Holds scripts and metadata for individual projects. For each project, a python script modifies a batch of copied metadata records using Elementtree. In the real estate project (one new record to revise several years of earlier records for the same data), the script reads in changes from a manually created json file, and uses the json data, the year in XML file names, and functions in update_xml_funcs.py to create new records. In the mass transit project (several new records to revise one previous iteration of each record), the script relies on hardcoded values, file names, and the functions.
* xml_to_json folder (experimental)
  * dcxml_gbjson: python script that converts our Dublin Core XML records to geoblacklight json (metadata source folder has sample input and output)
  * gb_blank.json: empty json file that's read into the script as a template