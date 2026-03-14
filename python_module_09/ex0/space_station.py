from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):

    station_id: str = Field(..., min_length=3, max_length=10,
                            description="Unique station ID")
    name: str = Field(..., min_length=1, max_length=50,
                      description="Station name")
    crew_size: int = Field(..., ge=1, le=20,
                           description="Number of crew members")
    power_level: float = Field(..., ge=0.0, le=100.0,
                               description="Power level (%)")
    oxygen_level: float = Field(..., ge=0.0, le=100.0,
                                description="Oxygen level (%)")
    last_maintenance: datetime = Field(
        ..., description="UTC timestamp of the last maintenance"
        )
    is_operational: bool = Field(default=True, description="Operational status"
                                 )
    notes: Optional[str] = Field(None, max_length=200,
                                 description="Optional notes about the station"
                                 )


def func() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )

        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(f"Status: "
              f"{'Operational' if valid_station.is_operational else 'Down'}")

    except ValidationError as error:
        print(f"Unexpected error with valid data: {error}")

    print()
    print("=" * 40)

    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(
            station_id="UFT-M00N",
            name="OUR-SPIRIT-WILL-NEVER-DIE",
            crew_size=100,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.now()
        )
        invalid_station.name

    except ValidationError as e:
        for err in e.errors():
            print(f"{err['msg']}")


if __name__ == "__main__":
    func()
