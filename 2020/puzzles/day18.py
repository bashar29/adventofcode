
#https://www.geeksforgeeks.org/program-to-convert-infix-notation-to-expression-tree/?ref=rp
#https://www.openbookproject.net/thinkcs/archive/python/thinkcspy3e_abandoned/ch20.html
#https://ksvi.mff.cuni.cz/~dingle/2019/algs/lecture_11.html#expression%20trees|outline

class Tree:
    
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def compute_tree(self):
        if self.cargo == '*':
            return self.left.compute_tree() * self.right.compute_tree()
        elif self.cargo == '+':
            return self.left.compute_tree() + self.right.compute_tree()
        else:
            return self.cargo

def print_tree(tree):
    if tree == None: return
    print(tree.cargo, end=' ')
    print_tree(tree.left)
    print_tree(tree.right)

def print_tree_inorder(tree):
    if tree == None: return
    print_tree_inorder(tree.left)
    print(tree.cargo, end=' ')
    print_tree_inorder(tree.right)

def print_tree_postorder(tree):
    if tree == None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end=' ')

def print_tree_indented(tree, level=0):
    if tree == None: return
    print_tree_indented(tree.right, level+1)
    print('-' * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    else:
        return False

def get_number_without_precedence(token_list):
    if get_token(token_list, '('):
        x = get_operation_without_precedence(token_list)         # get the subexpression
        get_token(token_list, ')')      # remove the closing parenthesis
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        token_list[0:1] = []
        return Tree (x, None, None)

def get_number_with_precedence(token_list):
    if get_token(token_list, '('):
        x = get_product(token_list)         # get the subexpression
        get_token(token_list, ')')      # remove the closing parenthesis
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        token_list[0:1] = []
        return Tree (x, None, None)

def get_operation_without_precedence(token_list):
    a = get_number_without_precedence(token_list)
    if get_token(token_list, '*'):
        b = get_operation_without_precedence(token_list)
        return Tree ('*', a, b)
    elif get_token(token_list, '+'):
        b = get_operation_without_precedence(token_list)
        return Tree ('+', a, b)
    else:
        return a

def get_product(token_list):
    a = get_sum(token_list)
    if get_token(token_list, '*'):
        b = get_product(token_list)
        return Tree ('*', a, b)
    else:
        return a

def get_sum(token_list):
    a = get_number_with_precedence(token_list)
    if get_token(token_list, '+'):
        b = get_sum(token_list)
        return Tree ('+', a, b)
    else:
        return a

def parse_expression_without_precedence(expression):
    for i,expr in enumerate(expression):
        if expr not in ('(',')','*','+'):
            expression[i] = int(expr)
        if (expr == ')'):expression[i] = '('
        elif (expr == '('):expression[i] = ')' 
    expression.append('end')
    tree = get_operation_without_precedence(expression)
    return tree
    #print_tree_indented(tree)
    #print_tree_inorder(tree)

def parse_expression_with_precedence(expression):
    for i,expr in enumerate(expression):
        if expr not in ('(',')','*','+'):
            expression[i] = int(expr)
        if (expr == ')'):expression[i] = '('
        elif (expr == '('):expression[i] = ')' 
    expression.append('end')
    tree = get_product(expression)
    return tree
    #print_tree_indented(tree)

def get_puzzle_input(filename):
    with open(filename,'r') as file:
        expressions = []
        for line in file:
            # binary tree will be construct from the reverted string, to resolve from left to right
            # and not from right to left
            expressions.append([d for d in [*line[::-1].strip()] if d != ' '])
        return expressions

def first_star():
    expressions = get_puzzle_input('../data/inputday18.txt')
    result = 0
    for i,expr in enumerate(expressions):
        tree = parse_expression_without_precedence(expr)
        result += tree.compute_tree()
    #tree = parse_expression([1,'+',2,'*',3,'+',4,'*',5,'+',6])
    #result = tree.compute_tree()
    print("[* ] sum of each expression : %s"%result)

def second_star():
    expressions = get_puzzle_input('../data/inputday18.txt')
    result = 0
    for i,expr in enumerate(expressions):
        tree = parse_expression_with_precedence(expr)
        result += tree.compute_tree()
    #tree = parse_expression_with_precedence([1,'+',2,'*',3,'+',4,'*',5,'+',6])
    #result = tree.compute_tree()
    print("[**] sum of each expression : %s"%result)    

if __name__ == "__main__":
    first_star()
    second_star()
