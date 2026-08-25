

actual = [2, 3, 4, 5, 5]
predicted = [1, 1, 2, 2, 3]

error = 0
for i in range(5):
    error += (abs(actual[i]-predicted[i]))**2
print(error/len(actual))
