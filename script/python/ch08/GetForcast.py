from numpy import *

def forcast(fileInputName, fileOutputName, fArr, k, isArray):      #general function to parse tab -delimited floats
    numFeat = len(open(fileInputName).readline().split('\t')) - 1 #get number of fields
    dataMat = []; labelMat = []
    fr = open(fileInputName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))

    # forcast by input and write to file
    out = open(fileOutputName, "w")
    if isArray == 0:
        yHat = lwlr(fArr, dataMat, labelMat, k);
        yHatNew = array(yHat).reshape(-1,).tolist()
        for item in yHatNew:
            out.write("%s\n" % item)
    else:
        yHat = lwlrArr(fArr, dataMat, labelMat, k);
        for item in yHat:
            out.write("%s\n" % item)
    out.close()
    return 1;

def lwlrArr(testArr,xArr,yArr,k=1.0):  #loops over all the data points and applies lwlr to each one
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat

def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))
    for j in range(m):                      #next 2 lines create weights matrix
        diffMat = testPoint - xMat[j,:]     #
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws

def main():
    import argparse
    parser = argparse.ArgumentParser(description='forcast algorithm collections',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--infile', default='', help="infile")
    parser.add_argument('-o', '--outfile', default='', help="outfile")
    parser.add_argument('-k', '--keffi', type=float, default=0.01, help="k")
    parser.add_argument('-f', '--farray', help="farray")

    args = parser.parse_args()
    if not args.infile or not args.outfile:
        parser.print_help()
        exit(-1)
    # get all input parameters
    infile = args.infile
    outfile = args.outfile
    k = args.keffi
    forcastArr = args.farray

    # convert forcastArr to 2 dimensions array
    fArr = []
    for one in forcastArr.split(','):
        tmp = []
        tmp.append(1.000000)
        tmp.append(float(one))
        fArr.append(tmp)

    # determine is array or one point.
    # 0: one point
    # 1: array points
    isArrayFlag = 0
    if forcastArr.find(",") == -1:
        isArrayFlag = 0
    else:
        isArrayFlag = 1

    # forcast the input
    forcast(infile, outfile, fArr, k, isArrayFlag)

if __name__ == "__main__":
    main()
