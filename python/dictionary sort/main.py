if __name__ == "__main__":
    source = {'a':1,'b':12,'c':2,'d':22,'e':3,'f':32,'g':4,'h':43,'i':5}
    sortedsourceascending = sorted(source.items(), key=lambda item: item[1], reverse=False)
    sortedsourcedescending = sorted(source.items(), key=lambda item: item[1], reverse=True)
    print(sortedsourceascending)
    print(sortedsourcedescending)