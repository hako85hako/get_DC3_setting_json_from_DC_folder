# floatに変換可能かどうかを判定
def isfloat(s): 
    try:
        float(s) 
    except ValueError:
        return False
    else:
        return True

# intに変換可能かどうかを判定
def isint(s): 
    try:
        int(s) 
    except ValueError:
        return False
    else:
        return True


if __name__=="__main__":
    print(isint('--'))
    print(isint('1'))