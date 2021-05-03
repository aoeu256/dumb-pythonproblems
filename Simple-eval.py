def arithmetic_arranger(problems, answer=False):
    outputS = [[], [], [], []]    
    if len(problems) <= 5: return "Error: Too many problems."
    for prob in problems:
      [a, op, b] = prob.split(" ")
      assert op in '+-'
      assert a.isdigit()
      assert b.isdigit()
      outputS[0].append(a)
      line2 = op + ' ' + b
      outputS[1].append(line2)
      outputS[2].append('-'*len(line2))
      if answer:
        op = {'+':lambda a,b: a+b, '-':lambda a,b: a-b}[op]
        line3 = str(op(int(a), int(b)))
        outputS[3].append(line3)

    arranged_problems = '\n'.join(outputS)
    return arranged_problems
