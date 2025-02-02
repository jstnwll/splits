import reflex as rx
from splits import formulas


class State(rx.State):
    ########################################
    # Time values
    ########################################

    time_hours: str = ""
    time_minutes: str = ""
    time_seconds: str = ""
    time_total: int = 0

    def set_time_hours(self, value: str):
        self.time_hours = value if value.isdigit() else ""
        self.time_total = formulas.time_to_seconds(
            int(self.time_hours or 0),
            int(self.time_minutes or 0),
            int(self.time_seconds or 0),
        )
        self.set_result()

    def set_time_minutes(self, value: str):
        self.time_minutes = value if value.isdigit() else ""
        self.time_total = formulas.time_to_seconds(
            int(self.time_hours or 0),
            int(self.time_minutes or 0),
            int(self.time_seconds or 0),
        )
        self.set_result()

    def set_time_seconds(self, value: str):
        self.time_seconds = value if value.isdigit() else ""
        self.time_total = formulas.time_to_seconds(
            int(self.time_hours or 0),
            int(self.time_minutes or 0),
            int(self.time_seconds or 0),
        )
        self.set_result()

    ########################################
    # Pace values
    ########################################

    pace_hours: str = ""
    pace_minutes: str = ""
    pace_seconds: str = ""
    pace_total: int = 0

    def set_pace_hours(self, value: str):
        self.pace_hours = value if value.isdigit() else ""
        self.pace_total = formulas.time_to_seconds(
            int(self.pace_hours or 0),
            int(self.pace_minutes or 0),
            int(self.pace_seconds or 0),
        )
        self.set_result()

    def set_pace_minutes(self, value: str):
        self.pace_minutes = value if value.isdigit() else ""
        self.pace_total = formulas.time_to_seconds(
            int(self.pace_hours or 0),
            int(self.pace_minutes or 0),
            int(self.pace_seconds or 0),
        )
        self.set_result()

    def set_pace_seconds(self, value: str):
        self.pace_seconds = value if value.isdigit() else ""
        self.pace_total = formulas.time_to_seconds(
            int(self.pace_hours or 0),
            int(self.pace_minutes or 0),
            int(self.pace_seconds or 0),
        )
        self.set_result()

    ########################################
    # Distance values
    ########################################

    distance: str = ""
    distance_value: str = ""
    use_km: bool = False

    def set_distance(self, value: str):
        distances = {
            "5k": "3.1",
            "10k": "6.2",
            "Half Marathon": "13.1",
            "Marathon": "26.2",
            "50k": "31.1",
            "50 miler": "50",
            "100k": "62.14",
            "100 miler": "100",
        }
        if value in distances:
            self.distance = distances[value]
            self.distance_value = value
        elif value == "Select Event":
            self.distance = ""
            self.distance_value = ""
        else:
            self.distance = ""
            self.distance_value = ""
        self.set_result()

    def set_custom_distance(self, value: str):
        self.distance = value if value.replace(".", "", 1).isdigit() else ""
        self.set_result()

    ########################################
    # Views (Calculator Type)
    ########################################

    result: str = "00:00:00"
    calculator_type: str = "Pace"
    view_pace: bool = False
    view_time: bool = True
    view_distance: bool = True

    def set_calculator_type(self, value: str):
        self.reset_values()
        self.calculator_type = value
        self.set_result()

        if self.calculator_type == "Pace":
            self.view_pace = False
            self.view_time = True
            self.view_distance = True
        elif self.calculator_type == "Time":
            self.view_pace = True
            self.view_time = False
            self.view_distance = True
        elif self.calculator_type == "Distance":
            self.view_pace = True
            self.view_time = True
            self.view_distance = False

    def set_result(self):
        self.time_total = formulas.time_to_seconds(
            int(self.time_hours or 0),
            int(self.time_minutes or 0),
            int(self.time_seconds or 0),
        )
        self.pace_total = formulas.time_to_seconds(
            int(self.pace_hours or 0),
            int(self.pace_minutes or 0),
            int(self.pace_seconds or 0),
        )
        self.result = "00:00:00"

        if self.calculator_type == "Pace":
            if self.distance:
                pace = formulas.calculate_pace(self.time_total, float(self.distance))
                self.result = formulas.seconds_to_time(pace)

        if self.calculator_type == "Time":
            if self.distance:
                time = formulas.calculate_time(self.pace_total, float(self.distance))
                self.result = formulas.seconds_to_time(time)

        if self.calculator_type == "Distance":
            self.result = f"{formulas.calculate_distance(self.pace_total, self.time_total):.1f} mi"

    def reset_values(self):
        self.time_hours = ""
        self.time_minutes = ""
        self.time_seconds = ""
        self.time_total = 0

        self.pace_hours = ""
        self.pace_minutes = ""
        self.pace_seconds = ""
        self.pace_total = 0

        self.distance = ""
        self.distance_value = ""
        self.use_km = False

        self.result = "00:00:00"
