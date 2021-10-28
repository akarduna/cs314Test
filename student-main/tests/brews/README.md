# Crowdsourced Tests

This directory contains crowdsourced test data for later in the semester.
This is done now so we can
* practice with Github and merge conflicts
* learn about JSONs and schemas
* work in teams
* pay attention to the details

This directory contains three crowdsourced test cases.

The test cases should be valid JSON objects (ie. must pass schema validation) using the (JSON Schema Validator)[https://www.jsonschemavalidator.net/]. 
The schemas for each file are listed below.

Remember that your goal is to prevent defects, both when you make the change and when you review/approve other peoples changes. 

## coloradoBrews.json Schema

```
{
  "$id": "https://example.com/address.schema.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "trip",
  "description": "list of places to visit",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "municipality": {
        "type": "string"
      },
      "latitude": {
        "type": "string",
        "pattern": "^[-+]?(?:90(?:(?:\\.0+)?)|(?:[0-9]|[1-8][0-9])(?:(?:\\.[0-9]+)?))$"
      },
      "longitude": {
        "type": "string",
        "pattern": "^[-+]?(?:180(?:(?:\\.0+)?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\\.[0-9]+)?))$"
      },
      "altitude": {
        "type": "string",
        "pattern": "^[0-9]+$"
      }
    },
    "required": [
      "name",
      "latitude",
      "longitude",
      "id",
      "municipality",
      "altitude"
    ],
    "additionalProperties": false
  }
}
```

## usBrews.json Schema

```
{
  "$id": "https://example.com/address.schema.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "trip",
  "description": "list of places to visit",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "municipality": {
        "type": "string"
      },
      "region": {
        "type": "string"
      },
      "latitude": {
        "type": "string",
        "pattern": "^[-+]?(?:90(?:(?:\\.0+)?)|(?:[0-9]|[1-8][0-9])(?:(?:\\.[0-9]+)?))$"
      },
      "longitude": {
        "type": "string",
        "pattern": "^[-+]?(?:180(?:(?:\\.0+)?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\\.[0-9]+)?))$"
      },
      "altitude": {
        "type": "string",
        "pattern": "^[0-9]+$"
      }
    },
    "required": [
      "name",
      "latitude",
      "longitude",
      "id",
      "municipality",
      "altitude",
      "region"
    ],
    "additionalProperties": false
  }
}
```

## worldBrews.json Schema

```
{
  "$id": "https://example.com/address.schema.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "trip",
  "description": "list of places to visit",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "municipality": {
        "type": "string"
      },
      "country": {
        "type": "string"
      },
      "latitude": {
        "type": "string",
        "pattern": "^[-+]?(?:90(?:(?:\\.0+)?)|(?:[0-9]|[1-8][0-9])(?:(?:\\.[0-9]+)?))$"
      },
      "longitude": {
        "type": "string",
        "pattern": "^[-+]?(?:180(?:(?:\\.0+)?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\\.[0-9]+)?))$"
      },
      "altitude": {
        "type": "string",
        "pattern": "^[0-9]+$"
      }
    },
    "required": [
      "name",
      "latitude",
      "longitude",
      "id",
      "municipality",
      "altitude",
      "country"
    ],
    "additionalProperties": false
  }
}
```

