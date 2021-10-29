# cs314Test
The goal of this porject is to help autimate testing for cs314. Currently their are three scripts, pytest and rmoteTest are used to create a dictionary of server responses for the tests that the class wrote.
currently they both just save the dictionary to the output.csv file, whith the first column being the key of the dictionary(team number) and the second column being the value(A list of distance lists).
The third script is loadData, which just converts the csv back to the dictioanry. 

I am going to continue working on this as the semester continues, if you have any suggestions or would like to help contribute please let me know either at akarduna@colostate.edu or in the slack at Alex karduna. 

## Running the scripts
Currently there is no package management so you will have to pip install of the libraries that are used that you do not have on your machine. 
Also if you want to remoteTest script to work you have to port forward all of the sprint machines. The basic workflow is run the tests once(either remoteTest of pytest) then it will save the resoults to output.csv and you can look at the results there without having to send more requests to the servers. 

## Future Ideas
* Make the tests run for all tests in the student repo.
* Add more single server testing
* Come up with a better way of showing the user their server response(dictionary is very clunky)
* Give the user more control through the comand line. (should be able to pass arguemnts to the program and have it run difrent scenerios rather then having to go in and edit the code.
* Add testing for dev environement so user doesnt have to make a realse to run tests. 

## Notes
Please do not run any of the test scripts durring the demo as they do put some load on the server and database. 
