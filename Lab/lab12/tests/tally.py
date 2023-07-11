test = {
  'name': 'tally',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (tally '())
          ()
          scm> (tally '(hany))
          ((hany 1))
          scm> (tally '(kevin kevin kevin))
          ((kevin 3))
          scm> (tally '(kevin irene ashley irene irene ashley brandon irene irene brandon))
          ((kevin 1) (irene 5) (ashley 2) (brandon 2))
          scm> (tally '(irene ashley irene irene brandon irene irene ashley brandon))
          ((irene 5) (ashley 2) (brandon 2))
          scm> (tally '(john michelle laryn michelle))
          ((john 1) (michelle 2) (laryn 1))
          scm> (tally '(billy billy bob billy bob billy bob))
          ((billy 4) (bob 3))
          scm> (tally '(adit bryce christina chris daphne grace troy tyler will))
          ((adit 1) (bryce 1) (christina 1) (chris 1) (daphne 1) (grace 1) (troy 1) (tyler 1) (will 1))
          scm> (tally '(abby alan ashwin abby albert anto ashwin))
          ((abby 2) (alan 1) (ashwin 2) (albert 1) (anto 1))
          scm> (tally '(charlotte emily cyrus gabe ethan hima emily))
          ((charlotte 1) (emily 2) (cyrus 1) (gabe 1) (ethan 1) (hima 1))
          scm> (tally '(jordan jessica jose jackie kotryna jose maanav marie marie jordan))
          ((jordan 2) (jessica 1) (jose 2) (jackie 1) (kotryna 1) (maanav 1) (marie 2))
          scm> (tally '(noor mingxiao matthew pragya priya rachel raymond rachel rikio ruslana rohit ruslana))
          ((noor 1) (mingxiao 1) (matthew 1) (pragya 1) (priya 1) (rachel 2) (raymond 1) (rikio 1) (ruslana 2) (rohit 1))
          scm> (tally '(steffi shamith steven thomas tim suhani swetha thomas))
          ((steffi 1) (shamith 1) (steven 1) (thomas 2) (tim 1) (suhani 1) (swetha 1))
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
