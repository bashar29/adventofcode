from puzzles.day18 import get_operation_without_precedence, print_tree_indented

def test_get_operator():
    expression = [1,'+',2,'*',3,'+',4,'*',5,'+',6]
    expr = expression[::-1]
    expr.append('end')
    print(expr)
    tree = get_operation_without_precedence(expr)
    print_tree_indented(tree)
    print(tree)
    assert (tree.compute_tree() == 71)
    expression = [1,'+','(',2,'*',3,')','+','(',4,'*','(',5,'+',6,')',')']
    expr = expression[::-1]
    expr.append('end')
    for i,e in enumerate(expr):
        if (e == ')'):expression[i] = '('
        elif (e == '('):expression[i] = ')' 
    tree = get_operation_without_precedence(expr)
    print_tree_indented(tree)
    print(tree)
    #assert (tree.compute_tree() == 51)
