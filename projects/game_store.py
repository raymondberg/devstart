class Game:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class VideoGameStore():
    def __init__(self, starting_items):
        self.shelves = starting_items

    def buy_item(self, item):
        self.shelves.append(item)

    def list_items(self):
        for item in self.shelves:
            print 'Game: {} ${:.2f}'.format(item.name, item.cost)

    def sell_item(self, item_name):
        item = self.find_item(item_name)
        if item is None:
            print "UH OH, CAN'T SELL THAT!"
        else:
            return self.shelves.remove(item)

    def find_item(self, item_name):
        for item in self.shelves:
            if item.name == item_name:
                return item

mario = Game('Super Mario Bros', 14.00)
halo = Game('Halo 3', 20.00)

store = VideoGameStore([mario, halo])
store.list_items()
    # Game: Super Mario Bros $14.00
    # Game: Halo 3 $20.00

store.buy_item(Game('Halo 4', 40.00))
store.sell_item('Super Mario Bros')
store.sell_item('Super Mario Bros')      #UH OH!

store.list_items()
    # Game: Halo 3 $20.00
    # Game: Halo 4 $40.00


## Ideas to improve the store:
# Keep track of how much money you're making in the store!
# You can't buy new games if you don't have money on hand. Check first so you don't go negative!
# How are you going to make money without marking up the games?
# Games shuld know how to print themselves prettily, check out __str__
# Really hard: Make it interactive, ask questions if they want to buy or sell and for game info.
