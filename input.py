# Программа позволяет вводить вершины, строит соответствующие им грани и выводить 3d фигуры в ply-файл.
# Можно соединить несколько объектов.
# Ввод интерактивный.
print('Введите количество объектов')
objectNumber = int(input())
vertexArray = []
faceArray = []
for i in range(0, objectNumber):
    print(f'Введите количество вершин у {i+1} объекта')
    vertexNumber = int(input())
    for j in range(0, vertexNumber):
        print(f'Введите {j+1} вершину в формате "x y z"')
        vertex = input()
        vertexArray.append(vertex)
    print(f'Введите количество граней у {i+1} объекта')
    faceNumber = int(input())
    for q in range(0, faceNumber):
        print(f'Введите грани, состоящие из вершин в формате "a1 a2...an, начиная с 0. Для каждой фигуры отсчет вершин начинается с k+1 номера, где k-номер последней вершины предыдущей фигуры."')
        face = input()
        faceArray.append(face)
resString = f'ply \n format ascii 1.0 \n element vertex {len(vertexArray)} \nproperty float x \n property float y \n property float z \n' + \
    f'element face {len(faceArray)} \n property list uchar int vertex_index \n end_header \n'
for i in range(0, len(vertexArray)):
    resString = resString+vertexArray[i]+'\n'
for j in range(0, len(faceArray)):
    currentFace = faceArray[j].split()
    resString = resString+str(len(currentFace)) + ' ' + faceArray[j] + '\n'
my_file = open("3dnew.ply", "w+")
my_file.write(resString)
my_file.close()