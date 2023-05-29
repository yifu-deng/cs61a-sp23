test = {
  'name': 'ascending?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (ascending? '(1 2 3 4 5))  ; #t or #f
          e449af4a212f1577546d3ef60d0624b0
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(1 5 2 4 3))  ; #t or #f
          103c46e912df79ac9b1767b4c1b57350
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(2 2))  ; #t or #f
          e449af4a212f1577546d3ef60d0624b0
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(1 2 2 4 3))  ; #t or #f
          103c46e912df79ac9b1767b4c1b57350
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '())  ; #t or #f
          e449af4a212f1577546d3ef60d0624b0
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
