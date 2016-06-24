# Replace Stopwords and Pattern in Multiple Files
This is a simple Python script to manipulate multiple text files in a folder. 
Stopwords will be removed and patterns can be replaced.

The script was designed to be executed from the commandline and tested only on Win.
Any bug report is very much appreciated.

From the commandline the script can be executed with the default settings:
>python removeAndReplace.py

The default settings expect:
- a file in the same folder named 'stopwords.txt' 
- a folder named 'txt' that contains one or more *.txt files with the text that should be manipulated

The stopword list in stopwords.txt should be structured each stopword in an new line. For instance:
In
a
an

Uppercase and lowercase will be treated in the same way!

Pattern replacement is possible with this script. With the argument -r the path to a pattern-replace file has to be provided:
>python removeAndReplace.py -r replaceStrgs.txt

The pattern-replace file should be a .txt file and structured in the following way each pattern - replace string pair on a separate line:
MA: Master
freee: free
go home: go Home
in dem: hoha
\s\d+\s : NUMBER
^\d : starts with number

The following optional arguments may be provided when executing the script from commandline:
-  -h, --help            show this help message and exit
-  -d DIR, --dir DIR     path to the directory containing the txt files
- -o OUT, --out OUT     path to the directory where the output txt files will be stored
-  -s STOPWORDS, --stopwords STOPWORDS 
                        file path to the stopword list, a txt file
- -r REPLACELIST, --replacelist REPLACELIST
                        file path to the replace list, a txt file containing a
                        list of strings and replace string in the following
                        format: strg:replstrg, strg:replstrg


