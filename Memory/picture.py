from random import shuffle


class Picture(object):
  def __init__(self, number_of_pairs, length_of_gamefield, extra_picture=False):
    self.backsite = '~'
    self.number_of_pairs = number_of_pairs
    self.frontsite = self.new_picture(length_of_gamefield, extra_picture)

  def new_picture(self, length_of_gamefield, extra_picture):
    little_alpha = ['a', 'b', 'd', 'e', 'f', 'g', 'h',
                    'i', 'j', 'l', 'm', 'n', 'q', 'r', 't', 'u', 'y']
    frontsite = [chr(i) for i in range(65, 65 + self.number_of_pairs)] * 2

    if (self.number_of_pairs - len(little_alpha)) > 0:
      diff = self.number_of_pairs - len(little_alpha)
      begin = 65 + self.number_of_pairs
      end = begin + diff
      frontsite += [chr(i) for i in range(begin, end)] * 2
      frontsite += little_alpha[:] * 2
    else:
      frontsite += little_alpha[:self.number_of_pairs] * 2

    if extra_picture:
      frontsite += ['Z', 'Z']

    shuffle(frontsite)
    return [frontsite[i:i+length_of_gamefield] for i in range(0, len(frontsite), length_of_gamefield)]
