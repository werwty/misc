Thesis: Permissioned blockchain used for governance
Every vote should be anonymous
Every vote should be eligible
Every vote should be zero knowledge, only total vote should be known at the end of the vote. 
Eventually: write a plugin to actual blockchain implementations
Can this (anonymity, eligibility, zk) be done with only hash functions


TODO: look up blockchain, sidechain (etherium casper)

TODO: Look at ZKBoo, circuits, and summarize.

- https://github.com/microsoft/Picnic
 
  - lowMC, ZKB++ (2,3) decomposition
  
  always (2,3) decomp
  
- https://github.com/IAIK/fish-begol
  
  - lowMC
    
- https://github.com/Sobuno/ZKBoo

  - C implementation Sha1 and SHA256
  - Issues with compilation, 

```
    bash-4.4$ gcc MPC_SHA256.c -o MPC_SHA256
In file included from MPC_SHA256.c:17:
shared.h:76:16: error: return type is an incomplete type
 EVP_CIPHER_CTX setupAES(unsigned char key[16]) {
                ^~~~~~~~
shared.h: In function ‘setupAES’:
shared.h:77:17: error: storage size of ‘ctx’ isn’t known
  EVP_CIPHER_CTX ctx;
                 ^~~
shared.h:87:9: warning: ‘return’ with a value, in function returning void
  return ctx;
         ^~~
shared.h:76:16: note: declared here
 EVP_CIPHER_CTX setupAES(unsigned char key[16]) {
                ^~~~~~~~
shared.h: In function ‘getAllRandomness’:
shared.h:96:17: error: storage size of ‘ctx’ isn’t known
  EVP_CIPHER_CTX ctx;
                 ^~~
shared.h: In function ‘init_EVP’:
shared.h:119:2: warning: ‘OPENSSL_config’ is deprecated [-Wdeprecated-declarations]
  OPENSSL_config(NULL);
  ^~~~~~~~~~~~~~
In file included from /usr/include/openssl/opensslconf.h:42,
                 from /usr/include/openssl/e_os2.h:13,
                 from /usr/include/openssl/sha.h:13,
                 from shared.h:12,
                 from MPC_SHA256.c:17:
/usr/include/openssl/conf.h:91:1: note: declared here
 DEPRECATEDIN_1_1_0(void OPENSSL_config(const char *config_name))
 ^~~~~~~~~~~~~~~~~~
MPC_SHA256.c: In function ‘main’:
MPC_SHA256.c:599:16: warning: passing argument 1 of ‘RAND_bytes’ from incompatible pointer type [-Wincompatible-pointer-types]
  if(RAND_bytes(keys, NUM_ROUNDS*3*16) != 1) {
                ^~~~
In file included from shared.h:19,
                 from MPC_SHA256.c:17:
/usr/include/openssl/rand.h:42:31: note: expected ‘unsigned char *’ but argument is of type ‘unsigned char (*)[3][16]’
 int RAND_bytes(unsigned char *buf, int num);
                ~~~~~~~~~~~~~~~^~~
MPC_SHA256.c:603:16: warning: passing argument 1 of ‘RAND_bytes’ from incompatible pointer type [-Wincompatible-pointer-types]
  if(RAND_bytes(rs, NUM_ROUNDS*3*4) != 1) {
                ^~
In file included from shared.h:19,
                 from MPC_SHA256.c:17:
/usr/include/openssl/rand.h:42:31: note: expected ‘unsigned char *’ but argument is of type ‘unsigned char (*)[3][4]’
 int RAND_bytes(unsigned char *buf, int num);
                ~~~~~~~~~~~~~~~^~~
MPC_SHA256.c:619:16: warning: passing argument 1 of ‘RAND_bytes’ from incompatible pointer type [-Wincompatible-pointer-types]
  if(RAND_bytes(shares, NUM_ROUNDS*3*i) != 1) {
                ^~~~~~
In file included from shared.h:19,
                 from MPC_SHA256.c:17:
/usr/include/openssl/rand.h:42:31: note: expected ‘unsigned char *’ but argument is of type ‘unsigned char (*)[3][(sizetype)(i)]’
 int RAND_bytes(unsigned char *buf, int num);
                ~~~~~~~~~~~~~~~^~~
MPC_SHA256.c:668:45: warning: passing argument 4 of ‘H’ from incompatible pointer type [-Wincompatible-pointer-types]
   H(keys[k][0], localViews[k][0], rs[k][0], &hash1);
                                             ^~~~~~
In file included from MPC_SHA256.c:17:
shared.h:127:71: note: expected ‘unsigned char *’ but argument is of type ‘unsigned char (*)[32]’
 void H(unsigned char k[16], View v, unsigned char r[4], unsigned char hash[SHA256_DIGEST_LENGTH]) {
                                                         ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~
MPC_SHA256.c:670:45: warning: passing argument 4 of ‘H’ from incompatible pointer type [-Wincompatible-pointer-types]
   H(keys[k][1], localViews[k][1], rs[k][1], &hash1);
                                             ^~~~~~
In file included from MPC_SHA256.c:17:
shared.h:127:71: note: expected ‘unsigned char *’ but argument is of type ‘unsigned char (*)[32]’
 void H(unsigned char k[16], View v, unsigned char r[4], unsigned char hash[SHA256_DIGEST_LENGTH]) {
                                                         ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~
MPC_SHA256.c:672:45: warning: passing argument 4 of ‘H’ from incompatible pointer type [-Wincompatible-pointer-types]
   H(keys[k][2], localViews[k][2], rs[k][2], &hash1);
                                             ^~~~~~
In file included from MPC_SHA256.c:17:
shared.h:127:71: note: expected ‘unsigned char *’ but argument is of type ‘unsigned char (*)[32]’
 void H(unsigned char k[16], View v, unsigned char r[4], unsigned char hash[SHA256_DIGEST_LENGTH]) {
                                                         ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~
```

kekkec shake

- https://github.com/XKCP/XKCP



TODO: look up crypto 2019 libra


- Ligero: https://acmccs.github.io/papers/p2087-amesA.pdf
    sha 256

- https://github.com/scipr-lab/libsnark

Look at related works, implementations of ZK
Check power complexity
Comparisons to other works
Types of hashes used (nonstandard, lowMC)
Keep eye for critisim of low MC (has it been analyzed enough)
