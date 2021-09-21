import numpy as np

def lerMalha(nome):
    """Recebe uma string com o nome do arquivo .obj a ser lido. Retorna um
    np.ndarray com as x,y,z coordenadas dos pontos (uma coluna é um ponto) da
    malha e uma lista de strings, onde cada elemento da lista define uma face."""
    vertices = []
    faces = []
    arquivo = open(nome, "r")
    for line in arquivo:
        if line[0] == "v":
            partes = line.split(" ")
            vertices.append([float(partes[1]), float(partes[2]),\
                             float(partes[3])])
        if line[0] == "f":
            faces.append(line)
    arquivo.close()
    pontos = np.transpose(np.array(vertices))
    return pontos, faces

    
def escreverMalha(pts, faces, nome):
    """Recebe uma nd.array com x,y,z coordenadas de todos os pontos da malha,
    uma lista com os strings representando as faces da malha e
    um nome do arquivo no qual a malha deve ser escrita (em formato .obj)."""
    novo = np.transpose(pontos)
    arquivo = open(nome, "w")
    for ponto in novo:
        arquivo.write("v ")
        for eixo in ponto:
            arquivo.write(str(eixo) + " ")
        arquivo.write("\n")
        
    for face in faces:
        arquivo.write(face)       
    arquivo.close()
    
#=================================================================
# Escreva todas as possíveis funções auxiliares dentro desse bloco



def transformacaoAfim(pts):
    print(pts[0])
    """Recebe um np.ndarray com x,y,z coordenadas de pontos. A função adiciona
    a 4a coordenada para representar os pontos em coordenadas homogêneas
    e aplica uma transformação afim. O valor de retorno é um np.ndarray
    com x,y,z coordenadas dos pontos transformados."""
    # crie a matriz composta de todas as transformações em coordenadas homogêneas
    # multiplique os pontos em coordenadas homogêneas por essa matriz
    # descarte a 4a coordenada e retorna apenas as coordenadas x,y,z dos pontos
    
    #PRECISA RODAR EM VOLTA DO EIXO X
    
    return zRotation(pts)

def scaling(sx, sy, sz):
    scal = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]])
    
    #para simetria só é preciso negativar os valores de sx e/ou sy e/ou sz
    
    return scal

def translation(tx, ty, tz):
    trans = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]])
    
    return trans

def zRotation(z):
    zRot = np.array([
        [np.cos(z), -np.sin(z), 0],
        [np.sin(z),  np.cos(z), 0],
        [        0,          0, 1]])
    
    return zRot

def yRotation(y):
    yRot = np.array([
        [ np.cos(y), 0, np.sin(y)],
        [         0, 1,         0],
        [-np.sin(y), 0, np.cos(y)]])
    
    return yRot

def xRotation(x):
    xRot = np.array([
        [1,         0,          0],
        [0, np.cos(x), -np.sin(x)],
        [0, np.sin(x),  np.cos(x)]])
    
    return xRot

def scale(value):
    return np.eye(value)

#=================================================================

pontos, faces = lerMalha("bob.obj")
pontos = transformacaoAfim(pontos)
escreverMalha(pontos, faces, "bob_novo.obj")

