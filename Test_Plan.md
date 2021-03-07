

## Description ##
Console application process_metrics.py does following tasks.

• periodically gathers process metrics (for a specified amount of time)
• creates a report of the gathered process metrics (in CSV format)
• outputs the average for each process metric
• detects possible memory leaks and raises a warning

More specifically, the app takes as input:
• the process name (mandatory)
• the overall duration of the monitoring in seconds (mandatory)
• the sampling interval in seconds (optional, by default 5 sec if not specified)

The metrics consists of:
• % of CPU used
• private memory used
• number of open handles / file descriptors


## Pre requisites: ##
- Python3 should be installed on to the system. 
- Install required modules from requirements.txt


## Assumptions: ##
- Tested on MacOS.
- Memory leak warning triggered if memory percent >  10 % 


# TEST PLAN 


Test environment:
OS : macOS Big Sur
Browser: Chrome

## Test Setup

1. Get software (console) application process_metrics.py
2. For Automartion framework use pytest



## Usability Tests

### Usability Test 1

1. Check whether you can specify required arguments PROCESS_NAME (-p)  and DURATION (-d)

python3 process_metrics.py -p devicecompute -d 10

EXPECT:

1. Command should run successfully.

### Usability Test 2

1. Check whether you can specify required arguments PROCESS_NAME and DURATION, and -s (sampling) is optional.

EXPECT:

1. Sampling option is optional.

### Usability Test 3

1. Check whether script gives error for wrong PROCESS_NAME

python3 process_metrics.py -p XXXX -d 10   (assuming there is no process running with XXXX name)

EXPECT:

1.  Should display "Pls enter running process name.:" message.

### Usability Test 3

1. Check whether script gives error for wrong PROCESS_NAME

python3 process_metrics.py -p XXXX -d 10   (assuming there is no process running with XXXX name)

EXPECT:

1.  Should display "Pls enter running process name.:" message.


### Usability Test 4

1. Check whether script gives error for negative DURATION

python3 process_metrics.py -p test -d -10   

EXPECT:

1.  Should display "error: argument -d/--duration: -10 is an invalid positive int value" message.


## Functionality Tests

### Test 1

1. Check whether csv file is generated.

python3 process_metrics.py -p devicecompute -d 10

EXPECT:

1. CSV is file generated with values.

###  Test 2

1. Check wheather test is monitoring for duration of seconds.

EXPECT:

1. Test should monitor for a given overall duration.

###  Test 3

1. Check whether the test sampling overwrites the default value 5 secs.

python3 process_metrics.py -p XXXX -d 10   -s 10

EXPECT:

1.  Should overwrite default sampling value.

###  Test 4

1. Check whether script without default value takes 5 secs.


EXPECT:

1.  Sampling default is 5 secs


###  Test 5

1. Check for a given running process csv file has more than one line.

EXPECT:

1.  CSV file should have more than one line.
