# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is {alien_0['color']}.")

alien_0 = {'x_postion': 0, 'y_postion': 25, 'speed': 'medium'}
print(f"Original postion: {alien_0['x_postion']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_postion'] = alien_0['x_postion'] + x_increment

print(f"New position: {alien_0['x_postion']}")
