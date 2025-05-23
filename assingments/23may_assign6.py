# ask the user to enter a sentence. Count how many times “a”, “e”, and “i” appear using .count() and sum them using str() + int().


y=input("enter a sentence")

t=[y.count("a"),y.count("e"), y.count("i")]

print(sum(t))
