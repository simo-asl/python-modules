from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime

from typing import Self


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        if not any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                member.years_experience >= 5
                for member in self.crew
            )
            if experienced_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need at least 50% experienced crew"
                )

        return self


def print_mission_details(mission: SpaceMission) -> None:
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions:.1f}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} "
            f"({member.rank.value}) - {member.specialization}"
        )


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    valid_crew: list[CrewMember] = [
        CrewMember(
            member_id="CM01",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=40,
            specialization="Mission Command",
            years_experience=20,
        ),
        CrewMember(
            member_id="CM02",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=38,
            specialization="Navigation",
            years_experience=18,
        ),
        CrewMember(
            member_id="CM03",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=35,
            specialization="Engineering",
            years_experience=9,
        ),
    ]

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-01-29 20:00",
            duration_days=900,
            crew=valid_crew,
            budget_millions=2500.0,
        )
        print_mission_details(valid_mission)

    except ValidationError as e:
        print("Unexpected validation error:")
        print(e)

    print()
    print("=" * 40)
    print("Expected validation error:")

    invalid_crew: list[CrewMember] = [
        CrewMember(
            member_id="CM01",
            name="Sarah Connor",
            rank=Rank.OFFICER,
            age=40,
            specialization="Mission Command",
            years_experience=20,
        ),
        CrewMember(
            member_id="CM02",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=38,
            specialization="Navigation",
            years_experience=18,
        ),
        CrewMember(
            member_id="CM03",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=35,
            specialization="Engineering",
            years_experience=9,
        ),
    ]

    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-01-29 20:00",
            duration_days=900,
            crew=invalid_crew,
            budget_millions=2500.0,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
