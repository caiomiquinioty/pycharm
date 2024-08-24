def notas(*n,sit=False):
    """
    Funcao para analisa notas e situaçao de varios alunos
    :param n:uma ou mais nota dos alunos , aceita varias
    :param sit:valor opcional, indicando se deve ou nao a situaçoo
    :return:dicionario com varios informaçoes saobre a situaçao da turma
    """
    r=dict()
    r['total']=len(n)
    r['maior']=max(n)
    r['menor']=min(n)
    r['media']=sum(n)/len(n)
    if sit:
        if r['media']>=7:
           r ['situação']='Boa'
        elif r['media']>=5:
            r ['situação']='Razoavel'
        else:
            r['situaçao']='ruim'
        return r


resp=notas(5.00,3.00,10,sit=True)
print(resp)
help(notas)
