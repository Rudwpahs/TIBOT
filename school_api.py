"""Small client for the Korean NEIS Open API used by TiBot."""

from __future__ import annotations

import os
from typing import Any

import requests


BASE_URL = "https://open.neis.go.kr/hub"


class NeisClient:
    def __init__(self, api_key: str | None = None, timeout: float = 10.0):
        self.api_key = api_key or os.getenv("TIBOT_NEIS_API_KEY")
        if not self.api_key:
            raise ValueError("Set TIBOT_NEIS_API_KEY or pass api_key explicitly.")
        self.timeout = timeout

    def _get(self, endpoint: str, **params: str) -> list[dict[str, Any]]:
        query: dict[str, Any] = {"KEY": self.api_key, "Type": "json", **params}
        response = requests.get(f"{BASE_URL}/{endpoint}", params=query, timeout=self.timeout)
        response.raise_for_status()
        payload = response.json()
        block = payload.get(endpoint, [])
        if len(block) < 2 or not isinstance(block[1], dict):
            return []
        return block[1].get("row", [])

    def find_school(self, name: str) -> list[dict[str, Any]]:
        return self._get("schoolInfo", SCHUL_NM=name)

    def select_school(self, name: str) -> dict[str, Any]:
        schools = self.find_school(name)
        if not schools:
            raise LookupError(f"No school found for: {name}")
        return schools[0]

    def _school_params(self, school: dict[str, Any]) -> dict[str, str]:
        return {
            "ATPT_OFCDC_SC_CODE": school["ATPT_OFCDC_SC_CODE"],
            "SD_SCHUL_CODE": school["SD_SCHUL_CODE"],
        }

    def meal(self, school: dict[str, Any], date: str) -> list[dict[str, Any]]:
        return self._get("mealServiceDietInfo", MLSV_YMD=date, **self._school_params(school))

    def schedule(self, school: dict[str, Any], date: str) -> list[dict[str, Any]]:
        return self._get("SchoolSchedule", AA_YMD=date, **self._school_params(school))

    def timetable(
        self, school: dict[str, Any], date: str, grade: str, class_name: str
    ) -> list[dict[str, Any]]:
        return self._get(
            "hisTimetable",
            ALL_TI_YMD=date,
            GRADE=grade,
            CLASS_NM=class_name,
            **self._school_params(school),
        )
