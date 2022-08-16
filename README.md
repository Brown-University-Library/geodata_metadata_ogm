# GeoData@SciLi Metadata Scripts

This repository contains schemas and scripts used for validating YAML metadata records for datasets produced by GeoData@SciLi at Brown University. We use a subset elements and terms that align closely with OpenGeoMetadata's Aardvark schema. This area is a work in progress and will eventually grow to include scripts for updating metadata and validating records in bulk. We currently do not have a data repository; we are creating these records for a future in which we will, and to provide basic documentation for series that we are currently creating or purchasing.

* sample_metadata: sample records used for validation
* schemas: the original JSON Aardvark schema, the JSON schema for Brown which contains a subset of these elements with additional validation requirements, and Brown's data application profile that contains lists of elements, terms, standards, and requirements
* scripts: *validate_basic.py* uses the jsonschema, json, and yaml modules to validate one YAML record against a JSON schema, and if successful creates a copy in markdown for display on GitHub