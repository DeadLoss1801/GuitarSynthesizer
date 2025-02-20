from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import Self

type Numeric = int | float | Decimal | Fraction

@dataclass(frozen=True)
class Time:
    seconds: Decimal

    @classmethod
    def from_milliseconds(cls, milliseconds: Numeric) -> Self:
        return cls(Decimal(str(float(milliseconds))) / 1000)