#!/usr/bin/env python3

def get_list(input_file):

    output_data = []
    try:
        with open (input_file,"r") as input_data:
            for row in input_data:
                try:
                    output_data.append(int(row))
                except:
                    print(f"Can not parse non int row. Data: {row}")
    except:
        print(f"We have some issue when opening {input_file}. Please double check your file name and path")

    return output_data

def main():
    fizz_count = 0
    buzz_count = 0
    fizz_buzz_count = 0

    data_list = get_list("numfile.txt")

    for data in data_list:
        if data % 15 == 0:
            print("FizzBuzz")
            fizz_buzz_count = fizz_buzz_count + 1
        elif data % 5 ==0:
            print("Buzz")
            buzz_count = buzz_count + 1
        elif data % 3 == 0:
            print("Fizz")
            fizz_count = fizz_count + 1
        else:
            print(data)

    print(f"We have {fizz_count} 'Fizz', {buzz_count} 'Buzz' and {fizz_buzz_count} 'FizzBuzz'")

if __name__ == "__main__":
    main()
