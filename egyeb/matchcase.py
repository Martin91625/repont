day=int(input("nap száma: "))

match day:
	case 1:
		print("hétfő")
	case 2:
		print("kedd")
	case 3:
		print("szerda")
	case __:
		print("egyik sem :(")
