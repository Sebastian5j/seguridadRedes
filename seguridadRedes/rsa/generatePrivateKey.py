import random, sys, os, rabinMiller, cryptomath
import sys

def main():
    if len(sys.argv) != 4:
        sys.stderr.write('Usage: %s p q e\n' % sys.argv[0])
        sys.exit(1)

    p, q, e = [ long(a,16) for a in sys.argv[1:] ]

    conf = get_asn1conf( build_key(p,q,e) )

    sys.stderr.write(helptext)
    d = cryptomath.findModInverse(e, (p - 1) * (q - 1))
    print conf

if __name__ == "__main__":
    main()


