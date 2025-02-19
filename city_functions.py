# def names(city, country):
    # """Generate neatly formatted names"""
    # names = f"{city}, {country}"
    # return names.title()

def names(city, country, population=''):
   """Generate neatly formatted names"""
   if population:
      names = f"{city}, {country} - {population}"
   else:
      names = f"{city}, {country}"
   return names.title()
