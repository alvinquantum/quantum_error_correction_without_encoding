OPENQASM 3.0;
include "stdgates.inc";
qubit[20] q;
rz(pi/2) q[0];
sx q[0];
rz(-pi/2) q[1];
sx q[1];
rz(0.45102681179626103) q[1];
sx q[1];
cz q[1], q[0];
sx q[0];
rz(pi/2) q[0];
sx q[1];
rz(-pi/2) q[2];
sx q[2];
rz(2.910115289619614) q[2];
cz q[1], q[2];
sx q[1];
rz(1.3393189628247173) q[1];
sx q[1];
sx q[2];
rz(pi/2) q[2];
cz q[1], q[2];
rz(pi/2) q[1];
sx q[1];
x q[2];
rz(pi/2) q[3];
sx q[3];
rz(0.23794112483020813) q[3];
cz q[2], q[3];
sx q[2];
rz(1.332855201964688) q[2];
sx q[2];
sx q[3];
rz(pi/2) q[3];
cz q[2], q[3];
rz(-pi/2) q[2];
sx q[2];
rz(-pi) q[2];
rz(-pi/2) q[4];
sx q[4];
rz(2.896613990462929) q[4];
cz q[3], q[4];
sx q[3];
rz(1.3258176636680314) q[3];
sx q[3];
sx q[4];
rz(pi/2) q[4];
cz q[3], q[4];
rz(pi/2) q[3];
sx q[3];
x q[4];
rz(pi/2) q[5];
sx q[5];
rz(0.2526802551420779) q[5];
cz q[4], q[5];
sx q[4];
rz(1.3181160716528186) q[4];
sx q[4];
sx q[5];
rz(pi/2) q[5];
cz q[4], q[5];
rz(-pi/2) q[4];
sx q[4];
rz(-pi) q[4];
rz(-pi/2) q[6];
sx q[6];
rz(2.8804352426867688) q[6];
cz q[5], q[6];
sx q[5];
rz(1.3096389158918722) q[5];
sx q[5];
sx q[6];
rz(pi/2) q[6];
cz q[5], q[6];
rz(pi/2) q[5];
sx q[5];
rz(-pi/2) q[7];
sx q[7];
rz(2.8710428906112195) q[7];
cz q[6], q[7];
sx q[6];
rz(1.300246563816322) q[6];
sx q[6];
sx q[7];
rz(pi/2) q[7];
cz q[6], q[7];
rz(pi/2) q[6];
sx q[6];
rz(-pi/2) q[8];
sx q[8];
rz(2.8605577520869794) q[8];
cz q[7], q[8];
sx q[7];
rz(1.2897614252920828) q[7];
sx q[7];
sx q[8];
rz(pi/2) q[8];
cz q[7], q[8];
rz(pi/2) q[7];
sx q[7];
x q[8];
rz(pi/2) q[9];
sx q[9];
rz(0.2928427717285751) q[9];
cz q[8], q[9];
sx q[8];
rz(1.2779535550663201) q[8];
sx q[8];
sx q[9];
rz(pi/2) q[9];
cz q[8], q[9];
rz(-pi/2) q[8];
sx q[8];
rz(-pi) q[8];
x q[9];
rz(pi/2) q[10];
sx q[10];
rz(0.30627736916966875) q[10];
cz q[9], q[10];
sx q[9];
rz(1.2645189576252278) q[9];
sx q[9];
sx q[10];
rz(pi/2) q[10];
cz q[9], q[10];
rz(-pi/2) q[9];
sx q[9];
rz(-pi) q[9];
x q[10];
rz(pi/2) q[11];
sx q[11];
rz(0.32175055439664124) q[11];
cz q[10], q[11];
sx q[10];
rz(1.2490457723982535) q[10];
sx q[10];
sx q[11];
rz(pi/2) q[11];
cz q[10], q[11];
rz(-pi/2) q[10];
sx q[10];
rz(-pi) q[10];
rz(-pi/2) q[12];
sx q[12];
rz(2.801755744135672) q[12];
cz q[11], q[12];
sx q[11];
rz(1.2309594173407739) q[11];
sx q[11];
sx q[12];
rz(pi/2) q[12];
cz q[11], q[12];
rz(pi/2) q[11];
sx q[11];
rz(-pi/2) q[13];
sx q[13];
rz(2.7802255296830847) q[13];
cz q[12], q[13];
sx q[12];
rz(1.2094292028881881) q[12];
sx q[12];
sx q[13];
rz(pi/2) q[13];
cz q[12], q[13];
rz(pi/2) q[12];
sx q[12];
rz(-pi/2) q[14];
sx q[14];
rz(2.753995966934612) q[14];
cz q[13], q[14];
sx q[13];
rz(1.1831996401397147) q[13];
sx q[13];
sx q[14];
rz(pi/2) q[14];
cz q[13], q[14];
rz(pi/2) q[13];
sx q[13];
rz(-pi/2) q[15];
sx q[15];
rz(2.7210583183058272) q[15];
cz q[14], q[15];
sx q[14];
rz(1.1502619915109316) q[14];
sx q[14];
sx q[15];
rz(pi/2) q[15];
cz q[14], q[15];
rz(pi/2) q[14];
sx q[14];
rz(-pi/2) q[16];
sx q[16];
rz(2.677945044588987) q[16];
cz q[15], q[16];
sx q[15];
rz(1.1071487177940895) q[15];
sx q[15];
sx q[16];
rz(pi/2) q[16];
cz q[15], q[16];
rz(pi/2) q[15];
sx q[15];
x q[16];
rz(pi/2) q[17];
sx q[17];
rz(pi/6) q[17];
cz q[16], q[17];
sx q[16];
rz(pi/3) q[16];
sx q[16];
sx q[17];
rz(pi/2) q[17];
cz q[16], q[17];
rz(-pi/2) q[16];
sx q[16];
rz(-pi) q[16];
sx q[17];
rz(-3*pi/2) q[17];
rz(pi/2) q[18];
sx q[18];
rz(2.1862760354652835) q[18];
sx q[18];
cz q[17], q[18];
sx q[17];
sx q[18];
rz(-2.1862760354652844) q[18];
sx q[18];
rz(pi/2) q[18];
rz(pi/2) q[19];
sx q[19];
rz(-pi/2) q[19];
cz q[18], q[19];
cz q[18], q[17];
sx q[17];
rz(pi/2) q[17];
sx q[18];
rz(pi) q[18];
sx q[19];
rz(3*pi/4) q[19];
cz q[18], q[19];
sx q[18];
rz(pi/4) q[18];
sx q[18];
sx q[19];
rz(-pi/2) q[19];
cz q[18], q[19];
rz(-pi/2) q[18];
sx q[18];
rz(pi/2) q[18];
sx q[19];
rz(-pi/2) q[19];
