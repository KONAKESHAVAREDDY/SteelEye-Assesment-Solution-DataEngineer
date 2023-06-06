# SteelEye-Assesment-Solution-DataEngineer
Descrption - I created this REST API for SteelEye's technical test to retrieve all trades, trades by id, and some complex search filters from the trade database. Additionally, I included the pagination and sorting features.

Installation
!pip install fastapi
!pip install uvicorn
!pip install fastapi-pagination

cd into the file(app.py) that conatins code using terminal or command prompt
Run the command uvicorn app:app --reload
Then u copy the http url and paste it in the browser u will get the application


I will demonstrate the output below

1.Fetching  All the  Trades
I added the endpoint URL /trades/ to get all the trades stored in the database. I returned the array where I have stored the details of the trade.


2.Fetching A Single Trade by Trade Id
I have added the endpoint URL /tradings/{trading_id} to get a trade which is equal to the Trade ID stored in the  Database.  I have run a for-loop to get the trade which has the same trade id that was given in the query parameter and gives particular trade in the form of dictionary.


3.Fetching All Trades that are matching with the search parameter
I have added the endpoint URL /trade to get all those trades where the search query parameteris equal to the counterparty, instrumentId, instrumentName and trader stored in the Trade database. From this, I used for-loop to get all those trades where atleast one of the values in the trade detail matches with the search paramter given in the query parameter and return all those trades in the form of list of dictionary.


4.Fetching All Trades by Advanced Filtering
I have added the endpoint URL /tradings to get all those trades where it matches with the exact value sent in the query paramter from the Trade database. I have looped through all the trades in the tradeing dictonary. Everytime loop run, I have wriiten a condition when it come under the constraints which is given in the query parameter then only it is going to add that trade into the result and return all those trades in the form of list of dictionary.


5.Pagination Functionality
For this, I have used inbuilt library given in the fastapi. They have created a function call /add_pagiantion/ which will allow the pagination functionality. After that, whenever I have to return the list of dictionary. I have added /paginate/ function to it.

6.Sorting Functionality
I have created a enum class. So that user can easily select the order in which they want to sort the data. I have used /sorted/ library given in the python to sort the list of dictionary according to the parameter given from the user.

<img width="555" alt="Screenshot 2023-06-06 223034" src="https://github.com/KONAKESHAVAREDDY/SteelEye-Assesment-Solution-DataEngineer/assets/104962709/a470c6e5-045e-49ee-a995-08e51393d5b7">
<img width="514" alt="Screenshot 2023-06-06 223234" src="https://github.com/KONAKESHAVAREDDY/SteelEye-Assesment-Solution-DataEngineer/assets/104962709/beac1019-9f57-418b-b86b-abf427a07324">
<img width="534" alt="Screenshot 2023-06-06 223257" src="https://github.com/KONAKESHAVAREDDY/SteelEye-Assesment-Solution-DataEngineer/assets/104962709/ecf1351c-704a-4d6b-ad47-286b996ee194">
<img width="503" alt="Screenshot 2023-06-06 223316" src="https://github.com/KONAKESHAVAREDDY/SteelEye-Assesment-Solution-DataEngineer/assets/104962709/00ccc0a3-8085-4106-a884-91c4d3b67cfd">










