pkg load control

a1 = 1;
a2 = 440;
a3 = 5500;

w1 = 40;
w2 = 440;
w3 = 5500;

H1 = tf( [a1 0], [1 w1] );
H2 = tf( [a2], [1 w2] );
H3 = tf( [a3], [1 w3] );

H = H1*H2*H3

bode(H, [1e-1:5:1e6])

