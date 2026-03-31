import re

def parse_receipt(text):
    trips = []

    # Regex for each booking line
    pattern = re.findall(
        r'(BKN\d+)\s+.*?\s+(\d+,\d+)\s+(\d{2}-\d{2}-\d{4})\s+\d{2}:\d{2}\s+-\s+\d{2}-\d{2}-\d{4}\s+\d{2}:\d{2}.*?€(\d+,\d{2})',
        text
    )

    for booking_id, distance, date, price in pattern:
        trips.append({
            "booking_id": booking_id,
            "date": date,
            "distance_km": float(distance.replace(",", ".")),
            "price": float(price.replace(",", "."))
        })

    return trips