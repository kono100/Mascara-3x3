import cv2

def filtro_suavizacao_mediana(imagem):
    # Aplicar o filtro de suavização por mediana na imagem
    imagem_suavizada = cv2.medianBlur(imagem, 3)

    return imagem_suavizada

# Carregar a imagem
imagem = cv2.imread('C:/Users/User/Downloads/Original.jpg')

# Aplicar o filtro de suavização por mediana
imagem_suavizada = filtro_suavizacao_mediana(imagem)

# Exibir a imagem original e a imagem suavizada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Suavizada', imagem_suavizada)
cv2.waitKey(0)
cv2.destroyAllWindows()