
def latency_FUNC(latency1):
    mili = latency1 * 1000
    micro = latency1 * 1000000
    nano = latency1 * 1000000000
    latency3 = mili, "miliseconds", micro, "microseconds", nano, "nanoseconds"
    msg = "Pong! your ping is", repr(latency3)
    boi = str(msg).replace('(', '') # remove unwanted charachter
    boi2 = str(boi).replace(')', '') # remove unwanted charachter
    boi3 = str(boi2).replace(',', '') # remove unwanted charachter
    boi4 = str(boi3).replace("'", "") # remove unwanted charachter
    global msg9 #makes var available ouside of  the function
    msg9 = str(boi4).replace('"', "`") # remove unwanted charachter
def c_latency():
    boi = str(msg9).replace("None", "")
    return(boi)


