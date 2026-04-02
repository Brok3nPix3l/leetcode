from dataclasses import dataclass

class Solution:
    
    @dataclass
    class Robot:
        id: int
        position: int
        health: int
        direction: chr

    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        structured_robots = [self.Robot(id+1, position, health, direction) for id, (position, health, direction) in enumerate(zip(positions, healths, directions))]
        structured_robots.sort(key=lambda robot: robot.position)
        stack = []
        for robot in structured_robots:
            if robot.direction == 'L':
                while len(stack) > 0 and stack[-1].direction == 'R':
                    # print(f'stack[-1]={stack[-1]} robot={robot}')
                    # handle collisions
                    if robot.health == stack[-1].health:
                        stack.pop()
                        robot.health = 0
                        break
                    elif robot.health < stack[-1].health:
                        stack[-1].health -= 1
                        robot.health = 0
                        break
                    else:
                        stack.pop()
                        robot.health -= 1
            if robot.health > 0:
                stack.append(robot)
        stack.sort(key=lambda robot: robot.id)
        return [robot.health for robot in stack]