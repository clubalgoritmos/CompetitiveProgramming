for _ in range(int(input())):
  def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

  def primo_mas_cercano(n):
      c = 0
      while True:   
          if es_primo(n+c) or es_primo(n-c):
            break
          c+=1
      return c

  print(primo_mas_cercano(int(input())))