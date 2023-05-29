test = {
  'name': 'interleave',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (interleave (list 1 3 5) (list 2 4))
          a99f818d897333f72e15227898b3d59b
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave (list 2 4) (list 1 3 5))
          766d3197a2f2cbd7f113b9383fe5f0d9
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave (list 1 2) (list 1 2))
          5719b30f24809fd4e0474771a2542732
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave '(1 2 3 4 5 6) '(7 8))
          9516ab5cb7caa3c7dd125121eff26c91
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
          scm> (interleave (list 1 3 5) (list 2 4 6))
          c149e0e1fd38badab69ff9cfe54b6531
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave (list 1 3 5) nil)
          50d598bfb4ea31bd04c2948afcb358df
          # locked
          scm> (interleave nil (list 1 3 5))
          50d598bfb4ea31bd04c2948afcb358df
          # locked
          scm> (interleave nil nil)
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
