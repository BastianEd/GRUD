from PIL import Image, ImageChops
from utils import get_determine_animal, get_center_of_mass, display_map


### TESTS ###
def test(n, f, tests, type_=None):
    success = failed = 0
    for input_, output_ in tests:
        try:
            if type_ == 'img':
                assert sum(r+g+b+a for r,g,b,a in ImageChops.difference(f(input_), Image.open(output_)).getdata()) < 10
            else:
                assert f(input_) == output_
            success += 1
        except AssertionError:
            failed += 1
    print(f"TEST {n}: {success} exitosos y {failed} erróneos")

tests1 = [
    (1, 'Gallina'),
    (1.5, 'Gallina'),
    (2, 'Ganso'),
    (3.5, 'Ganso'),
    (20, 'Oveja'),
    (50, 'Oveja'),
    (80, 'Cerdo'),
    (240, 'Cerdo'),
    (400, 'Caballo'),
    (600, 'Caballo'),
]
tests2 = [
    ([(1, 1, 1), (2, 4, 4)], (3, 3)),
    ([(1, 0, 0), (2, -2, 9),], (-1.33, 6)),
    ([(100, 1.56, 1.23), (150, 4.67, 5.64), (1, 1245, 5432)], (8.37, 25.5)),
    ]

tests3 = [
    ([(1, 275491, 6312596), (2, 275591, 6312696), (20, 275691, 6312796), (80, 275791, 6312896), (400, 275891, 6312996), (400, 275991, 6313096)], 'test-resources/1.png'),
    ]

test(1, get_determine_animal, tests1)
test(2, get_center_of_mass, tests2)
test(3, display_map, tests3, 'img')