test = {
  'name': 'using-pair',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '18bdc0680dc0f3e9daea29f10a6af2c3',
          'choices': [
            "Pair('+', Pair('-', Pair(2, Pair(4, Pair(6, Pair(8, nil))))))",
            "Pair('+', Pair(Pair('-', Pair(2, Pair(4))), Pair(6, Pair(8))))",
            'Pair(+, Pair(Pair(-, Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))',
            "Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))",
            'None of these'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Write out the Python expression that returns a `Pair` representing the given expression: (+ (- 2 4) 6 8)'
        },
        {
          'answer': '6a6e74663803090608705c573b14fbd2',
          'choices': [
            '-',
            '+',
            '(',
            '2',
            '6',
            'None of these'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is the operator of the call expression?'
        },
        {
          'answer': '1133f1e98acfe4306164f5062de34638',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If the `Pair` you constructed in the previous part was bound to the name `p`,
          how would you retrieve the operator?
          """
        },
        {
          'answer': 'f60be8080c5a9136725d6fd53786a9fc',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If the `Pair` you constructed was bound to the name `p`, 
          how would you retrieve a list containing all of the operands?
          """
        },
        {
          'answer': 'd313609c200dc1782bcb806aacd318cb',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'How would you retrieve only the first operand?'
        },
        {
          'answer': '211848be182bcd927de5d5eeca919503',
          'choices': [
            "'-'",
            "'+'",
            '2',
            '4',
            '-2',
            "Pair('-', Pair(2, Pair(4, nil)))",
            'Pair(2, Pair(4, nil))'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is the first operand of the call expression (prior to evaluation)?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
