from code import entity
from code.enemy import Enemy
from code.entity import Entity


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        pass
    @staticmethod
    def verify_collision(entity_listy: list[Entity]):
        for i in range(len(entity_listy)):
            test_entity = entity_listy[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_listy: list[Entity]):
        for ent in entity_listy:
            if ent.health <= 0:
                entity_listy.remove(ent)
