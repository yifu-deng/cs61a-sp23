test = {
  'name': 'efficiency-quiz',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Linear',
          'choices': [
            'Constant',
            'Logarithmic',
            'Linear',
            'Quadratic',
            'Exponential',
            'None of these'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': r"""
          What is the worst case (i.e. when n is prime) order of growth of is_prime in terms of n?
          
          def is_prime(n):
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
          """
        },
        {
          'answer': 'Quadratic',
          'choices': [
            'Constant',
            'Logarithmic',
            'Linear',
            'Quadratic',
            'Exponential',
            'None of these'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': r"""
          What is the order of growth of bar in terms of n?
          
          def bar(n):
              i, sum = 1, 0
              while i <= n:
                  sum += biz(n)
                  i += 1
              return sum
          
          def biz(n):
              i, sum = 1, 0
              while i <= n:
                  sum += i**3
                  i += 1
              return sum
          """
        },
        {
          'answer': 'Logarithmic',
          'choices': [
            'Constant',
            'Logarithmic',
            'Linear',
            'Quadratic',
            'Exponential',
            'None of these'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': r"""
          What is the order of growth of foo in terms of n, where n is the length
          of lst? Assume that slicing a list and calling len on a list can both be
          done in constant time.
          
          def foo(lst, i):
              mid = len(lst) // 2
              if mid == 0:
                  return lst
              elif i > 0:
                  return foo(lst[mid:], -1)
              else:
                  return foo(lst[:mid], 1)
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
