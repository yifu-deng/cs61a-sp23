test = {
  'name': 'unique',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (count 100 '())
          0
          scm> (count 1 '(1 1 1 1))
          4
          scm> (count 1 '(3 4 5 6 7 8))
          0
          scm> (count 4 '(1 4 3 2 4 5))
          2
          scm> (count 's '(c s 6 1 a))
          1
          scm> (count 'c '(c s 6 1 c))
          2
          scm> (count 'a '(a a b c d e a a g a h a))
          6
          """,
          'hidden': False,
          'locked': False,
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
