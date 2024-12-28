import asyncio
from enum import Enum, auto
from random import choice


class Action(Enum):
    HIGHKICK = auto()
    LOWKICK = auto()
    HIGHBLOCK = auto()
    LOWBLOCK = auto()


class Agent:
    def __aiter__(self):
        self.health = 5
        self.actions = list(Action)
        return self

    async def __anext__(self):
        return choice(self.actions)


async def fight():
    agent = Agent()
    async for agent_action in agent:
        if agent_action in (Action.HIGHKICK, Action.LOWKICK):
            neo_action = choice([Action.HIGHBLOCK, Action.LOWBLOCK])
        else:
            neo_action = choice([Action.HIGHKICK, Action.LOWKICK])

        if agent_action == Action.HIGHBLOCK and neo_action == Action.LOWKICK:
            agent.health -= 1
        elif agent_action == Action.LOWBLOCK and neo_action == Action.HIGHKICK:
            agent.health -= 1

        print(f"Agent: {agent_action}, Neo: {neo_action}, Agent Health: {agent.health}")

        if agent.health <= 0:
            print("Neo wins!")
            break


if __name__ == "__main__":
    asyncio.run(fight())
