"""Mini game RPG: áp dụng kiến thức OOP của Week 14.

Chạy từ thư mục gốc repository:
    python weeks/week-14-oop-essentials/game_oop_example.py

EX01 - Class & Object:
    Character là class; hero và monster là các object.

EX02 - Composition:
    Monster nhận một strategy bên ngoài để quyết định hành động.
    Có thể đổi monster.strategy mà không sửa class Monster.

EX03 - Inheritance:
    Hero kế thừa Character và bổ sung kỹ năng đặc biệt.
"""

from collections.abc import Callable
from typing import Literal

Action = Literal["attack", "defend"]
Strategy = Callable[["Character", "Character"], Action]


class Character:
    """Lớp cơ sở chứa dữ liệu và hành vi chung của nhân vật."""

    def __init__(self, name: str, hp: int, attack_power: int) -> None:
        if hp <= 0:
            raise ValueError("HP phải lớn hơn 0.")
        if attack_power <= 0:
            raise ValueError("Sức tấn công phải lớn hơn 0.")

        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)

    def attack(self, target: "Character") -> None:
        target.take_damage(self.attack_power)
        print(
            f"{self.name} tấn công {target.name}, "
            f"gây {self.attack_power} sát thương."
        )


class Hero(Character):
    """Anh hùng kế thừa Character và có thêm kỹ năng đặc biệt."""

    def special_attack(self, target: Character) -> None:
        damage = self.attack_power * 2
        target.take_damage(damage)
        print(
            f"{self.name} dùng kỹ năng đặc biệt lên {target.name}, "
            f"gây {damage} sát thương!"
        )


def aggressive_strategy(monster: Character, hero: Character) -> Action:
    """Chiến thuật hung hăng: luôn tấn công."""
    return "attack"


def defensive_strategy(monster: Character, hero: Character) -> Action:
    """Chiến thuật phòng thủ: phòng thủ khi máu thấp."""
    if monster.hp <= 15:
        return "defend"
    return "attack"


class Monster(Character):
    """Quái vật có chiến thuật được truyền vào (composition)."""

    def __init__(
        self, name: str, hp: int, attack_power: int, strategy: Strategy
    ) -> None:
        super().__init__(name, hp, attack_power)
        self.strategy = strategy

    def take_turn(self, hero: Character) -> None:
        action = self.strategy(self, hero)
        if action == "attack":
            self.attack(hero)
        elif action == "defend":
            print(f"{self.name} thủ thế và hồi 5 HP.")
            self.hp += 5
        else:
            raise ValueError(f"Chiến thuật trả về hành động không hợp lệ: {action}")


def play_battle() -> None:
    hero = Hero("Knight", hp=50, attack_power=10)
    monster = Monster(
        "Goblin",
        hp=35,
        attack_power=7,
        strategy=aggressive_strategy,
    )

    print("=== MINI RPG: KNIGHT vs GOBLIN ===")
    turn = 1

    while hero.is_alive() and monster.is_alive():
        print(f"\n--- Lượt {turn} ---")
        hero.attack(monster)

        if not monster.is_alive():
            break

        monster.take_turn(hero)
        print(f"HP {hero.name}: {hero.hp} | HP {monster.name}: {monster.hp}")
        turn += 1

        # Đổi chiến thuật trong lúc chơi: đây là composition.
        # Quái vật sẽ phòng thủ khi HP thấp.
        if monster.hp <= 15:
            monster.strategy = defensive_strategy

    print("\n=== KẾT THÚC ===")
    if hero.is_alive():
        print(f"{hero.name} chiến thắng!")
    else:
        print(f"{monster.name} chiến thắng!")


if __name__ == "__main__":
    play_battle()
