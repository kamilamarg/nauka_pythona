def print_dict(d):
     for key in d:
         print("{0}:{1}").format(key, d[key])

if __name__ == "__main__":
    samolot = {'name': 'boeing',
                'przebieg': 1000,
                'type': 'pasazerski'}
   samolot ['nazwa'] = samolot['name']
   samolot.pop('name')
   samolot['typ']= samolot['type']
   samolot.pop('type')

   print_dict(samolot)
