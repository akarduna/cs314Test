# t02 Interop Report for Port 31402

The issues listed in this report describe possible problems this with team's client or server found by students on other teams.

### Client

These issues occurred when this team's client attempted to operate with the specified server port for another team.

| sprint | server | issue or none found |
| :--- | :--- | :--- |
| 3  | 31419  | This team's client displays 'mi' for the distance between each place, and '0 mi' for the total distance at each place, instead of displaying the correct distance returned by the server. This issue occurs regardless of whether their client is connected to their server or team 19's server. |
| 3 | 31424 | "No Municipality" listed along with each found item. |
| 3 | 31427 | Still seems to be sending Post requests to their server instead of swaping |

### Server

These issues occurred when another team's client on the specified port attempted to operate with this teams server. 

| sprint | client | issue or none found |
| :--- | :--- | :--- |
| 3 | 31419 | This team appears to be rounding their distances down to the unit, instead of rounding to the nearest unit. |
| 3 | 31424 | Postman tests show "type" and "where" return the same results, no results for "ryp" (expected 4), and a long wait for random places |
| 3 | 31427 | Distance response seems to be failing for some weird requests. Zoomed out and clicked on right america and left greenland and it failed concestantly  |
| 3 | 31411 | Postman findRequest testing show that the server returns back a empty places array. |
