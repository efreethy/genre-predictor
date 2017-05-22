### Description
Consumes a dataset of people (strictly formatted) and predicts how strongly they
associate across 4 different genres

Accepts input file formats (csv|tsv) and supports output formats (csv|tsv|json)

Input: Dataset of people

Output: Same dataset, populated with predicted genre information

### USAGE (at the command line)
#### params:
 `input-filename=<name>`  Input file must live in same dir. as main.py
 
 `output-filename=<my-output-filename>`
   
 `output-format=(csv|tsv|json)`
 
 `python main.py input-filename=<name>.(csv|tsv) output-filename=<my-output-filename> output-format=(csv|tsv|json)`
 
 #### Example  
 `python main.py input-filename=test_data.csv output-filename=bestresults output-format=tsv`
