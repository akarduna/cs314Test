# t03 Interop Report for Port 31403

The issues listed in this report describe possible problems this with team's client or server found by students on other teams.

### Client

These issues occurred when this team's client attempted to operate with the specified server port for another team.

| sprint | server | issue or none found |
| :--- | :--- | :--- |
| 3 | t12 | No issues were found when connecting the t03 client to the t12 server. The config response returned with no errors. The find feature successfully queried results and distances were computed correctly aftering adding locations. |
| 3 | t01 | None found, client is able to connect to server.
### Server

These issues occurred when another team's client on the specified port attempted to operate with this teams server. 

| sprint | client | issue or none found |
| :--- | :--- | :--- |
| 3 | t12 | There are no interop problems when connecting the t12 client to the t03 server. The config response returns correctly and supports all features that t12 does. Distances compute as expected. |
| 3 | t01 | None found, just displays that t01 only has config and find features and is missing distances, type, and where.
