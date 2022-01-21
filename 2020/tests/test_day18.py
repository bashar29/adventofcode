from puzzles.day18 import get_operator, print_tree_indented

def test_get_operator():
    expression = [1,'+',2,'*',3,'+',4,'*',5,'+',6,'end']
    print(expression)
    tree = get_operator(expression)
    print_tree_indented(tree)
    print(tree)
    assert (tree.compute() == 71)
    expression = [1,'+','(',2,'*',3,')','+','(',4,'*','(',5,'+',6,')',')','end']
    tree = get_operator(expression)
    print_tree_indented(tree)
    print(tree)
    assert (tree.compute_tree() == 51)
