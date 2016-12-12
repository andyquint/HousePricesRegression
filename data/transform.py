import csv
import sys

def main(argv):
	if (len(argv) == 0):
		print("Error: no file given")
		return
	for arg in argv:
		filename = str(arg)
		with open(filename) as csvfile:
			encoded_filename = 'encoded_{}'.format(filename)
			datareader = csv.DictReader(csvfile)
			with open(encoded_filename, 'w') as encoded_csv:
				csv_writer = csv.writer(encoded_csv)
				for row in datareader:
					csv_writer.writerow()

if __name__ == "__main__":
	main(sys.argv[1:])
