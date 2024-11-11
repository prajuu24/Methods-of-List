#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#1.append()
#problem statement:Append "Ferrari" to the list
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
cars.append("ferrari")
print(cars)

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#2. Insert
#problem statement: insert "porsche" at index 3
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
cars.insert(2,"porsche")
print(cars)

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#3. clear
#Problem Statement: clea all elements form the list
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
cars.clear()
print(cars)

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#4. sort
#problem statement: sort the original list of cars in alphabetical order
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
cars.sort()
print(cars)

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#5. Remove
#Problem statement: remove "audi" from the list
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
cars.remove("audi")
print(cars)

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#6. index
#problem statement: find the index of "mustang"
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
print(cars.index("mustang"))

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#7. Extend
#problem statement: extend the list with another list of cars
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
cars.extend(["ford","hyundai","kia","nissan","toyota"])
print(cars)

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#8. pop
#problem statement: pop the last element from the list and print it
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
print(cars.pop())

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#9. count
#problem statement: count how many times "bmw" appears in the list
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
print(cars.count("bmw"))

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#10. append multiple
#problem statement: append multiple cars:["jaguar", "fiat"] to the list
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
cars.append("jaguar")
cars.append("fiat")
print(cars)

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#insert multiple
#problem statement: insert multiple cars:["volvo", "honda"] to the list
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
cars.insert(1,["volvo","honda"])
print(cars)

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#12 clear if empty
#problem statement: clear if the list is empty and claer it it is
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
cars.clear()
print(cars)

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#13 sort descending
#problem statement: sort the original list of cars in descending order
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
cars.sort(reverse=True)
print(cars)

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#14 remove all occurences
#problem statement: remove all occurences of "bmw" from the list
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
cars.remove("bmw")
print(cars)

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#15 find last index
#problem statement: find the last index of "tata"
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
print(cars.index("tata"))

#cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
#16 extend with condition
#problem statement: extend the list with ["ferrari", "lambo"] only if "bmw" is in the list
cars=["bmw","mahindra","suzuki","rools royce","bentley","aston martin","tata","audi","mustang"]
cars.extend(["ferrari","lambo"])
print(cars)