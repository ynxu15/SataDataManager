# -*- coding: utf-8 -*-

for i in range(10,19):
	for j in range(1,5):
		print "pf_"+str(i)+str(j)+" = models.FloatField(u'利润（20"+str(i)+"年第"+str(j)+"季度）',max_digits=15,decimal_places=2)"