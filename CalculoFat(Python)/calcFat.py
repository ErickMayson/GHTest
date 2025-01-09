import json


def calculateRevenue(data):
    revenueData = json.loads(data)

    for day in revenueData:
        if day["day"] > 31:
            raise ValueError(f"Days cannot be greater than 31.")
    dailyValues = [day["value"] for day in revenueData if day["value"] > 0]

    ## Minimum Revenue per day
    minRevenue = min(dailyValues)
    ## Max Revenue per day
    maxRevenue = max(dailyValues)
    ## Average Revenue per day
    avgRevenue = sum(dailyValues) / len(dailyValues)

    daysAboveAvg = sum(1 for value in dailyValues if value > avgRevenue)

    return {
        "minRevenue": minRevenue,
        "maxRevenue": maxRevenue,
        "daysAboveAvg": daysAboveAvg,
    }


## JSON Example
data = """
[
    {"day": 1, "value": 100},
    {"day": 2, "value": 200},
    {"day": 3, "value": 0},
    {"day": 4, "value": 300},
    {"day": 5, "value": 400},
    {"day": 6, "value": 120},
    {"day": 7, "value": 650}
]
"""

result = calculateRevenue(data)
print(result)
