from Lundo import Lundo
from Medicine import Medicine
from Bed import Bed
from Food import Food
from Hygiene import Hygiene


def main():
    pet = Lundo("Fido")
    print(pet.status())
    pet.addFoodToEquipment(Food("apple",1))
    pet.addMedToEquipment(Medicine("ibuprofen",1))
    pet.eat()
    pet.useMedicine()
    print(pet.status())
main()