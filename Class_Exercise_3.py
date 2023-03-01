#Exercise 3 Part 1
def Exercise_1():
	temp = 0
	total = 0
	max_temp = 102.5
	while temp < max_temp:
		temp = float(input('Enter a new temperature: '))
		if temp < max_temp:
			total = total + temp

	average = total / 4

	print('sum =' , total)
	print('average =' , average)
	return str


def Exercise_2():
	total_commission = 0
	total_sales = 0
	n = 0
	while n < 4:
		n = n + 1
		sales = float(input('Enter the amount of sales: '))
		comm_rate = float(input('Enter the commission rate: '))
		commission = sales * comm_rate
		print('sales:' , sales)
		print('commission:' , commission)
		total_sales = total_sales + sales
		total_commission = total_commission + commission

	print('total sales is' , total_sales)
	print('total commission is' , total_commission)

	return str


def Exercise_3():
	list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	print('Even Numbers:')
	for number in list:
		if number % 2 == 0:
			print(number)

	print('Odd Numbers:')
	for number in list:
		if number % 2 == 1:
			print(number)

	return str


def Exercise_4():
	for name in ['Pham']:
		print(name)

	for name in ['Tyler']:
		print(name)

	return str


def Exercise_5():
	for world in range(10):
		print('Hello World')

	return str



#Exercise 3 Part 2
def Part2Exercise_1():
	MAX = 5
	total = 0.0

	print('This program calculates the sum of')
	print(f'{MAX} numbers you will enter.')

	for counter in range(MAX):
		number = int(input('Enter a number: '))
		total = total + number

	average = total / MAX

	print(f'The total is {total}.')
	print(f'The average is {average}.')

	return str


def Part2Exercise_2():
	product = float(input('Enter a number: '))

	while product < 100:
		product = product * 10
		print('The product changed to' , product)

	print('The final number is' , product)

	return str


def Part2Exercise_3():
	day = 0
	total = 0
	for collect in range(5):
		day = day + 1
		bugs = int(input('Enter the number of bugs collected today: '))
		total = bugs + total
		print("You have collected a total of" , total , "bugs on day" , str(day) + ".")

	print('The total number of bugs you have collected is' , str(total) + '.')
	return str


def Part2Exercise_4():
	time = 0
	for calculate in range(6):
		time = time + 5
		calories = 4.2 * time

		if time == 10:
			print('the total calories after 10 minutes is' , calories)

		if time == 15:
			print('the total calories after 15 minutes is' , calories)

		if time == 20:
			print('the total calories after 20 minutes is' , calories)

		if time == 25:
			print('the total calories after 25 minutes is' , calories)

		if time == 30:
			print('the total calories after 30 minutes is' , calories)
	return str


def Part2Exercise_5():
	total = 0
	list = []
	n = int(input('Enter the number of laps you ran: '))
	for calculate in range(n):
		lapTime = int(input('Enter the time of your lap in seconds: '))
		list.append(lapTime)
		total = total + lapTime

	average = total / n
	
	print('The fastest lap time is' , max(list))
	print('The slowest lap time is' , min(list))
	print('The average of all the lap times is' , average)

	return str



#Exercise 3.7
def Challenge_4():
	numbers = [1,2,3,4,5,6,7,8,9,10]
	sum = 0
	
	for value in numbers:
		sum += value

	average = sum / len(numbers)

	print('the total is' , sum)
	print('the average is', average)

	f = open("output.txt", "w")
	f.writelines(str(numbers))
	f.close()
	f = open("output.txt", "r")
	print(f.read())
	
	return str


#Total Sales App
def Challenge_4_2():
	sales_list = []
	total = 0

	for sales in range(7):
		sales = float(input('Enter the sales: '))
		sales_list.append(sales)
		total += sales

	print('The total amount of sales for the entire week is' , total)

	f = open("output.txt", "w")
	f.write(str(total))
	f.close()
	f = open("output.txt", "r")
	print(f.read())
	
	return str


#Rainfall App
def Challenge_5():
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	rain_list = []

	total = 0

	for n in months:
		rain = float(input(f'Enter the amount of rain for {n}: '))
		rain_list.append(rain)
		total += rain

	average = total / len(rain_list)
	least = min(rain_list)
	most = max(rain_list)
	least_rain_index = rain_list.index(least)
	most_rain_index = rain_list.index(most)

	print('The total rain in the entire year was' , total)
	print('The average rain was' , average)
	print(f'The month with the lowest amount of rain was: {months[least_rain_index]}')
	print(f'The month with the highest amount of rain was: {months[most_rain_index]}')

	return str
