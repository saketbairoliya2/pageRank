# pageRank
A Python Package for finding the page rank for multiple pages based on the tags.

## Installation

```
git clone https://github.com/saketbairoliya2/pageRank.git
cd pageRank
```

## Usage
```
python page_ranking.py
```
Accepts Input through command line, can be exited by pressing -1.

## Sample Input

P Ford Car Review  
P Review Car  
P Review Ford  
P Toyota Car  
P Honda Car  
P Car  
Q Ford  
Q Car  
Q Review  
Q Ford Review  
Q Ford Car  
Q cooking French  

## Sample Output 

Q1: P1 P3  
Q2: P6 P1 P2 P4 P5  
Q3: P2 P3 P1  
Q4: P3 P1 P2  
Q5: P1 P3 P6 P2 P4  
Q6:  


