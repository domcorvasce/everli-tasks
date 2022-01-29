#!/usr/bin/env python3
from haversine import haversine
from typing import List


def compute_coverage(locations: List[object], shoppers: List[object]) -> List[object]:
    """Compute the percentage of the zone covered by enabled shoppers.

    One shopper covers a zone if the distance among the coordinates is less than 10 km.
    The resulting array is sorted in descending order.

    Args:
      - locations: a set of geographical zones
      - shoppers: a collection of shoppers' locations
    Returns: The percentage of the zone covered by each enabled shopper
    """
    MAX_DISTANCE = 10

    coverages = []
    num_locations = len(locations)
    enabled_shoppers = [shopper for shopper in shoppers if shopper["enabled"]]

    # Extract latitude and longitude of each location once, instead of doing it
    # multiple times when iterating over each *enabled* shopper
    locations_coords = [(location["lat"], location["lng"]) for location in locations]

    # NOTE: This is totally unnecessary for this task, but in a real-world scenario
    # it would allow us to reuse the coverage for shoppers who share the same location
    coverage_cache = {}

    for shopper in enabled_shoppers:
        shopper_coords = (shopper["lat"], shopper["lng"])
        shopper_coverage = {"shopper_id": shopper["id"], "coverage": 0}

        # If the shopper shares the same location of another shopper whose zone coverage
        # has already been computed, then we don't need to compute che coverage manually
        if not coverage_cache.get(shopper_coords) is None:
            shopper_coverage["coverage"] = coverage_cache[shopper_coords]
            coverages.append(shopper_coverage)
            next

        covered_locations = 0

        for location in locations_coords:
            if haversine(shopper_coords, location) < MAX_DISTANCE:
                covered_locations += 1

        shopper_coverage["coverage"] = (covered_locations / num_locations) * 100
        coverages.append(shopper_coverage)
        coverage_cache[shopper_coords] = shopper_coverage["coverage"]

    return sorted(coverages, key=lambda x: x["coverage"], reverse=True)


if __name__ == "__main__":
    locations = [
        {"id": 1000, "zip_code": "37069", "lat": 45.35, "lng": 10.84},
        {"id": 1001, "zip_code": "37121", "lat": 45.44, "lng": 10.99},
        {"id": 1002, "zip_code": "37129", "lat": 45.44, "lng": 11.00},
        {"id": 1003, "zip_code": "37133", "lat": 45.43, "lng": 11.02},
    ]

    shoppers = [
        {"id": "S1", "lat": 45.46, "lng": 11.03, "enabled": True},
        {"id": "S2", "lat": 45.46, "lng": 10.12, "enabled": False},
        {"id": "S3", "lat": 45.34, "lng": 10.81, "enabled": True},
        {"id": "S4", "lat": 45.76, "lng": 10.57, "enabled": False},
        {"id": "S5", "lat": 45.34, "lng": 10.63, "enabled": False},
        {"id": "S6", "lat": 45.42, "lng": 10.81, "enabled": True},
        {"id": "S7", "lat": 45.34, "lng": 10.94, "enabled": True},
    ]

    print(compute_coverage(locations, shoppers))
