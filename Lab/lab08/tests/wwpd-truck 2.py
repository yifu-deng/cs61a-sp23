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
          >>> deneros_truck = MonsterTruck('Monster', 'Batmobile')
          >>> deneros_car.size # Type Error if an error occurs and Nothing if nothing is displayed
          'Tiny'
          >>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          'Tesla Model S goes vroom!'
          >>> deneros_truck.size # Type Error if an error occurs and Nothing if nothing is displayed
          'Monster'
          >>> deneros_truck.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> MonsterTruck.drive(deneros_truck) # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.drive(deneros_truck) # Type Error if an error occurs and Nothing if nothing is displayed
          'Monster Batmobile goes vroom!'
          >>> deneros_truck.gas # Type Error if an error occurs and Nothing if nothing is displayed
          0
          >>> MonsterTruck.rev(deneros_truck) # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          >>> MonsterTruck.rev(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          >>> Car.rev(deneros_truck) # Type Error if an error occurs and Nothing if nothing is displayed
          Error
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
