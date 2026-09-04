"""Documented command-line entry point for TiBot's school data features."""

from __future__ import annotations

import argparse
import json
from datetime import date

from school_api import NeisClient


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Query Korean school information from NEIS.")
    parser.add_argument("--school", required=True, help="School name, for example 서울고등학교")
    parser.add_argument(
        "--action", choices=("school", "meal", "schedule", "timetable"), default="school"
    )
    parser.add_argument("--date", default=date.today().strftime("%Y%m%d"), help="YYYYMMDD")
    parser.add_argument("--grade", help="Grade for timetable queries")
    parser.add_argument("--class-name", help="Class name for timetable queries")
    parser.add_argument("--api-key", help="Optional NEIS key (prefer TIBOT_NEIS_API_KEY)")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    client = NeisClient(api_key=args.api_key)
    school = client.select_school(args.school)
    if args.action == "school":
        result = school
    elif args.action == "meal":
        result = client.meal(school, args.date)
    elif args.action == "schedule":
        result = client.schedule(school, args.date)
    else:
        if not args.grade or not args.class_name:
            raise SystemExit("--grade and --class-name are required for timetable queries")
        result = client.timetable(school, args.date, args.grade, args.class_name)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
