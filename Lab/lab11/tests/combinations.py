test = {
  'name': 'What Would Scheme Display?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (- 10 4)
          71dc1c0558e41b2d6d30fd9795b4fb1f
          # locked
          scm> (* 7 6)
          afa373c99abc5a519735aa7466635f88
          # locked
          scm> (+ 1 2 3 4)
          994cc386b9ac20ceafc06b188d1ee65b
          # locked
          scm> (/ 8 2 2)
          805a87056a1a3fd559e4ef12a815b2be
          # locked
          scm> (quotient 29 5)
          9934e055a74f1f7f5fb94c0f9fd6402d
          # locked
          scm> (modulo 29 5)
          3cfd97a152be55d1a3486dbacb2bf637
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (= 1 3)                    ; Scheme uses '=' instead of '==' for comparison
          6687e91ee1a92d6553457317c0165f4a
          # locked
          scm> (< 1 3)
          811dacf2a8c491d71193b389f2e6d3ab
          # locked
          scm> (or 1 #t)                  ; or special form short circuits
          94ce22b5936436a75abf185df37ba826
          # locked
          scm> (and #t #f (/ 1 0))
          6687e91ee1a92d6553457317c0165f4a
          # locked
          scm> (not #t)
          6687e91ee1a92d6553457317c0165f4a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define x 3)
          5ce45267887fa5dae1771a9b64b54929
          # locked
          scm> x
          350815b30c2ebeb01da1870d87346e85
          # locked
          scm> (define y (+ x 4))
          847f7c178da2025ec82e39b01a424bfd
          # locked
          scm> y
          3f8f8f09d1f65fa9740c33b3c16d4731
          # locked
          scm> (define x (lambda (y) (* y 2)))
          5ce45267887fa5dae1771a9b64b54929
          # locked
          scm> (x y)
          2ac3553c8fa906a0ec29e6b3fe8cf4ea
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (if (not (print 1)) (print 2) (print 3))
          94ce22b5936436a75abf185df37ba826
          350815b30c2ebeb01da1870d87346e85
          # locked
          scm> (* (if (> 3 2) 1 2) (+ 4 5))
          b1cf566efb20d5b4e8e0fcba34deeb5f
          # locked
          scm> (define foo (lambda (x y z) (if x y z)))
          603330d515a0d452dda52d8a7f3d1dad
          # locked
          scm> (foo 1 2 (print 'hi))
          2371fa29af94abdb618fc78229de00d9
          805a87056a1a3fd559e4ef12a815b2be
          # locked
          scm> ((lambda (a) (print 'a)) 100)
          a1068219c1264e3c30f090f447a18f5c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
