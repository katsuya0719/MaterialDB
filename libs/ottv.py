def wallCalc(area,direction,U=1,alpha=0.7):
    et={"N":2.72,"NNE":3.30,"NE":3.86,"ENE":4.44,"E":5.01,"ESE":4.65,"SE":4.3,"SSE":3.95,"S":3.6,"SSW":3.92,"SW":4.23,"WSW":4.29,"W":4.35,"WNW":3.94,"NW":3.54,"NNW":3.13,"Roof":13.37}
    total=area*U*alpha*et[direction]

    return total

def windowCalc(area,direction,sc,esm=1):
    sf={"N":104,"NNE":121,"NE":138,"ENE":153,"E":168,"ESE":183,"SE":197,"SSE":194,"S":191,"SSW":197,"SW":202,"WSW":189,"W":175,"WNW":157,"NW":138,"NNW":121,"Roof":264}
    total=area*sc*esm*sf[direction]

    return total

def ottv(wallList,windowList):
    wallarea=[]
    wallsum=[]
    windowarea=[]
    windowsum=[]
    for wall in wallList:
        wallarea.append(wall[0])
        wallsum.append(wallCalc(wall[0],wall[1],wall[2],wall[3]))#will accept only one argument wall

    if len(wallsum)>1:
        wallsum=wallsum.sum()
        wallarea=wallarea.sum()

    elif len(wallsum)==1:
        wallsum=wallsum[0]
        wallarea=wallarea[0]

    for window in windowList:
        windowarea.append(window[0])
        windowsum.append(windowCalc(window[0],window[1],window[2]))

    if len(windowsum)>1:
        windowsum=windowsum.sum()
        windowarea=windowarea.sum()

    elif len(windowsum)==1:
        windowsum=windowsum[0]
        windowarea=windowarea[0]

    ottv=(wallsum+windowsum)/(wallarea+windowarea)
    area=wallarea+windowarea

    return [ottv,area]

def calcTotal(envList):
    results=[]
    areas=[]
    for ele in envelope:
        temp=ottv(ele[0],ele[1])
        results.append(temp[0])
        areas.append(temp[1])

    print(results)
    denom=0
    numer=0
    for result,area in zip(results,areas):
        denom+=area
        numer+=result*area

    return numer/denom

if __name__ == '__main__':
    #[[[area,direction,Uvalue,alpha]][[area,direction,SCvalue]]]
    N=[[[4957,"N",1,0.7]],[[2457,"N",0.6]]]
    E=[[[4028.6,"E",1,0.7]],[[4911.7,"E",0.6]]]
    S=[[[4311.2,"S",1,0.7]],[[2973.1,"S",0.6]]]
    W=[[[5221,"W",1,0.7]],[[4087.07,"W",0.6]]]
    roof=[[[5473,"Roof",0.5,0.9]],[[0,"Roof",1]]]

    envelope=[N,E,S,W,roof]

    result=calcTotal(envelope)

    print (result)