1→X
1→Y
5→P
0→L
1→C
1→D
0→S
ClrHome
Input "SELECT SPEED 1-10:",A
min(10,A→A
max(0,A→A
ClrHome
Repeat G=45 or L=1
Wait ((10-A)/100)
getKey→G
If X=1
1→C
If X=26
­1→C
If Y=1
1→D
If Y=10
Then
If X<P xor X>P+3
1→L
­1→D
S+1→S
End
If G
Output(10,P,"     //four spaces
P-2(G=24 and P>1→P
P+2(G=26 and P<23→P
Output(10,P,"----
Output(Y,X,"  //one space
X+C→X
Y+D→Y
If L=0
Output(Y,X,0
End
ClrHome
Output(4,10,"GAME OVER
Output(5,10,"SCORE:
Output(5,17,S
"