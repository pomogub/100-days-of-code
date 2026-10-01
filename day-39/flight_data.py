class FlightData:

    def __init__(self):
        self.price = ...
        self.origin_airport = ...
        self.destination_airport = ...
        self.out_date = ...
        self.return_date = ...


def find_cheapest_flight(data, return_date):
    # Handle empty data if no flight data is returned
    # Get data for a flight
    # Find the cheapest flight. Use FlightData to help you.

    cheapest_flight = ...

    return cheapest_flight


# flight["price"] -- this is already a number (no conversion needed)
# flight["flights"][0]["departure_airport"]["id"] -- Origin airport
# flight["flights"][-1]["arrival_airport"]["id"] -- Destination airport
# flight["flights"][0]["departure_airport"]["time"] -- Departure date

# The SerpAPI date is in the YYYY-MM-DD HH:MM format. You can use .split(" ")[0] to get just the date.