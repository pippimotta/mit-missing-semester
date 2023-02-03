import sys
def fizz_buzz(limit):
    for i in range(1, limit+1):
        if i % 15 == 0: 
            print('fizz_buzz')
        elif i % 3 == 0: 
            print('fizz')
        elif i % 5==0: 
            print('buzz')
        else:
            print(i)
def main():
    fizz_buzz(int(sys.argv[1]))

if __name__ == "__main__":
    main()
     
