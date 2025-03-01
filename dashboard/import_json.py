import json
import os
from datetime import datetime
from django.utils import timezone
from dashboard.models import DataPoint  # Ensure correct model import

# Path to your JSON file
json_file_path = os.path.join(os.path.dirname(__file__), "jsondata.json")

# Load JSON data
with open(json_file_path, encoding="utf-8") as file:
    data = json.load(file)

# Function to convert date strings to timezone-aware datetime objects
def parse_datetime(date_str):
    if not date_str:
        return timezone.now()  # Default to now if empty/missing
    try:
        return timezone.make_aware(datetime.strptime(date_str, "%B, %d %Y %H:%M:%S"))
    except ValueError:
        return timezone.now()  # Fallback if the format is unexpected

# Iterate over records and save to database
for item in data:
    DataPoint.objects.create(
        end_year=item.get("end_year") or None,
        intensity=item.get("intensity", 0),
        sector=item.get("sector", "Unknown"),
        topic=item.get("topic", "General"),
        insight=item.get("insight", ""),
        url=item.get("url", ""),
        region=item.get("region", ""),
        start_year=item.get("start_year") or None,
        impact=item.get("impact") or None,
        added=parse_datetime(item.get("added")),
        published=parse_datetime(item.get("published")),  # Convert and ensure non-null
        country=item.get("country", ""),
        relevance=item.get("relevance", 1),
        pestle=item.get("pestle", ""),
        source=item.get("source", ""),
        title=item.get("title", ""),
        likelihood=item.get("likelihood", 1),
    )

print("Data imported successfully!")
