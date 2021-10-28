# t12 Interop Report for Port 31412

The issues listed in this report describe possible problems this with team's client or server found by students on other teams.

### Client

These issues occurred when this team's client attempted to operate with the specified server port for another team.

| sprint | server | issue or none found |
| :--- | :--- | :--- |
| 3 | t04 | When connected to our server at port 31404, the distances and find features work fine. When the page first renders, their config request sends back an error message |
| 3 | t02 | none found |
| 3 | 31401 | none found |
| 3 | t23 | [console.log](#t23-consolelog)          |
| 3 | t23 | [ConfigResponse.json](#t23-configresponsejson)  |
| 3 | t23 | [getOriginalServerUrl](#t23-getoriginalserverurl) |
| 3 | t26 | none found |
| 3 | t13 | 'Server config response json is invalid. Check the Server.' When changing servers. (Tested on t13, t02, t04) |

### Server

These issues occurred when another team's client on the specified port attempted to operate with this teams server. 

| sprint | client | issue or none found |
| :--- | :--- | :--- |
| 3 | t04 | Could not connect to server, failure in the config request |
| 3 | t02 | none found |
| 3 | 31401 | none found |
| 3 | t23 | none found |
| 3 | t26 | none found |
| 3 | t13 | none found |


#### t23: console.log
The client is rampant with several calls to console.log.
This clutters console output and makes it hard to debug.

#### t23: ConfigResponse.json
The JSON schema for ConfigResponse.json is incorrect.

Found on the client (via devtools):
```javascript
{
    "description":"the APIs and optional properties supported by this server",
    "type":"array",
    "items":{
    "type":"string",
        "enum":["config","find","distance","tour","type","where","units","title"]
    }
}

```

And taken from the [product repo](https://github.com/CSU-CS-314-Fall-2021/product/blob/main/protocol/config/ConfigResponse.json):
```javascript
"features" : {
  "description": "the APIs and optional properties supported by this server",
  "type": "array",
  "items": {
    "type": "string",
    "enum": ["config", "find", "distances", "tour", "type", "where"]
  }
}
```

Note that the `distances` field differs.

#### t23: getOriginalServerUrl

It appears that portions of t12's client code use `getOriginalServerUrl` when it shouldn't.
One such instance is during the API call for calculating distances.
