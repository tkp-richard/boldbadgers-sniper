import json
import pickle

percentages = {
	"Trident": "0.72",
	"Katana": "0.66",
	"Lightsaber": "0.54",
	"Katana black": "0.01",
	"Mustache": "2.62",
	"Long beard blond": "2.42",
	"Long beard ginger": "2.31",
	"Long beard black": "2.29",
	"Long beard white": "1.51",
	"Santa beard ginger": "1.39",
	"Santa beard": "1.34",
	"Santa beard black": "1.33",
	"Santa beard blond": "1.27",
	"Floral jacket": "4.50",
	"Starry jacket": "4.45",
	"Hoodie Orange": "3.84",
	"T-Shirt Orange": "3.81",
	"Lab coat": "3.71",
	"Shirt white": "3.59",
	"Basketball jersey": "3.54",
	"Basketball jersey black": "3.51",
	"Soccer jersey": "3.48",
	"Hoodie White": "3.43",
	"Kimono": "3.33",
	"T-Shirt White": "3.31",
	"Tank Top Orange": "3.27",
	"Shirt black": "3.20",
	"T-Shirt Purple": "2.07",
	"Toga": "2.07",
	"Tank Top Purple": "2.06",
	"Leather jacket": "2.00",
	"Jacket Red": "1.80",
	"Hoodie Purple": "1.66",
	"Prisoner uniform": "1.78",
	"Jacket Black": "1.62",
	"Starry jacket black": "1.60",
	"Tuxedo": "1.09",
	"Army uniform": "1.03",
	"Pilot vest": "0.96",
	"Astronaut suit": "0.55",
	"Hoodie Black": "0.52",
	"Solana T-shirt": "0.51",
	"Samurai armor": "0.50",
	"Samurai armor black": "0.49",
	"Knight armor": "0.44",
	"Phantom jacket": "0.03",
	"Samo Jersey": "0.02",
	"Degen top": "0.01",
	"T-Shirt Red": "0.01",
	"Hazmat suit": "0.01",
	"Ninja outfit": "0.01",
	"Scientist suit": "0.01",
	"Earplugs": "3.26",
	"Stethoscope": "3.24",
	"Gauge earrings": "3.16",
	"Dangle earrings": "3.11",
	"Wireless earphones": "3.03",
	"Earphones": "2.94",
	"Earrings": "2.78",
	"Beret Green": "4.30",
	"Backwards cap": "4.27",
	"Bandana": "4.24",
	"Mohawk hair fire": "2.41",
	"Antennae": "2.40",
	"Crown of thorns": "2.38",
	"Mohawk hair red": "2.38",
	"Party hat": "2.26",
	"Robin Hood hat": "2.25",
	"Afro hair black": "1.62",
	"Graduate hat": "1.61",
	"Headset red": "1.57",
	"Headset black": "1.50",
	"Cowboy hat": "1.49",
	"Turban": "1.48",
	"Army helmet": "1.47",
	"Captain cap": "1.47",
	"Scooter helmet": "1.45",
	"Headset purple": "1.44",
	"Top hat": "1.44",
	"Afro hair blond": "1.43",
	"Ninja mask": "1.34",
	"Toxic mask": "1.33",
	"Afro hair ginger": "1.31",
	"Snorkeling mask": "1.23",
	"Executioner hood": "1.14",
	"Welding mask": "1.09",
	"Tengai": "1.08",
	"Aviator helmet": "1.03",
	"Horns": "1.03",
	"Helicopter bucket hat": "0.96",
	"Mohawk hair purple": "0.93",
	"Bamboo hat": "0.87",
	"Antlers": "0.84",
	"Beret Purple": "0.84",
	"Wizard hat": "0.84",
	"Toque": "0.82",
	"Leprechaun hat": "0.81",
	"Native Headdress": "0.80",
	"Beret Black Solana": "0.77",
	"Sombrero": "0.77",
	"Elf hat": "0.74",
	"Straw hat": "0.74",
	"Motorcycle helmet": "0.72",
	"King crown": "0.70",
	"Investigator hat": "0.68",
	"Astronaut helmet": "0.65",
	"Brim dome hat": "0.45",
	"Galea": "0.43",
	"Saiyan hair": "0.42",
	"Laurel crown": "0.41",
	"Bunny ears": "0.40",
	"Samurai helmet": "0.27",
	"Pirate hat": "0.24",
	"Samurai helmet black": "0.23",
	"Headset gold": "0.22",
	"Super Saiyan hair": "0.20",
	"Clown hair": "0.15",
	"Backwards cap COPE": "0.01",
	"Snake eyes yellow": "6.52",
	"Snake eyes blue": "6.21",
	"Snake eyes green": "6.09",
	"Snake eyes red": "5.97",
	"Snake eyes purple": "5.97",
	"Red eyes": "3.27",
	"Black eyes": "1.74",
	"White eyes": "1.62",
	"Fire eyes": "0.75",
	"Eyepatch": "4.56",
	"Swimming glasses": "4.52",
	"Monocle": "4.34",
	"Hippie glasses": "4.25",
	"Aviator sunglasses": "3.97",
	"Blindfold": "3.60",
	"Viper gold": "1.82",
	"Viper sunglasses": "1.82",
	"Vizor": "1.74",
	"Magnifying glasses": "1.66",
	"Viper Solana": "1.61",
	"Eye mask purple": "1.60",
	"Viper orange": "1.59",
	"Eye mask white": "1.52",
	"Eye mask": "1.49",
	"Eye mask red": "1.48",
	"VR headset": "1.41",
	"Viper pink": "1.22",
	"3D glasses": "0.94",
	"Laser eyes": "0.46",
	"Eye mask gold": "0.43",
	"Scouter": "0.06",
	"Samo glasses": "0.03",
	"Grey": "22.15",
	"Regular": "21.25",
	"White": "20.69",
	"Ginger": "7.44",
	"Brown": "7.33",
	"Blue": "4.69",
	"Red": "4.38",
	"Pink": "3.83",
	"Silver": "3.29",
	"Black": "2.18",
	"Golden": "0.70",
	"Rainbow": "0.50",
	"Zombie": "0.40",
	"Fire": "0.30",
	"Ice": "0.20",
	"Furless": "0.15",
	"Dissected": "0.09",
	"Skeleton": "0.07",
	"Robot": "0.04",
	"Cyclope": "0.01",
	"Honey Badger": "0.01",
	"Shadow": "0.01",
	"Demon": "0.01",
	"Angel": "0.01",
	"Tape": "5.43",
	"Straw": "5.14",
	"Bubble gum": "4.97",
	"Cigarette": "4.77",
	"Buck teeth": "2.27",
	"Missing teeth": "2.18",
	"Sharp smile": "2.00",
	"Smokebreath": "1.87",
	"Pipe": "1.09",
	"Snake tongue": "0.58",
	"Crayons": "0.53",
	"Cigar": "0.46",
	"Firebreath": "0.38",
	"Golden Pipe": "0.21",
	"Surgical mask": "0.20",
	"Surgical mask black": "0.12",
	"Smile": "13.40",
	"Tongue out": "4.69",
	"Toothless": "4.65",
	"Rose": "4.50",
	"Lipstick": "2.64",
	"Shuriken": "2.60",
	"Saberteeth": "2.56",
	"Foam": "1.42",
	"Goldchain": "3.86",
	"Necklace": "3.84",
	"Nunchuks": "3.53",
	"Scarf Orange": "2.22",
	"Scarf purple": "2.17",
	"Scarf black": "1.89",
	"Scarf white": "1.81",
	"Phantom necklace": "0.02",
	"Rudolph nose": "6.27",
	"Clothespin": "6.26",
	"Nosering": "6.09",
	"Bandade": "6.05",
	"Zebra stripes": "8.35",
	"Leopard spots": "4.64",

	"Purple": "100",
	"Mango": "100",
	"Skyblue": "100",
	"Lightblue": "100",
	"Peach": "100",
	"Solana": "100",
	"Black light": "0.1",
	"Purple dark": "0.1",
	"Blue light": "0.1",
	"Radioactive green": "0.1",
}
for k, v in percentages.items():
	percentages[k] = float(v)

bg_percentages = {
	"Black light": 0.01,
	"Purple dark": 0.01,
	"Blue light": 0.01,
	"Radioactive green": 0.01,
	"Purple": 11.93,
	"Black": 12.35,
	"Red": 12.39,
	"Peach": 12.42,
	"Mango": 12.49,
	"Rainbow": 12.68,
	"Solana": 12.76,
	"Skyblue": 12.94,
	"Lightblue": 12.94,
}

replaced_names = {
	"Afro hair roux": "Afro hair ginger",
	"Santa beard roux": "Santa beard ginger",
	"Basketball jersey - Black": "Basketball jersey black",
	"Solana T-Shirt": "Solana T-shirt",
	"T-shirt Purple": "T-Shirt Purple",
	"T-shirt Orange": "T-Shirt Orange",
	"T-shirt White": "T-Shirt White",
	"T-shirt Red": "T-Shirt Red",
	"Phantom Jacket": "Phantom jacket",
	"Phantom Necklace": "Phantom necklace",
}
for k, v in replaced_names.items():
	percentages[k] = percentages[v]

backgrounds = ['Black light', 'Purple dark', 'Blue light', 'Radioactive green', 'Purple', 'Black', 'Red', 'Peach', 'Mango', 'Rainbow', 'Solana', 'Skyblue']
only_backgrounds = ["Purple", "Mango", "Skyblue", "Peach", "Solana", "Black light", "Purple dark", "Blue light", "Radioactive green"]

_badger_attributes_list = []
with open('badgers.json', 'rb') as f:
	_badger_attributes_list = json.load(f)
badger_attributes = {}
for i, b in enumerate(_badger_attributes_list):
	badger_attributes[i] = [a['name'] for a in b if a['layer'] != 'Background']

_count_rarities = [
	0.26,
	2.06,
	10.62,
	23.96,
	29.52,
	21.65,
	9.32,
	2.31,
	0.30,
]

ranks = {}
with open('ranks.pkl', 'rb') as f:
	ranks = pickle.load(f)