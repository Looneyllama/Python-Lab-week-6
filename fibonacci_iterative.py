def fibonacci_iterative(n):
  fibonacci = [0,1]
  if(n <= 1):
    return fibonacci[n]
  else:
    for i in range(1,n):
      fibonacci.append(fibonacci[i] + fibonacci[i-1])
    return fibonacci[n]

fibonacci_iterative(10)
