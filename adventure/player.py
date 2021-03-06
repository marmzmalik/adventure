class Player:

    def __init__(self, x, y):
        '''
        Creates a new Player.
        :param x: x-coordinate of position on map
        :param y: y-coordinate of position on map
        :return:

        Example:
        x: 2
        y: 3

        This is a suggested starter class for Player.
        You may add new parameters / attributes / methods to this class as you see fit.
        Consider every method in this Player class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --
        '''
        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self.points = 0



    def move(self, dx, dy):
        '''
        Given integers dx and dy, move player to new location (self.x + dx, self.y + dy)
        :param dx: x coordinate
        :param dy: y corrdinate
        :return:

        example:
        dx : 4
        dy : 3
        '''
        self.x += dx
        self.y += dy

        pass

    def move_north(self):
        '''These integer directions are based on how the map must be stored
        in our nested list World.map

        :param: Player moves north
        :return: player coordinates

        example:
        player moves North, x = 0 , y = 1
        coordinates ( 0,1 )
        '''

        """Go to the 4th floor of the library, if possible."""

        self.move(0,1)


    def move_south(self):
        '''
        :param: Player moves south
        :return: player coordinates

        example:
        player moves south, x = 0 , y = 1
        coordinates ( 0,1 )
        '''
        self.move(0,1)

    def move_east(self):
        '''
        :param: Player moves east
        :return: player coordinates

        example:
        player moves east x = 1, y = 0
        coordinates (1, 0)
        '''
        self.move(1,0)

    def move_west(self):
        '''
        :param: Player moves west
        :return: player coordinates

        example:
        player moves west x = -1, y = 0
        coordinates (-1, 0)

        '''
        self.move(-1,0)

    def add_item(self, item):
        '''
        Add item to inventory.
        :param:item
        :return: True if item is added into inventory

        example:
        Inventory:  cookie
                    pencil
                    eraser
        add: gum

        Inventory: cookie
                   pencil
                   eraser
                   gum
        '''

        if item not in self.inventory:
            self.inventory.append(item)
        return True

    def remove_item(self, item):
        '''
        Remove item from inventory.
        :param item:
        :return: True if item is removed from inventory

        Example:
        Inventory: gum
                    pencil
                    eraser
        remove: gum

        Inventory: pencil
                   eraser

        '''
        if item in self.inventory:
            self.inventory.remove(item)

        return True




    def get_inventory(self):
        '''
        Return inventory.
        :return: every item that is located in invetory

        Example:
        Inventory: cookie
                    gum
                    pencil
                    eraser
        '''

        return self.inventory


    def points_location(self):
        '''

        :param self:
        :return: every time player gets closer to IB they will get points according to their locations

        Example:
        Player at 3rd floor library
        points: -1
        Player at Starbucks
        points: 1
        '''
        return self.points
