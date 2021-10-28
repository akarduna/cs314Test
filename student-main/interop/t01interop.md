# t01 Interop Report for Port 31401 #####

The issues listed in this report describe possible problems this with team's client or server found by students on other teams.

### Client

These issues occurred when this team's client attempted to operate with the specified server port for another team.

| sprint | server | issue or none found |
| :--- | :--- | :--- |
| 3 | t04 | none found |
| 3 | 31413 | None found, client correctly sent config and find request. |
| 3 | 31402 | Same issue with 'Invalid Server URL!' when trying to connect with our server. |
| 3 | t20 | Client returns 'Invalid Server URL!' when I tried to connect to our teams server. Could not test any further. Looks like schema validation failed, its looking for "distance" when it is "distances"|
| 3 | t23   | Same issue with 'Invalid Server URL!' when trying to connect to my team's server. Further testing unavailable |

### Server

These issues occurred when another team's client on the specified port attempted to operate with this teams server. 

| sprint | client | issue or none found |
| :--- | :--- | :--- |
| 3 | t04 | Failed distance request returns 404 error instead of 400 |
| 3 | t13 | Find Request - it does not appear that the limit set by our client is being respect (expected:5, got:10). We are also only getting a found value of 10 for every query. Our servers also populated different results for the same query, looks like you guys are searching by alphabetical order? <br> Distances Request - didn't get back 'distances' in features array so our distance request never sends. |
| 3 | t02 | Same issue with 'find' or distances back as features. |
| 3 | t20 | Server incompatibilities: Find, Distances. Search bar did not populate. |
| 3 | t23 | Able to connect but can't run 'Find' or 'Distances'. My team's search is set up to disable features that are unavailble. |
