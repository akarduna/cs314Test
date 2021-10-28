# t16 Interop Report for Port 31416

The issues listed in this report describe possible problems this with team's client or server found by students on other teams.

### Client

These issues occurred when this team's client attempted to operate with the specified server port for another team.

| sprint | server | issue or none found |
| :--- | :--- | :--- |
| 3 | t12 | Unable to connect to server (no error message), likely because distances is unsupported |
| 3 | t01 | None Found - able to connect |
| 3 | t22 | Unable to connect to server. When trying other servers, some work (features aren't displayed), presumably those that don't have distances supported |
| 3 | t13 | able to connect to server, however, console shows: "bundle.js:2 Server config response json is invalid. Check the Server."|

### Server

These issues occurred when another team's client on the specified port attempted to operate with this teams server. 

| sprint | client | issue or none found |
| :--- | :--- | :--- |
| 3 | t12 | Unable to connect to server (Server doesn't support: distances) |
| 3 | t01 | none found - able to connect|
| 3 | t22 | Can connect to server, but t16 server says distances isn't supported. However, distances is implemented and working, sending API requests to the correct server |
|3 | t13 | Nothing found, connects to server |

