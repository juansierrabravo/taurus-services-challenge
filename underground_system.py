"""Problema 3:

Un sistema ferroviario está haciendo un seguimiento de los tiempos de 
viaje de los clientes entre diferentes estaciones. Están usando estos 
datos para calcular el tiempo promedio que toma viajar de una estación 
a otra.
"""


class UndergroundSystem:

    def __init__(self):
        """Initializes the UndergroundSystem with empty check-ins and check-outs
        records.
        """
        self.check_ins = []
        self.check_outs = []

    def check_in(self, id_: int, station_name: str, t: int) -> None:
        """Records the check-in of a passenger.

        Args:
            id_: The ID of the passenger.
            station_name: The name of the station where the check-in occurs.
            t: The time of the check-in.
        """
        self.check_ins.append(
            {
                "passenger_id": id_,
                "station_name": station_name,
                "t": t,
            }
        )

    def check_out(self, id_: int, station_name: str, t: int) -> None:
        """Records the check-out of a passenger.

        Args:
            id_ : The ID of the passenger.
            station_name: The name of the station where the check-out occurs.
            t: The time of the check-out.
        """
        self.check_outs.append(
            {
                "passenger_id": id_,
                "station_name": station_name,
                "t": t,
            }
        )

    def get_average_time(self, start_station: str, end_station: str):
        """Calculates the average travel time between two stations.

        Args:
            start_station: The starting station name.
            end_station: The ending station name.

        Returns:
            float: The average travel time from start_station to end_station.

        Note:
            Assumes a one-to-one correspondence between check-ins and check-outs.
        """

        # Pair each check-in with its corresponding check-out
        travels = zip(self.check_ins, self.check_outs)

        # Filter pairs to only those that start at start_station and end at end_station
        travels_between_stations = [
            travel
            for travel in travels
            if travel[0]["station_name"] == start_station
            and travel[1]["station_name"] == end_station
        ]

        # Initialize lists to hold check-in and check-out times
        check_in_times = []
        check_out_times = []

        # Extract times from the filtered travels
        for check_in_record, check_out_record in travels_between_stations:
            check_in_times.append(check_in_record["t"])
            check_out_times.append(check_out_record["t"])

        # Calculate the travel time for each pair of check-in and check-out times
        travel_times = [
            check_out_time - check_in_time
            for check_in_time, check_out_time in zip(check_in_times, check_out_times)
        ]

        # Calculate and return the average travel time
        return sum(travel_times) / len(travel_times)
