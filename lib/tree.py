class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    to_visit = [self.root]

    while len(to_visit) > 0:
      node = to_visit.pop(0)

      if node["id"] == id:
        return node

      to_visit = node["children"] + to_visit