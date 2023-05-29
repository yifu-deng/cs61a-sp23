from classes import *

standard_cards = [
	TACard('Tim, Twin Terror of Twos', 1200, 2100),
	TutorCard('José, Brazilian Dude', 2300, 1000),
	TACard('Anto, Spinner', 2300, 1000),
	TutorCard('Albert, NewJeans Enjoyer', 1100, 2200),
	TACard('Kevin H, random bum who, for some reason, is incredibly powerful', 1500, 1800),
	TACard('Cyrus, Educator of Ed', 2100, 1200),
	TutorCard('Tyler, Lam(bda)', 1600, 1600),
	TACard('λaryn, λord of λambdas', 1600, 1500),
	TutorCard('Abby, Queen of Geese', 1000, 2000),
	TutorCard('Christina, Lemonade Slurper', 1900, 1400),
	TutorCard('Ashley, Caffeinated Sleeper', 1300, 1700),
	AICard('Ethan, Crazy Capybara', 1100, 2000),
	AICard('Dimple, Diligent Dilly-Dallyer', 1500, 1500),
	AICard('Mihir, Turbo Turtle', 1800, 1600),
	TACard('Michelle, Mysterious Mountain', 1700, 1500),
	AICard('jade, jestering juggernaut ', 2299, 1001),
	TutorCard('Thomas, the Tank', 1500, 1600),
	AICard('Aditya, the Illuminous Thunder', 1600, 1800),
	AICard('“Kitty, Dumpling Master”', 1700, 1700),
	AICard('Aarnav, Drowsy Potato ', 2300, 1100),
	AICard('Malavikha, Oscillating Oddity ', 1000, 2200),
	AICard('Matt, Merchant of Malice', 2100, 1100),
	AICard('Balaji, Grand Supreme Lord of Ballers', 1800, 1600),
	TutorCard('Christina, Master of Fans', 1800, 1200),
	AICard('Alexander, The Great One', 1400, 2000),
	AICard('Elder Beggs', 1200, 2000),
	AICard('♩eremy, Joker', 2000, 1100),
	AICard('Milad, King of Creami', 1700, 1200),
	AICard('Rishi, Harbinger of the Fishies', 1700, 1500),
	AICard('Laryn\'s Dad ', 1500, 1800),
	AICard('Rain Crow, Cousin of Storm Crow', 2000, 1000),
	AICard('Pranit, Sapient Sage', 1900, 1500),
	AICard('Diana, Dorm Dweller', 1000, 1500),
	TACard('Bryce, Fuzzy Fire Flinger', 1400, 2000),
	TutorCard('Chris, Poli of Wags', 1500, 1000),
	TACard('Aditya, Existential Hermit', 1000, 2300),
	TACard('Daphne, Asian of Chaos', 2300, 1000),
	InstructorCard('DeNero, Antihero', 5000, 5000),
	InstructorCard('Justin, Chaotic Wanderer', 0, 10000)
]

standard_deck = Deck(standard_cards)
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()
