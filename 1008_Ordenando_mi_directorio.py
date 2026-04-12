# https://jv.umsa.bo/oj/problem.php?id=1008
#  Ordenando mi directorio
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#   Ejemplo Entrada
#    26ContestApplet.jnlp.Image.jpgBook.pdfMovie.avi..8No..Zaphod.JustVeryvery...Improbable
#   Ejemplo Salida
#    Caso 1:ContestApplet.jnlpMovie.aviImage.jpgBook.pdf...Caso 2:NoImprobableZaphodvery...JustVery...
#   Ayuda
#    2da div. 2012 UMSA

for _ in range(int(input())):
    DIR = [input() for _ in range(int(input()))]
    while set(DIR[-2:])!={".",".."}:
        for i in range(len(DIR)-1):
            if DIR[i] in {".",".."}:
                DIR[i], DIR[-1] = DIR[-1], DIR[i]
                break
        if set(DIR[-2:])=={".",".."}:
            break

        for i in range(len(DIR)-1):
            if DIR[i] in {".",".."}:
                DIR[i], DIR[-2] = DIR[-2], DIR[i]
                break
    print(f"Caso {_+1}:")
    print(*DIR, sep="\n")
    print()