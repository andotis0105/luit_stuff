def unique(given_list=[]):
  to_return = []
  for el in given_list:
    if el not in to_return:
      to_return.append(el)
  return to_return

