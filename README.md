# vault_recall
Python scripts for recalling files from Vault (object store) or Archive (tape), and checking progress / estimating recall completion time (or the inverse, archival)

### Installation

`pip install -r requirements.txt`

### Running

Both the `recall.py` script, and the `check_recall_progress.py` script, initially rely on a list of filepaths to check, as a plain text file.  
You can generate such a file with a command similar to `find . -type f > filelist.txt`.  

Running `check_recall_progress.py -f filelist.txt` will record a CSV of filepaths, timestamps and stat results.  
The location of this CSV can be specified with the `--progress_file` or `-p` parameter.  
If not specified, progress_file will default to `~/recall_progress.csv`.  
Instead of passing both a filelist and progress_file on subsequent runs, you can just pass the progress_file to recheck previously checked files.  

`check_recall_progress.py -h` will output:

```
usage: check_recall_progress.py [-h] [-f FILELIST] [-p PROGRESS_FILE] [-s] [-v]

Check detailed vault/archive status

optional arguments:
  -h, --help            show this help message and exit
  -f FILELIST, --filelist FILELIST
                        a text file containing files to check
  -p PROGRESS_FILE, --progress_file PROGRESS_FILE
                        progress CSV file to read/write to
  -s, --stats_only      just print previously recorded info, don't check files
  -v, --verbose         print status for each file to console
```

`check_recall_progress.py` will output summary stats to console, which looks like this:


```
Run ended time: 2023-03-23T11:47:20
525279/630441 (83.32%) files on fast tier
Size on fast tier: 3.65 TB/6.88 TB (53.03%)
Note some tools (like du) will report twice the current file size (7.29 TB), due to replication between OGG and Tamaki
93538/630441 (14.84%) files accessed in the week prior (since 2023-03-16T11:47:20)
303.67 GB/6.88 TB (4.42%) accessed in the week prior (since 2023-03-16T11:47:20)
Latest atime: 2023-03-22 22:05:22
```