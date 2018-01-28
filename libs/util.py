def getDirection(angle):
    if angle<11.25 or angle>=348.75:
        return "N"
    elif angle<33.75 and angle>=11.25:
        return "NNE"
    elif angle<56.25 and angle>=33.75:
        return "NE"
    elif angle<78.75 and angle>=56.25:
        return "ENE"
    elif angle<101.25 and angle>=78.75:
        return "E"
    elif angle<123.75 and angle>=101.25:
        return "ESE"
    elif angle<146.25 and angle>=123.75:
        return "SE"
    elif angle<168.75 and angle>=146.25:
        return "SSE"
    elif angle<191.25 and angle>=168.75:
        return "S"
    elif angle<213.75 and angle>=191.25:
        return "SSW"
    elif angle<236.25 and angle>=213.75:
        return "SW"
    elif angle<258.75 and angle>=236.25:
        return "WSW"
    elif angle<281.25 and angle>=258.75:
        return "W"
    elif angle<303.75 and angle>=281.25:
        return "WNW"
    elif angle<326.25 and angle>=303.75:
        return "NW"
    elif angle<348.75 and angle>=326.25:
        return "NNW"