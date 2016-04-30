from random import randint


class IsaacMap(object):
    """Little class to build map for binding of isaac.
    basic constructor to take width and height values and simple methods to build & also print map to console.
    """
    def __init__(self, width, height, allowed_characters):
        self.width = width
        self.height = height
        self.tile_map = self.build(allowed_characters)

    def build(self, allowed_characters):
        tile_map = []
        for i in range(self.height):
            map_row = []
            for j in range(self.width):
                # pull random character from input
                char_index = randint(0, (len(allowed_characters) - 1))
                map_row.append(allowed_characters[char_index])
            tile_map.append(map_row)

        # override one tile to be special character
        special_x = randint(0, self.width-1)
        special_y = randint(0, self.height-1)
        # height first, then width
        tile_map[special_y][special_x] = '%'

        return tile_map

    def display(self):
        for i in self.tile_map:
            print(i)


if __name__ == "__main__":
    # Not sure if there's much input to test here, I didn't do any as it didn't seem too important to the test
    my_chars = input("Enter allowed characters: ")

    w, h = 10, 10

    test_map = IsaacMap(w, h, my_chars)

    test_map.display()
