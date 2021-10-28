# t20 Interop Report for Port 31420

The issues listed in this report describe possible problems this with team's client or server found by students on other teams.

### Client

These issues occurred when this team's client attempted to operate with the specified server port for another team.

| sprint | server | issue or none found |
| :--- | :--- | :--- |
| 3 | t27 | none found |
| 3 | t19 | DistanceRequest Client-Side - Not displaying the total distance correctly client-side despite T19's server having distances implemented. After inspection their code, it seems their "total distance" is a hardcoded value, so no issue required to fix, I assume displaying the actual total distance is in progress. |
| 3 | t24 | None Found |
| 3 | t11 | Random places seem to return the same random places every time |

### Server

These issues occurred when another team's client on the specified port attempted to operate with this teams server. 

| sprint | client | issue or none found |
| :--- | :--- | :--- |
| 3 | t27 | none found |
| 3 | t19 | DistanceRequest Server-Side - Distances off by 1 compared to T19's distance request results (rounding error?), could be t19 distances request or t20's |
| 3 | t24 | None found |
| 3 | t11 | None found |
