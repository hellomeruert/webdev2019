def alarm_clock(day, vacation):
  a = "7:00" if not vacation else "10:00"
  b = "10:00" if not vacation else "off"
  return a if day not in [6,0] else b