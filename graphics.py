def findCoordinations(x1, y1, x2, y2, a):
    xy = []
    xy.append((x1 + x2 * a) / (a + 1))
    xy.append((y1 + y2 * a) / (a + 1))
    return xy

def dict():
    d = {a: a ** 2 for a in range(7)}
    print(d)
    key, value = max(d.iteritems(), key=lambda x: x[1])
    print(key, value)
    print(d.get(max(d, key = d.get)))

if __name__ == "__main__":
    dict()
    #print(findCoordinations(1,1,200,200,1))
    # x1, y1, x2, y2, a = map(float,input().split())
    # print("%.2f %.2f" %(x,y))