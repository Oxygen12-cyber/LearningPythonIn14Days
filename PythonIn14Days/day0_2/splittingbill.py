tax = 20 / 100
def main():
	sub_total = input('How much is the bill in $ ?: ')
	num_friends = int(input('how many friends: '))
	filtered_subT = amount_to_float(sub_total)
	compressed = bill_split(filtered_subT, num_friends)
	print(f'each friend will pay ${compressed:.2f} 20% tax included.')


def amount_to_float(d):
	dollars = d.replace("$", "")
	dollar = float(dollars)
	return dollar

def bill_split(amount, friends):
	def tax_calc(taxs, amounts):
		return taxs * amount
		
	split_amount = (amount + tax_calc(tax, amount)) / friends
	return float(split_amount)
	


main()