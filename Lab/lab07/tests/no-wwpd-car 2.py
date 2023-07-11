test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.model
          'Model S'
          >>> deneros_car.gas
          30
          >>> deneros_car.gas -= 20 # The car is leaking gas
          >>> deneros_car.gas
          10
          >>> deneros_car.drive()
          'Tesla Model S goes vroom!'
          >>> deneros_car.drive()
          'Cannot drive!'
          >>> deneros_car.fill_gas()
          'Gas level: 20'
          >>> deneros_car.gas
          20
          >>> Car.gas
          30
          >>> Car.gas = 50 # Car manufacturer upgrades their cars to start with more gas
          >>> ashleys_car = Car('Honda', 'HR-V')
          >>> ashleys_car.gas
          50
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> brandons_car = Car('Audi', 'A5')
          >>> brandons_car.wheels = 2
          >>> brandons_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> brandons_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          'Cannot drive!'
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          >>> Car.drive(brandons_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Cannot drive!'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
