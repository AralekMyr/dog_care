from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'fill the db with dummy data'

    def handle(self, *args, **options):
        # add_breeds()
        add_centers()
        add_cares()

        self.stdout.write(self.style.SUCCESS('db filled. Have fun !'))



def add_breeds():
    from api.models.breed import Breed
    # Partially taken from https://www.woopets.fr/chien/races/
    breeds = [
        "Affenpinscher",
        "Airedale Terrier",
        "Akita Américain",
        "Akita Inu",
        "American Staffordshire Terrier",
        "Ariégeois",
        "Barbet",
        "Barbu Tchèque",
        "Barzoï",
        "Basenji",
        "Basset",
        "Beagle",
        "Bearderd Collie",
        "Beauceron",
        "Bedlington Terrier",
        "Berger Allemand",
        "Berger Australien",
        "Berger Belge",
        "Berger Blanc Suisse",
        "Berger de Bergame",
        "Berger de Bohême",
        "Berger de Brie",
        "Berger de l'Atlas",
        "Berger de Picardie",
        "Berger de Russie",
        "Berger des Pyrénées",
        "Berger des Shetland",
        "Berger du Caucase",
        "Berger Hollandais",
        "Bichon",
        "Billy",
        "Bobtail",
        "Boerbull",
        "Border Collie",
        "Border Terrier",
        "Boston Terrier",
        "Bouledogue Américain",
        "Bouledogue Français",
        "Bouvier Australien",
        "Bouvier Bernois",
        "Bouvier des Ardennes",
        "Boxer",
        "Brachet",
        "Braque Allemand",
        "Braque",
        "Broholmer",
        "Buhund Norvégien",
        "Bull Terrier",
        "Bulldog",
        "Bullmastiff",
        "Cairn Terrier",
        "Cane Corso",
        "Caniche",
        "Carlin",
        "Cavalier King Charles",
        "Chesapeake Bay Retriever",
        "Chien Chinois à Crête",
        "Chien Courant",
        "Chien d'arrêt",
        "Chien d'eau",
        "Chien d'ours de Carélie",
        "Chien d'Oysel",
        "Chien de Canaan",
        "Chien de montagne des Pyrénées",
        "Chien de montagne portugais",
        "Chien de Saint Hubert",
        "Chien du Groenland",
        "Chien du Pharaon",
        "Chien d'Artois",
        "Chien d'élan",
        "Chien Dinnois de Laponie",
        "Chien Jindo Coréen",
        "Chien Loup",
        "Chien Norvégien de Macareux",
        "Chien Nu",
        "Chien Rouge",
        "Chien Thaïlandais",
        "Chihuahua",
        "Chow Chow",
        "Cirneco de l'Etna",
        "Clumber-Spaniel",
        "Cocker Américain",
        "Cocker Anglais",
        "Colley",
        "Coton de Tuélar",
        "Curly Coated Retriever",
        "Cursinu",
        "Dalmatien",
        "Dandie-Dinmont-Terrier",
        "Dobermann",
        "Dogo Canario",
        "Dogue Allemand",
        "Dogue Argentin",
        "Dogue de Bordeaux",
        "Dogue de Majorque",
        "Dogue du Tibet",
        "Drever",
        "Espagneul Breton",  # Bretagne rpz X)
        "Eurasier",
        "Field-Spaniel",
        "Fila Brasileiro",
        "Fila de Sao Miguel",
        "Flat-Coated Retriever",
        "Fox Terrier",
        "Foxhoud Américain",
        "Foxhound Anglais",
        "Golden Retriever",
        "Goldendoodle",
        "Grand Anglo-Français",
        "Grand Basset Griffon vendéen",
        "Grand Bouvier Suisse",
        "Grand Epagneul de Münster",
        "Greyhound",
        "Griffon Belge",
        "Griffon Bleu de Gascogne",
        "Griffon Bruxellois",
        "Griffon Fauve de Bretagne",
        "Griffon Korthals",
        "Griffon Nivernais",
        "Harrier",
        "Hokkaïdo Ken",
        "Hovawart",
        "Husky Sibérien",
        "Irish Glen of Imaal Terrier",
        "Irish Terrier",
        "Jack Russel Terrier",
        "Jagdterrier",
        "Kai",
        "Kelpie",
        "Kerry Blue Terrier",
        "King Charles Spaniel",
        "Komondor",  #alias Serpillère sur pattes...
        "Kromfohrländer",
        "Kuvasz Hongrois",
        "Labradoodle",
        "Labrader Retriever",
        "Laïke de Sibérie occidentale",
        "Laïke de Sibérie orientale",
        "Laïka Russo-Européen",
        "Lakeland Terrier",
        "Landseer",
        "Leonberger",
        "Lévrier Afghan",
        "Lévrier Azawakh",
        "Lévrier Ecossais",
        "Lévrier Espagnol",
        "Lévrier Irlandais",
        "Lévrier Polonais",
        "Lhassa Apso",
        "Malamute de l'Alaska",
        "Mastiff",
        "Mâtin de l'Alentejo",
        "Mâtin de Naples",
        "Mâtin des Pyénées",
        "Mâtin Espagnol",
        "Mudi",
        "Norfolk Terrier",
        "Norwich Terrier",
        "Otterhound",
        "Parson Russel Terrier",
        "Pékinois",
        "Petit Basset Griffon vendéen",
        "Petit Brabançon",
        "Petit Chien Lion",
        "Petit Epagneul de Münster",
        "Petit Lévrier Italien",
        "Pinscher",
        "Pitbull",
        "Podenco Canario",
        "Podenco Ibicencio",
        "Pointer Anglais",
        "Poitevin",
        "Pomsky",
        "Porcelaine",
        "Pudelpointer",  #la serpillère, le retour !
        "Puli",
        "Pumi",
        "Ratonero Bodeguero Andaluz",
        "Retriever de la Nouvelle-Ecosse",
        "Rhodesian-Rigeback",
        "Rottweiler",
        "Saint-Bernard",
        "Saluki",
        "Samoyède",
        "Schapendoes",
        "Schipperke",
        "Schnauzer",
        "Sealyham Terrier",
        "Setter Anglais",
        "Setter Gordon",
        "Setter Irlandais Rouge",
        "Shar-Pei",
        "Shiba Inu",  #BONK ! go to horny jail !
        "Shih Tzu",  #... J'me... J'me SHIH TZU XD !
        # (Oh ça va, il est presque une heure du mat',
        # et ce commentaire sera pas lu de toute façon...)
        "Shikoku",
        "Silky Terrier",
        "Skye Terrier",
        "Sloughi",
        "Smous des Pays-Bas",
        "Spinone",
        "Spitz Allemand",
        "Spitz de Norrbotten",
        "Spitz des Wisigoths",
        "Spitz Finlandais",
        "Spitz Japonais",
        "Springer Anglais",
        "Staffordshire Bull Terrier",
        "Sussex-Spaniel",
        "Tchouvatch Slovaque",
        "Teckel",
        "Terre-Nauve",
        "Terrier Australien",
        "Terrier Brésilien",
        "Terrier de Manchester",
        "Terrier Ecossais",
        "Terrier Japonais",
        "Terrier Noir Russe",
        "Terrier Tchèque",
        "Terrier Tibétain",
        "Tosa",
        "Volpino Italien",
        "Welsh Corgi Cardigan",
        "Welsh Corgi Pembroke",
        "Welsh Springer Spaniel",
        "Welsh Terrier",
        "West Highland White Terrier",
        "Whippet",
        "Yorkshire Terrier"
    ]

    for breed_name in breeds:
        Breed.objects.get_or_create(name=breed_name)


def add_cares():
    from api.models.care import Care

    Care.objects.get_or_create(name="Bain", duration="00:45:00", price=45)
    Care.objects.get_or_create(name="Toilettage", duration="01:15:00", price=75)
    Care.objects.get_or_create(name="Coupe Poils", duration="01:00:00", price=60)
    Care.objects.get_or_create(name="Coupe Griffes", duration="00:15:00", price=15)
    Care.objects.get_or_create(name="Massage", duration="01:00:00", price=60)
    Care.objects.get_or_create(name="Promenade", duration="02:30:00", price=150)
    Care.objects.get_or_create(name="Entretien Dentaire", duration="00:45:00", price=45)
    Care.objects.get_or_create(name="Coiffe", duration="01:30:00", price=90)


def add_centers():
    from api.models.center import Center

    Center.objects.get_or_create(name="Scoobyd'Aix")
    Center.objects.get_or_create(name="Tout'if")
    Center.objects.get_or_create(name="Toutou Net")


def add_employee():
    from api.models.center import Center
    from api.models.employee import Employee

    # Employee de Scoobyd'Aix

