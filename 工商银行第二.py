import random

print("====================================")
print("|-------中国工商银行账户管理系统-------|")
print("|-------1、开户               -------|")
print("|-------2、存钱               -------|")
print("|-------3、取钱               -------|")
print("|-------4、转账               -------|")
print("|-------5、查询               -------|")
print("|-------6、退出               -------|")
print("====================================")
#开户的逻辑
bank={
    'bank3':{
        'yhm':1,
        'zh':10000000,
        'mima':222222,
        'gj':'中国',
        'sf':'北京',
        'jd':'七马路',
        'mp':'001',
        'yue': 100,
        'khh':'中国工商银行回龙观支行'
},
    'bank2':{
        'yhm':1,
        'zh':11111111,
        'mima':222222,
        'gj':'中国',
        'sf':'北京',
        'jd':'七马路',
        'mp':'001',
        'yue': 100,
        'khh':'中国工商银行回龙观支行'
}
}
bank2={
    'yhm':1,
    'zh':11111111,
    'mima':222222,
    'gj':'中国',
    'sf':'北京',
    'jd':'七马路',
    'mp':'001',
    'yue': 100,
    'khh':'中国工商银行回龙观支行'
}
khh='中国工商银行回龙观支行'
def bank_kaihu(zh,yhm,mima,gj,sf,jd,mp):
    if len(bank) > 100:
        return 3
    if yhm in bank:
        return 2
    bank[yhm]={
        'zh':zh,
        'mima':mima,
        'gj':gj,
        'sf':sf,
        'jd':jd,
        'mp':mp,
        'yue': 0,
        'khh':khh
    }
    return 1
#开户的操作过程

def kaihu():
    yhm=input('请输入用户名：')
    zh=random.randint(00000000,99999999)
    mima=input('请输入密码：')
    gj=input('请输入国籍：')
    sf=input('请输入省份：')
    jd=input('请输入街道：')
    mp=input('请输入门牌：')
    yanzheng=bank_kaihu(zh,yhm,mima,gj,sf,jd,mp)
    if yanzheng == 3:
        print('用户已满，请到其他网点办理业务')
    if yanzheng == 2:
        print('该用户名重复，请重新输入')
    if yanzheng == 1:
        print('开户成功，以下您的信息')
        info = '''
          ------------个人信息------------
            用户名:%s
            账号：%s
            密码：*****
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
        '''
        print(info % (yhm,zh,gj,sf,jd,mp,bank[yhm]['yue'],khh))
#存款
def bank_cunkuan(zh,ckje,yue):
    if zh != bank2['zh']:
        return 2
    else:
        bank2['yue']=bank2['yue']+ckje
        return 1

def cunkuan():
    zh=int(input('请输入存款账号：'))
    ckje=int(input('请输入存款金额：'))
    yue=bank2['yue']+ckje
    yanzheng=bank_cunkuan(zh,ckje,yue)
    if yanzheng == 2:
        print('存款失败，存款账号错误')
    if yanzheng == 1:
        print('存款成功，以下是存款信息')
        info = '''
          ------------存款信息------------
            账号：%s
            存款金额：%s
            账户余额：%s
        '''
        print(info % (zh,ckje,yue))

#取款
def bank_qukuan(zh,qkje,mima,yue):
    if zh != bank2['zh']:
        return 1
    if mima != bank2['mima']:
        return 2
    if qkje > bank2['yue']:
        return 3
    bank2[zh] = {
        'mima': mima,
        'yue': yue,
    }
    return 4

def qunkuan():
    zh=int(input('请输入取款账号：'))
    qkje=int(input('请输入取款金额：'))
    mima=int(input('请输入密码：'))
    yue=bank2['yue']-qkje
    yanzheng=bank_qukuan(zh, qkje, mima,yue)
    if yanzheng == 1:
        print('取款失败，输入的账号不存在')
    if yanzheng == 2:
        print('取款失败，账户密码输入错误')
    if yanzheng == 3:
        print('取款失败，账户余额不足')
    if yanzheng == 4:
        print('取款成功，以下是取款信息')
        info = '''
          ------------取款信息------------
            账号：%s
            取款金额：%s
            账户余额：%s
        '''
        print(info % (zh,qkje,yue))
#转账
def bank_zhuanzhang(zh,zh2,mima,zzje,yue):
    if zh != bank['bank2']['zh'] or zh2  != bank['bank3']['zh']:
        return 1
    if mima != bank['bank2']['mima']:
        return 2
    if zzje > bank['bank2']['yue'] :
        return 3
    bank2[zh] = {
        'mima': mima,
        'yue': 0,
        'khh': khh
    }
    return 4

def zhuanzhang():
    zh2=int(input('请输入转入账户：'))
    zh=int(input('请输入转出账户：'))
    mima=int(input('请输入转出账户密码：'))
    zzje=int(input('请输入转账金额：'))
    yue=bank2['yue']-zzje
    yanzheng = bank_zhuanzhang(zh,zh2,mima,zzje,yue)
    if yanzheng == 1:
        print('转账失败，转入或转出账户不存在')
    if yanzheng == 2:
        print('转账失败，转出账户密码不正确')
    if yanzheng == 3:
        print('转账失败，转出账户余额不足')
    if yanzheng == 4:
        print('转账成功，以下是转账信息')
        info = '''
          ------------取款信息------------
            转入账号：%s
            转出账号：%s
            转账金额：%s
            账户余额：%s
        '''
        print(info % (zh2,zh,zzje,yue))

def bank_chaxun(zh,mima):
    if zh not in bank2.values():
        return 1
    if mima not in bank2.values():
        return 2
    else:
        return bank2

def chaxun():
    zh=int(input('请输入要查询的账户：'))
    mima=int(input('请输入账户密码：'))
    yanzheng=bank_chaxun(zh,mima)
    if yanzheng == 1:
        print('输入的账号错误')
    elif yanzheng == 2:
        print('密码输入错误')
    else:
        print('查询成功，以下是账户信息')
        info = '''
          ------------个人信息------------
            用户名:%s
            账号：%s
            密码：*****
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
                '''
        print(info % (str(yanzheng['yhm']),str(yanzheng['zh']),yanzheng['gj'],yanzheng['sf'],yanzheng['jd'],yanzheng['mp'],str(yanzheng['yue']),yanzheng['khh']))

while True:
    num=input("请输入您要办的业务：")
    if num  == "1":
        print("----------开户----------")
        kaihu()
    elif num == "2":
        print("----------存钱----------")
        cunkuan()
    elif num == "3":
        print("----------取钱----------")
        qunkuan()
    elif num == "4":
        print("----------转账----------")
        zhuanzhang()
    elif num == "5":
        print("----------查询----------")
        chaxun()
    elif num == "6":
        print("----------再见----------")
        break
    else:
        print("----------你就瞎按吧----------")
        break