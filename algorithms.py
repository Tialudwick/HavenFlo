# houses the stadalone truama informed matching algorith, isolating math scripts from presentation layer
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Standard Haversine formula to find absolute distance in miles between coordinates.
    """
    R = 3958.8  # Earth radius in miles
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def run_trauma_informed_matching(resident, available_beds):
    """
    Evaluates available beds against trauma indicators and returns a sorted list of matches.
    """
    scored_matches = []

    for bed in available_beds:
        score = 100
        prop = bed.room.property
        room = bed.room

        # 1. HARD FILTER: Gender Alignment
        if resident.gender.lower() != room.gender_designation.lower() and room.gender_designation.lower() != 'coed':
            continue

        # 2. HARD FILTER: Geographic Safety (Trauma-Informed Pillar 1: Safety)
        if resident.trigger_latitude and resident.trigger_longitude:
            distance_to_trigger = calculate_distance(
                prop.latitude, prop.longitude, 
                resident.trigger_latitude, resident.trigger_longitude
            )
            if distance_to_trigger < 3.0: # 3-mile mandatory exclusion zone
                continue

        # 3. SOFT FILTER: Claustrophobia / Panic Trait Checks
        if resident.has_claustrophobia_or_panic and "top" in bed.bed_label.lower():
            score -= 30  # Strongly de-prioritize top bunks to reduce panic risk

        # 4. SOFT FILTER: Environmental Sensory Trait Checks
        if resident.needs_low_sensory_environment:
            if room.is_low_sensory:
                score += 15  # Reward highly compatible layouts
            else:
                score -= 20  # Penalize high-traffic areas

        # Keep scores bounded between 0 and 100
        score = max(0, min(score, 100))

        scored_matches.append({
            'bed': bed,
            'score': score,
            'property_name': prop.name,
            'room_number': room.room_number
        })

    # Sort array by highest compatibility score to present optimal choices
    return sorted(scored_matches, key=lambda x: x['score'], reverse=True)
