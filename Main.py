from Lundo import Lundo
from Medicine import Medicine
from Bed import Bed
from Food import Food
from Hygiene import Hygiene


def main():
    pet = Lundo("Fido")
    pet.addToEquipment(Food("apple",1,1))
    pet.eat()
    pet.play()
    pet.work()
    pet.bath()
    pet.sleep()
    print(pet.status())

    medicine = Medicine("Health Potion", 5, 20)
    health_gain = medicine.use()
    pet.increase_health(health_gain)
    print(f"Used medicine, gained {health_gain} health points.")
    print(pet.status())

    bed = Bed(5, 20)
    energy_gain = bed.use()
    pet.increase_energy(energy_gain)
    print(f"Used bed, gained {energy_gain} energy points.")
    print(pet.status())

    food = Food("Apple", 5, 2)
    hunger_decrease = food.feed()
    pet.decrease_hunger(hunger_decrease)
    pet.decrease_money(food.price)
    print(f"Used food, decreased hunger by {hunger_decrease} points and spent {food.price} money.")
    print(pet.status())

    hygiene = Hygiene()
    hygiene.poop()
    pet.decrease_hygiene(10)
    print(pet.status())

    hygiene.wash()
    pet.increase_hygiene(20)
    print(pet.status())

main()