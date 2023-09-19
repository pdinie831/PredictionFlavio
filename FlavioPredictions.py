import flavio
import flavio.plots
import math
from prettytable import PrettyTable
from flavio.classes import Parameter

#
# q^2 bins defined as in "CMS Collaboration, Phys. Lett. B, 753 (2017) 424"
#
print('============= * FLAVIO * =============') 
##
#
print('\n=============================\n') 
print('=>B0->K*mumu [P(\') obs]\n') 
#
table = PrettyTable()
table.field_names = ["q^2 bin", "FL", "P1", "P2", "P3","P4p","P5p","P6p","P8p"]
for q2Bin in range(0,8):
    print('================================\n') 
    print('   q2Bin = %d\n'%(q2Bin)) 
    print('================================\n') 
    
    if (q2Bin==0) :
     q2min=1
     q2max=2
    if (q2Bin==1) :
     q2min=2
     q2max=4.3
    if (q2Bin==2) :
     q2min=4.3
     q2max=6
    if (q2Bin==3) :
     q2min=6
     q2max=8.68
    if (q2Bin==4) :
     continue
    if (q2Bin==5) :
     q2min=10.09
     q2max=12.86
    if (q2Bin==6) :
     continue
    if (q2Bin==7) :
     q2min=14.18
     q2max=16

    FL_Val = flavio.sm_prediction('<FL>(B0->K*mumu)',q2min,q2max)
    FL_Err = flavio.sm_uncertainty('<FL>(B0->K*mumu)',q2min,q2max)
    FL_Frm = '{:+.5f}+/-{:+.5f}'.format(FL_Val,FL_Err)
    print('<FL>(B0->K*mumu) = ',FL_Frm)
    #
    P1_Val = flavio.sm_prediction('<P1>(B0->K*mumu)',q2min,q2max)
    P1_Err = flavio.sm_uncertainty('<P1>(B0->K*mumu)',q2min,q2max)
    P1_Frm = '{:+.5f}+/-{:+.5f}'.format(P1_Val,P1_Err)
    print('<P1>(B0->K*mumu) = ',P1_Frm)
    #
    P2_Val = flavio.sm_prediction('<P2>(B0->K*mumu)',q2min,q2max)
    P2_Err = flavio.sm_uncertainty('<P2>(B0->K*mumu)',q2min,q2max)
    P2_Frm = '{:+.5f}+/-{:+.5f}'.format(P2_Val,P2_Err)
    print('<P2>(B0->K*mumu) = ',P2_Frm)
    #
    #
    P3_Val = flavio.sm_prediction('<P3>(B0->K*mumu)',q2min,q2max)
    P3_Err = flavio.sm_uncertainty('<P3>(B0->K*mumu)',q2min,q2max)
    P3_Frm = '{:+.5f}+/-{:+.5f}'.format(P3_Val,P3_Err)
#    P3_Frm = '{:+.5f}'.format(P3_Val)
    print('<P3>(B0->K*mumu) = ',P3_Frm)
    #
    P4p_Val = flavio.sm_prediction('<P4p>(B0->K*mumu)',q2min,q2max)
    P4p_Err = flavio.sm_uncertainty('<P4p>(B0->K*mumu)',q2min,q2max)
    P4p_Frm = '{:+.5f}+/-{:+.5f}'.format(P4p_Val,P4p_Err)
    print('<P4p>(B0->K*mumu) = ',P4p_Frm)
    #
    P5p_Val = flavio.sm_prediction('<P5p>(B0->K*mumu)',q2min,q2max)
    P5p_Err = flavio.sm_uncertainty('<P5p>(B0->K*mumu)',q2min,q2max)
    P5p_Frm = '{:+.5f}+/-{:+.5f}'.format(P5p_Val,P5p_Err)
    print('<P5p>(B0->K*mumu) = ',P5p_Frm)
    #
    P6p_Val = flavio.sm_prediction('<P6p>(B0->K*mumu)',q2min,q2max)
    P6p_Err = flavio.sm_uncertainty('<P6p>(B0->K*mumu)',q2min,q2max)
    P6p_Frm = '{:+.5f}+/-{:+.5f}'.format(P6p_Val,P6p_Err)
#    P6p_Frm = '{:+.5f}'.format(P6p_Val)
    print('<P6p>(B0->K*mumu) = ',P6p_Frm)
    #
    P8p_Val = flavio.sm_prediction('<P8p>(B0->K*mumu)',q2min,q2max)
    P8p_Err = flavio.sm_uncertainty('<P8p>(B0->K*mumu)',q2min,q2max)
    P8p_Frm = '{:+.5f}+/-{:+.5f}'.format(P8p_Val,P8p_Err)
#    P8p_Frm = '{:+.5f}'.format(P8p_Val)
    print('<P8p>(B0->K*mumu) = ',P8p_Frm)
    table.add_row([q2Bin,FL_Frm, P1_Frm, P2_Frm, P3_Frm,P4p_Frm,P5p_Frm,P6p_Frm,P8p_Frm ])
#
print(table)


