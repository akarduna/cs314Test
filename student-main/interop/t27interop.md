# t27 Interop Report for Port 31427

The issues listed in this report describe possible problems this with team's client or server found by students on other teams.

### Client

These issues occurred when this team's client attempted to operate with the specified server port for another team.

| sprint | server | issue or none found |
| :--- | :--- | :--- |
| 3 | 31424 | none found |
| 3 | 31418 | none found |
| 3 | 31406 | Connection refused, request to server failed |

### Server

These issues occurred when another team's client on the specified port attempted to operate with this teams server. 

| sprint | client | issue or none found |
| :--- | :--- | :--- |
| 3 | 31424 | find with type or where returns 500 server error, should work or return 400  |
| 3 | 31424 | find with "por" and "ter" don't get right number back, make sure database query searches the right columns |
| 3 | 31418 | none found | 
| 3 | 31406 | Connection refused, request to server failed. Likely interop error in t06 |
