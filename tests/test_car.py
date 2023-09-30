"""Test for Car class"""


class TestCar:
    """Test class for Car model."""
    
    def test_move_distance_traveled_modified(self, car):
       
       car.move(4)

       assert 4 == car.distance_traveled

       car.move(5)

       assert 9 == car.distance_traveled

    def test_move_distance_traveled_modified_negative(self, car):
       
       car.move(-1)

       assert 0 == car.distance_traveled 

    def test_move_distance_traveled_modified_upper(self, car):
       
       car.move(1000)

       assert 5 == car.distance_traveled
    def test_move_distance_traveled_with_bad_class(self, carInvalid):
       carInvalid.move(1000)

       assert 5 == carInvalid.distance_traveled


    def test_run_class(self, car):
       car.run()

       assert car.running == True


    def test_not_run_class(self, car):

       assert car.running == False