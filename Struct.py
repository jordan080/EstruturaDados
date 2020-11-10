class CovidLine:
  def __init__(self, ch, observation_date, province_state, country_region, last_update, confirmed, deaths, recovered):    
    self.ch = ch
    self.observation_date = observation_date
    self.province_state = province_state
    self.country_region = country_region
    self.last_update = last_update
    self.confirmed = confirmed
    self.deaths = deaths
    self.recovered = recovered