from typing import List, Callable

import numpy
import math

from generic.read_inputs import read_txt_list_from_nr


class Monkey:
  items: List[int] = [],
  operation: Callable = None,
  operand: int = 0,
  test_divisor: int = 0,
  throw_true: int = -1,
  throw_false: int = -1,
  items_inspected:int = 0

  def test(self, x):
    if x % self.test_divisor == 0:
      return self.throw_true
    else:
      return self.throw_false

  def __str__(self):
    return f"""
    Monkey
    items: {self.items}
    operation: {self.operation.__name__}
    operand: {self.operand}
    test_divisor: {self.test_divisor}
    throw_true: {self.throw_true}
    throw_false: {self.throw_false}
    items_inspected: {self.items_inspected}
    """


def add_nrs(x,y):
  return x + y


def multiply(x,y):
  return x*y


def square(x,y):
  return x * x


def construct_monkeys(input:List[str]) -> List[Monkey]:
  rows_per_monkey = 7
  num_monkeys = int((len(input)+1)/rows_per_monkey)
  monkeys = []

  for monkey_index in range(num_monkeys):
    # Monkey 0:
    if not input[monkey_index*rows_per_monkey].startswith('Monkey '):
      raise ValueError(f"Input failed. First line of monkey is {input[monkey_index*rows_per_monkey]}")
    monkey = Monkey()

    #   Starting items: 59, 65, 86, 56, 74, 57, 56
    starting_items_str = input[monkey_index*rows_per_monkey + 1].removeprefix("  Starting items: ").removesuffix('\n')
    monkey.items = [int(x) for x in starting_items_str.split(', ')]
    
    #Operation: new = old * 17
    operation_str = input[monkey_index*rows_per_monkey + 2].removeprefix("  Operation: ").removesuffix('\n')
    if operation_str == 'new = old * old':
      monkey.operation = square
    else:
      operations_list = operation_str.split(' ')
      
      monkey.operand = int(operations_list[4])

      if operations_list[3] == '*':
        monkey.operation = multiply
      elif operations_list[3] == '+':
        monkey.operation = add_nrs
      else:
        raise NotImplementedError(f'Operator {operations_list[3]} not supported.')

    #  Test: divisible by 3
    monkey.test_divisor = int(input[monkey_index*rows_per_monkey + 3].removeprefix('  Test: divisible by ').removesuffix('\n'))

    #    If true: throw to monkey 3
    monkey.throw_true = int(input[monkey_index*rows_per_monkey + 4].removeprefix('    If true: throw to monkey ').removesuffix('\n'))

    #    If false: throw to monkey 6
    monkey.throw_false = int(input[monkey_index*rows_per_monkey + 5].removeprefix('    If false: throw to monkey ').removesuffix('\n'))

    monkeys.append(monkey)
  return monkeys


def play_round(monkeys: List[Monkey], super_worried: bool) -> List[Monkey]:
  
  if super_worried:
    divisor = get_divisor(monkeys)
  
  for index, monkey in enumerate(monkeys):
    for item in monkey.items:

      item = monkey.operation(item, monkey.operand)

      if not super_worried:
        item = int(item/3)
      else:
        item = item % divisor
        
      throw_to = monkey.test(item)

      monkeys[throw_to].items.append(item)

      monkey.items_inspected += 1
    monkey.items = []

  return monkeys


def get_divisor(monkeys: List[Monkey]) -> int:
  divisors = [monkey.test_divisor for monkey in monkeys]
  
  common_divisor = int(numpy.prod(divisors))
  return common_divisor


def play_monkey_business(
  monkeys: List[Monkey],
  rounds:int=20,
  super_worried:bool = False
) -> int:
  for round in range(rounds):
    monkeys = play_round(monkeys,super_worried=super_worried)

  ordered_monkey_business = sorted(
    [monkey.items_inspected for monkey in monkeys],
    reverse=True)
  return ordered_monkey_business[0] * ordered_monkey_business[1]


def part1(use_example:bool=False) -> int:
  input = read_txt_list_from_nr(11, use_example=use_example)
  monkeys = construct_monkeys(input)
  
  lvl_monkey_business = play_monkey_business(
    monkeys,
    rounds=20,
    super_worried=False)

  return lvl_monkey_business


def part2(use_example:bool=False) -> int:
  input = read_txt_list_from_nr(11, use_example=use_example)
  
  monkeys = construct_monkeys(input)

  lvl_monkey_business = play_monkey_business(
    monkeys,
    rounds=10000,#4,#20,#10000,
    super_worried=True)

  return lvl_monkey_business
