# t09 Interop Report for Port 31409

The issues listed in this report describe possible problems this with team's client or server found by students on other teams.

### Client

These issues occurred when this team's client attempted to operate with the specified server port for another team.

| sprint | server | issue or none found |
| :--- | :--- | :--- |
| 3 | 31403 | Does not display available features accuartly, server config responce json is invalid, bad arguments |
| 3 | 31410 | It does not change the server connection to 31410 - Errors thrown: "Server config response json is invalid. Check the Server"; "bad arguments - isJsonResponseValid(object: null, schema: [object Object])"; "Request to server failed : TypeError: Failed to fetch" |
| 3 | 31426 | unable to connect to t26 server, is your team using the correct schema? |
| 3 | 31407 | None found |

### Server

These issues occurred when another team's client on the specified port attempted to operate with this teams server. 

| sprint | client | issue or none found |
| :--- | :--- | :--- |
| 3 | 31403 | Failed to load resource, bad argument, server config responce json is invalid |
| 3 | 31410 | It does not change the server connection to 31410 - Error: "Server doesn't support required feature" |
| 3 | 31426 | Server connection listed config,find as unsupported despite connecting properly |
| 3 | 31407 | None found |
