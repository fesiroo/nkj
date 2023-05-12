class Tree:
    def __init__ (self, name, speed):
        self.name = name
        self.speed = speed
        self.height = 15
        self.leaf = 2
    def grow(self):
        self.height += self.speed
        self.leaf += self.speed * 3
        print(f"У дерева {self.name} высота: {self.height}, листьев: {self.leaf}")
apple_tree1 = Tree("Бомгю", 5)
apple_tree2 = Tree("Юнхо", 3)
apple_tree3 = Tree("Чонвон", 10)
for i in range(1000):
    apple_tree1.grow()
    apple_tree2.grow()
    apple_tree3.grow()