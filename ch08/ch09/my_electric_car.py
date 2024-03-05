from car import Car

my_leaf = Car('nissan', 'leaf', 2024)
print(f"전기차는 {my_leaf.get_descriptive_name()}")
print("전기차는 {}".format(my_leaf.get_descriptive_name()))
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()