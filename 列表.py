squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

# 切片
players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team: ")
for player in players:
    print(player.title())

# 复制列表
my_food = ['pizza','falafel','carrot cake']
friend_food = my_food[:]
my_food.append('cannoli')
friend_food.append('ice cream')

print("My favorite food are:")
print(my_food)
print("\nMy friend's favorite food are:")
print(friend_food)
