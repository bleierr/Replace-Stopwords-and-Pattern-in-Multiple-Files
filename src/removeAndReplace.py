import os, re
import glob
import argparse

def getStopwords(fname):
    with open(fname, "r") as f:
        fStrg = f.read()
    stopsLst = []
    for line in fStrg.splitlines():
        stopsLst = stopsLst + [w.lower().strip() for w in line.split()]
    return stopsLst

def replaceFileToTuple(fname):
    with open(fname, "r") as f:
        fStrg = f.read()
    replStrgLst = []
    for line in fStrg.splitlines():
        replStrgLst = replStrgLst + [tuple([strg.strip() for strg in line.split(":")])]
    return replStrgLst


def removeStopwordsFromFiles(fdir, odir, stops):
    fnames = glob.glob(fdir + os.sep + "*.txt")
    for fname in fnames:
        with open(fname, "r") as f:
            fStrg = f.read()
        #Pattern matching possible

        notInStops = []
        for line in fStrg.splitlines():
            lineLst = [w.strip() for w in line.strip().split()]
            
            for char in [".", ",", ":", ";"]:
                lineLst = [w.strip(char) for w in lineLst]

            notInStops.append(" ".join([w for w in lineLst if w.lower() not in stops]))

        tail = os.path.split(fname)[1]

        with open(odir+os.sep+tail, "w") as f:
            f.write("\n".join(notInStops))
    print("Stopwords removed!")
    return fnames

def replaceStrgInFiles(fdir, odir, replStrgLst):
    fnames = glob.glob(fdir + os.sep + "*.txt")
    for fname in fnames:
        with open(fname, "r") as f:
            fStrg = f.read()

        replaced = []
        
        for line in fStrg.splitlines():
            for replTuple in replStrgLst:
                #Pattern matching possible with regex, but it has to be used with care
                replStrg = replTuple[1]
                if replTuple[0][:2] == "\s": 
                    replStrg = " " + replStrg
                if replTuple[0][-2:] == "\s":
                    replStrg = replStrg + " "
                line = replStrg.join(re.split(replTuple[0], line))
                    
                #line = replTuple[1].join(line.split(replTuple[0]))
            replaced.append(line)
        #no solution if a phrase goes over two lines!

        tail = os.path.split(fname)[1]

        with open(odir+os.sep+tail, "w") as f:
            f.write("\n".join(replaced))
    print("Pattern replaced with strings!")
    return fnames

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument('-d', '--dir', default=os.getcwd()+os.sep+"txt/", help='path to the directory containing the txt files')
    parser.add_argument('-o', '--out', default=os.getcwd()+os.sep+"cleanedFiles", help='path to the directory where the output txt files will be stored')
    parser.add_argument('-s', '--stopwords', default=os.getcwd()+os.sep+"stopwords.txt", help='file path to the stopword list, a txt file')
    parser.add_argument('-r', '--replacelist', help='file path to the replace list, a txt file containing a list of strings and replace string in the following format: strg:replstrg, strg:replstrg')

    args = parser.parse_args()

    stopsfile = args.__dict__["stopwords"]

    freplLst = args.__dict__["replacelist"]
    

    fdir = args.__dict__["dir"]

    odir = args.__dict__["out"]

    if (os.path.exists(stopsfile)):
        stops = getStopwords(stopsfile)

        if (os.path.exists(fdir)):
            if(os.path.exists(odir)):
                create = input("Shall the files in the folder {} be overwritten (Y/N)".format(odir))
            else:
                create = input("The following path will been created {} (Y/N)".format(odir))
                if create in ["Y","y"]:
                    os.mkdir(odir)
                
            if create in ["Y","y"]:
                
                if freplLst:
                    if os.path.exists(freplLst):
                        replTupleLst = replaceFileToTuple(freplLst)
                        replaceStrgInFiles(fdir, odir, replTupleLst)
                        fnames = removeStopwordsFromFiles(odir, odir, stops)
                        print("{} files created!".format(len(fnames)))
                    else:
                        print("Error! There seems to be something wrong with the file path of your replace string list:")
                        print(freplLst)
                else:
                    fnames = removeStopwordsFromFiles(fdir, odir, stops)
                    print("{} files created!".format(len(fnames)))            
                
            else:
                print("The script has been aborted!")

        else:
            print("Error: something is wrong with the path to the input files folder!")
            

    
        #for arg, val in args.__dict__.items():
            #print(arg, val)

    else:
        print("Error: something is wrong with the path to the stopword list!")

    print("Script finished!")
    

