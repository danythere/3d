import math

# Промежуток с нецелым шагом.
# start - итерируемое значение
# end - конечное значение
# step - шаг


def frange(start, end, step):
    while start < end:
        yield start
        start += step
    yield start


# alVertex, facesString - все вершины и все ребра, отображающиеся на сцене.
allVertex = []
facesString = []

# Функция для добавления круга на сцену.
# x0, y0, z0 - координаты центра; r - радиус; a, b, c - коэф. секущей плоскости.
# alVertex, facesString - все вершины и все ребра, отображающиеся на сцене.


def makeCircle(x0=0, y0=0, z0=0, r=1, a=1, b=1, c=1, allVertex=[], facesString=[]):
    oldAllVertexLen = len(allVertex)
    for t in frange(0, 2*math.pi, .1):
        x = x0+r/(a**2+c**2)*(c*math.cos(t) -
                              (a*b*math.sin(t))/math.sqrt(a**2+b**2+c**2))
        y = y0+(r*math.sqrt(a**2+c**2))/(math.sqrt(a**2+b**2+c**2))*math.sin(t)
        z = z0-r/math.sqrt(a**2+c**2)*(a*math.cos(t) +
                                       (b*c*math.sin(t))/(math.sqrt(a**2+b**2+c**2)))
        allVertex.append(f'{x} {y} {z}')
    faceLength = len(allVertex)-oldAllVertexLen
    faceString = f'{faceLength} '
    for i in range(oldAllVertexLen, len(allVertex)):
        faceString = faceString+f'{i} '
    facesString.append(faceString)
    return allVertex, facesString

# Функция добавления цилиндра на сцену.
# x0, y0, z0, z1, b1, c1 - координаты первого круга и коэф. секущей плоскости.
# x1, y1, z1, a2, b2, c2 - координаты второго круга и коэф секущей плоскости.
# alVertex, facesString - все вершины и все ребра, отображающиеся на сцене.


def makeCylinder(x1=0, y1=0, z1=0, r1=1, a1=1, b1=1, c1=1, x2=0, y2=0, z2=0, r2=1, a2=1, b2=1, c2=1, allVertex=[], facesString=[]):
    lenAllVertex = len(allVertex)
    allVertex, facesString = makeCircle(
        x1, y1, z1, r1, a1, b1, c1, allVertex, facesString)
    allVertex, facesString = makeCircle(
        x2, y2, z2, r2, a2, b2, c2, allVertex, facesString)
    for i in range(lenAllVertex, int(lenAllVertex+(len(allVertex)-lenAllVertex)/2)-1):
        facesString.append(
            '4 ' + f'{i} {i+1} {i+int((len(allVertex)-lenAllVertex)/2)+1} {i+int((len(allVertex)-lenAllVertex)/2)}')
    facesString.append(
        '4 ' + f'{len(allVertex)-1} {lenAllVertex} {lenAllVertex+int((len(allVertex)-lenAllVertex)/2)} {lenAllVertex+int((len(allVertex)-lenAllVertex)/2)-1}')
    return allVertex, facesString

# Функция добавления шара на сцену.
# x0, y0, z0 - координаты центра шара.
# r - радиус шара.
# alVertex, facesString - все вершины и все ребра, отображающиеся на сцене.


def makeBall(x0=0, y0=0, z0=0, r=1, allVertex=[], facesString=[]):
    allVertexLen = len(allVertex)
    tmp = 0
    for beta in frange(0, math.pi, .1):
        tmp = 0
        for alpha in frange(0, 2*math.pi, .1):
            tmp += 1
            x = x0 + r * math.sin(beta) * math.cos(alpha)
            y = y0 + r * math.sin(beta) * math.sin(alpha)
            z = z0 + r * math.cos(beta)
            allVertex.append(f'{x} {y} {z}')
    for i in range(allVertexLen, len(allVertex) - tmp - 1):
        face = (i, (i + tmp), (i + tmp + 1) % len(allVertex), i + 1)
        facesString.append(f'4 {face[0]} {face[1]} {face[2]} {face[3]}')
    return allVertex, facesString

# x0, y0, z0 - координаты центра фигуры.
# l длина каждого ребра.
# alVertex, facesString - все вершины и все ребра, отображающиеся на сцене.


def makeTree(x0=0, y0=0, z0=0, l=200, allVertex=[], facesString=[]):
    allVertex, facesString = makeBall(x0, y0, l, 10, allVertex, facesString)
    allVertex, facesString = makeBall(x0, y0, z0, 10, allVertex, facesString)
    allVertex, facesString = makeBall(l, x0, z0, 10, allVertex, facesString)
    allVertex, facesString = makeBall(x0, l, z0, 10, allVertex, facesString)
    allVertex, facesString = makeBall(-l, x0, y0, 10, allVertex, facesString)
    allVertex, facesString = makeBall(x0, y0, -l, 10, allVertex, facesString)
    allVertex, facesString = makeCylinder(
        x0, y0, z0, 10, -1, 1, -1, x0, y0, l, 10, -1, 1, -1, allVertex, facesString)
    allVertex, facesString = makeCylinder(
        x0, y0, z0, 10, -1, 1, -1, x0, l, z0, 10, -1, 1, -1, allVertex, facesString)
    allVertex, facesString = makeCylinder(
        x0, l, z0, 10, -1, 1, -1, l, y0, z0, 10, -1, 1, -1, allVertex, facesString)
    allVertex, facesString = makeCylinder(
        x0, l, z0, 10, -1, 1, -1, x0, y0, l, 10, -1, 1, -1, allVertex, facesString)
    allVertex, facesString = makeCylinder(
        x0, y0, z0, 10, -1, 1, -1, l, y0, z0, 10, -1, 1, -1, allVertex, facesString)
    allVertex, facesString = makeCylinder(
        x0, y0, z0, 10, -1, 1, -1, x0, y0, -l, 10, -1, 1, -1, allVertex, facesString)
    allVertex, facesString = makeCylinder(
        x0, l, z0, 10, 1, 1, 1, -l, y0, z0, 10, 1, 1, 1, allVertex, facesString)
    allVertex, facesString = makeCylinder(
        x0, l, z0, 10, 1, 1, 1, x0, y0, -l, 10, 1, 1, 1, allVertex, facesString)
    allVertex, facesString = makeCylinder(
        x0, y0, z0, 10, -1, 1, -1, -l, x0, y0, 10, -1, 1, -1, allVertex, facesString)
    return allVertex, facesString

# x0, y0, z0 - координаты центра фигуры.
# rCircle, rCyl - радиусы нанизанных на цилиндр шариков и радиус самого цилиндра.
# alVertex, facesString - все вершины и все ребра, отображающиеся на сцене.
# k - количество нанизываемых шариков.


def makeBarbecue(x0=0, y0=0, z0=0, k=1, rCircle=100, rCyl=50, allVertex=[], facesString=[]):
    lCyl = (k+1)*rCircle*2
    allVertex, facesString = makeCylinder(
        x0, y0, z0, rCyl, 1, 0, -1, x0, y0, lCyl, rCyl, 1, 0, -1, allVertex, facesString)
    for i in range(k):
        allVertex, facesString = makeBall(
            x0, y0, i*rCircle*2+rCircle*2, rCircle, allVertex, facesString)
    return allVertex, facesString


allVertex, facesString = makeBarbecue(0, 0, 0, 10)

resString = f'ply \n format ascii 1.0 \n element vertex {len(allVertex)} \nproperty float x \n property float y \n property float z \n' + \
    f'element face {len(facesString)} \n property list uchar int vertex_index \n end_header \n'
print(allVertex)
for i in range(0, len(allVertex)):
    resString = resString+allVertex[i]+'\n'
for i in range(0, len(facesString)):
    resString = resString+facesString[i]+'\n'
myFile = open("3dobj.ply", "w+")
myFile.write(resString)
myFile.close()
