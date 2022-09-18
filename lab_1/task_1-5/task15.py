from typing import List


def hello(name: str = None) -> str:
    result = 'Hello'
    
    if (name):
        result += ', ' + name
    result += '!'
    
    return result


def int_to_roman(num: int) -> str:
    result = ''

    symbols_dict = {
        'M': 1000, 
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    for symbol, value in symbols_dict.items():
        result += symbol * (num // value)
        num %= value

    return result


def longest_common_prefix(strs_input: List[str]) -> str:
    if len(strs_input) == 0:
        return ''

    result = strs_input[0].lstrip()

    for str_input in strs_input[1:]:
        str_input = str_input.lstrip()
        for i in range(min(len(result), len(str_input)), 0, -1):
            if result[:i] == str_input[:i]:
                result = result[:i]
                break
        else:
            result = ''
            break

    return result


def primes() -> int:
    i = 2
    primes = []

    while True:
        for p in primes:
            if i % p == 0:
                break;
        else:
            primes.append(i)
            yield i

        i += 1


class BankCard:
    def __init__(self, total_sum: int, balance_limit: int = -1):
        self.total_sum = total_sum
        self.balance_limit = balance_limit


    def __call__(self, sum_spent: int):
        if self.total_sum < sum_spent:
            raise ValueError(f'Not enough money to spend {str(sum_spent)} dollars.')

        self.total_sum -= sum_spent
        print(f'You spent {str(sum_spent)} dollars.')


    def __repr__(self) -> str:
        return 'To learn the balance call balance.'

    @property
    def balance(self) -> int:
        if self.balance_limit == 0:
            raise ValueError('Balance check limits exceeded.')
        
        if self.balance_limit > 0:
            self.balance_limit -= 1
        
        return self.total_sum


    def put(self, sum_put: int):
        self.total_sum += sum_put
        print(f'You put {str(sum_put)} dollars.')

            
    def __add__(self, other):
        new_limit = self.balance_limit
        if other.balance_limit > new_limit or other.balance_limit == -1:
            new_limit = other.balance_limit

        return BankCard(self.total_sum + other.total_sum, new_limit)
