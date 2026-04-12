#Time limit
import heapq

N, K = map(int, input().split())
F = list(map(lambda x: -int(x), input().split()))  # Convertir todos los elementos a negativos
heapq.heapify(F)  # Convertir F en un heap

for _ in range(K):
  max_value = -heapq.heappop(F)  # Extraer el valor máximo (que será el valor mínimo debido a nuestra negación)
  turn = sum(map(int, str(max_value)))  # Calcular la suma de los dígitos
  heapq.heappush(F, -(max_value - turn))  # Empujar el nuevo valor (max_value - turn) de vuelta al heap

print(turn)