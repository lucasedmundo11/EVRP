
def calculate_center_of_gravity(locations):
    """
    Calculate the center of gravity (centroid) of a set of weighted locations.
    
    :param locations: List of tuples, where each tuple contains the (x, y) coordinates and the weight of a location.
    :return: Tuple containing the (x, y) coordinates of the center of gravity.
    """
    if not locations:
        raise ValueError("The list of locations cannot be empty")

    total_weight = sum(location[2] for location in locations)
    if total_weight == 0:
        raise ValueError("The total weight cannot be zero")

    x_weighted_sum = sum(location[0] * location[2] for location in locations)
    y_weighted_sum = sum(location[1] * location[2] for location in locations)

    center_of_gravity = (x_weighted_sum / total_weight, y_weighted_sum / total_weight)
    return center_of_gravity

if __name__ == "__main__":
    # Example usage
    locations = [(2, 3, 1), (4, 5, 2), (6, 7, 3)]
    cog = calculate_center_of_gravity(locations)
    print(f"The center of gravity is at: {cog}")