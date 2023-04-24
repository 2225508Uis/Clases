
class combi:
  def __init__(self,n,r) -> None:
    if type(n) is list:
      self.n = n
    elif type(n) is int:
      self.n = list(range(1,n+1))
    self.r = r
    self.prm =list(permutations(self.n,self.r))
    self.nprm = len(self.prm)
    self.com =list(combinations(self.n, self.r))
    self.ncom = len(self.com)

  pass
