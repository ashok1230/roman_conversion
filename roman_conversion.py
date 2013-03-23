class read:
   def __init__(self):
	d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	x=raw_input("enter roman number: ")
	result=0
	main=0
	a=list(x)
	a.reverse()
	try:
	    for i in a:
	        if d[i]>=main:
		    result+=d[i]
		    main=d[i]
	        else:
		    result-=d[i]
	except KeyError:
	    print 'you enter wrong roman letter'
	else:
	    print result
	    
read()	    
	
