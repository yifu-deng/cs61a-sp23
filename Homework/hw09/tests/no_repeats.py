test = {
  'name': 'no-repeats',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (no-repeats '(5 4 3 2 1))
          7772672b0d7983fcad285ba36fdb9e60
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats '(5 4 3 2 1 1))
          7772672b0d7983fcad285ba36fdb9e60
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats '(5 5 4 3 2 1))
          7772672b0d7983fcad285ba36fdb9e60
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats '(12))
          8b2130ac87026f9d03c15c5b6e94ff0c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats '(1 1 1 1 1 1))
          41b46952e8febc14ae103a14b6edee11
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
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (no-repeats (list 5 4 2))
          f548fc04dff3c01f20060ee2a960e786
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats (list 5 4 5 4 2 2))
          f548fc04dff3c01f20060ee2a960e786
          # locked
          scm> (no-repeats (list 5 5 5 5 5))
          ad7b77cde813c2a412843ac391a89a34
          # locked
          scm> (no-repeats ())
          010af2cd1e765be62ece0c49314e61bd
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
