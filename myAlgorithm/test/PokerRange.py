"""
手中一幅扑克牌，假设顺序为ABCDEF，把第一张放到桌面上，第二张挪到最后，第三张放到桌面，第四张挪到最后，一直到所有牌都在桌面

BCDEF　　 A
CDEFB
DEFB　　　AC
EFBD
…

把最后在桌面上的这副牌给你，求出原始牌的顺序
"""

def end_to_start(list=[]):
    if len(list) <= 1:
        pass
    else:
        list.insert(0, list[-1])
        list.pop()
    return list


def pokerArrange(aim_list):
    result= []
    for i in range(len(aim_list), 0, -1):
        end_to_start(result)
        result.insert(0, aim_list[i - 1])

    print result

if __name__=="__main__":
    aim_list = [1, 3, 5, 2, 6, 4]
    # aim_list = ['A', 'C', 'E', 'B', 'F', 'D']
    pokerArrange(aim_list)