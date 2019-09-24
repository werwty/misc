## Multi Party Computation

### Goldreich Micali Wigderson (GMW)

    P1 -> x
    P2 -> y
    
    Let x = x1 ⊕ x2
    Let y = y1 ⊕ y2
    
Assumption 1: All computational functions can be expressed as circuits.

All circuits can be expressed with a combination of NOT AND XOR gates
    
Goal: P1 and P2 want to calculate f(x,y) without sharing x,y with each other.

        P1 gives x2 to P2
        P2 gives y1 to P1

        P1 -> x1, y1, x2
        P2 -> x2, y2, y1

Computing the gates are as follows:

    NOT: on predetermined party flips share (e.g. P1 flips x1)
    XOR: since x ⊕ y = (x1 ⊕ x2) ⊕ (y1 ⊕ y2) =  (x1 ⊕ y1) ⊕ (x2 ⊕ y2) each party can xor their shares separately
    
    AND: (x1 ⊕ x2) & (y1 ⊕ y2) 
    
   