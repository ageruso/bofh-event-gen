## For bofh_event)gen.py ##

Execution example: python3 bofh_event_gen.py -u http://10.10.10.10:8088/services/collector -t \<token\>

This will send a json event to any splunk HEC collector you define that will contain a "randomly" generated excuse from the BOFH excuse board.


## For bofh_scraper.py ##

Execution Example: python3  bofh_scraper.py
This will generate a random excuse created using the bofh excuse board, then print out to your terminal.


*All credit for the excusese goes to BOFH*
Link to BOFH excuse board: http://bofh.bjash.com/ExcuseBoard.html
