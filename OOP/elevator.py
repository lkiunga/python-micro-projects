class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom= bottom
        self.top =top
        self.current = current
    def __str__(self):
        """Return the current floor"""
        return "Current Floor: {}".format(self.current)
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            self.current += 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > self.bottom + 1:
            self.current -= 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor >= self.bottom and floor <= self.top:
            self.current = floor
        elif floor < 0:
            self.current = 0
        else:
            self.current = 10

elevator = Elevator(-1, 10, 0)


elevator.up() 
elevator.current #should output 1
elevator.down() 
elevator.current #should output 0
elevator.go_to(10) 
elevator.current #should output 10

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

elevator.go_to(5)
print(elevator)