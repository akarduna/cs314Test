# t08 Interop Report for Port 31408

The issues listed in this report describe possible problems this with team's client or server found by students on other teams.

### Client

These issues occurred when this team's client attempted to operate with the specified server port for another team.


| sprint | server | issue or none found |
| :--- | :--- | :--- |
| 3 | 31425 | client will not connect to :31425 server, or any server with distances implemented |
| 3 | 31417 | The client would not recognize that :31417 existed. It would not list our implemented features.|
| 3 | 31414 | Client would not save 31414, listed features for the client were not listed in the footer for 31408 or attempted 31414 |
| 3 | 31415  | supported features not listed when server selected                                    |
| 3 | 31415  | Attempt to search resulted in Uncaught TypeError: cannot read properties of undefined |

### Server

These issues occurred when another team's client on the specified port attempted to operate with this teams server.

| sprint | client | issue or none found |
| :--- | :--- | :--- |
| 3 | 31425 | distances request responds with code 404, not expected 400  |
| 3 | 31417 | Like stated above, a distance postman request to the server responds with error 404 (Not Found).  |
| 3 | 31414 | Distances request reponds with error 404 |
| 3 | 31415  | POST https://localhost:31408/api/distances net::ERR_FAILED 404 instead of BAD_REQUEST 400, used residual search locations from previous server to execute distance request |