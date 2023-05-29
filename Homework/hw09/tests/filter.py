test = {
  'name': 'my-filter',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (my-filter even? '(1 2 3 4))
          d676660c7ec6fda72fb2e4188a758bc5
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter odd? '(1 3 5))
          50d598bfb4ea31bd04c2948afcb358df
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter odd? '(2 4 6 1))
          41b46952e8febc14ae103a14b6edee11
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter even? '(3))
          010af2cd1e765be62ece0c49314e61bd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter odd? nil)
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
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (my-filter even? '(1 2 3 4)) ; checks you dont use builtin filter
          d676660c7ec6fda72fb2e4188a758bc5
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (define filter nil)
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
