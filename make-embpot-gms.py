#!/usr/bin/python

import numpy as np                 #here we load numpy
import time, sys                   #and load some utilities



def testfunction():

        fn=open("/panfs/storage.local/scs/huang/Sara/Embedding/CO_Cu_surface/embedding_ccsd/script_prepare_embpot_for_gamess/convert_binary_ascii/embpot_new_format.ascii","r")

	n1= 80
	n2= 72
	n3 =225 

        n1_new = 80
        n2_new = 80
        n3_new = 80        
   
	a = np.array([8.1267054999999999 ,0.0000000000000000, 0.0000000000000000])
	b = np.array([-4.8760234499999999,5.9718846899999996, 0.0000000000000000])
	c = np.array([ 0.0000000000000000 ,0.0000000000000000,23.9023600000000016])
	A = np.array([[8.1267054999999999 ,0.0000000000000000, 0.0000000000000000], \
                      [-4.8760234499999999,5.9718846899999996, 0.0000000000000000],  \
                      [0.0000000000000000 ,0.0000000000000000,23.9023600000000016]])

	cu1 = np.array([-0.302710274,3.620341723,8.054210156])
	cu2 = np.array([-1.928160706,5.633547035,8.054144880])
	cu3 = np.array([-2.705663540,3.329606143,7.454081750])
	H   = np.array([-1.779193721,4.094989652,8.809879039])

	C1_old = (cu1[0]+ cu2[0]+ cu3[0]+H[0])/4
        C2_old = (cu1[1]+ cu2[1]+ cu3[1]+H[1])/4
        C3_old = (cu1[2]+ cu2[2]+ cu3[2]+H[2])/4
                  
        c1_new = 10/2
        c2_new = 10/2
        c3_new = 10/2
         
        d1 = c1_new-C1_old 
        d2 = c1_new-C1_old
        d3 = c1_new-C1_old

        #for i  in fn.readlines():
             
        q_new = [10/n1_new * i ,10/n2_new * j , 10/n3_new * k]
        
        

   
   
