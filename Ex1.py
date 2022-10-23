def is_pal(s):
  s = s.lower()
  return s == s[::-1]

  ans = is_pal(s)
  if ans:
    return True
  else:
    return False

s = "Roma summus amor"
is_pal(s)