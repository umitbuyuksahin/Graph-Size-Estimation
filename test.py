def onay_al(prompt, denemeler=4, sikayet='Evet veya hayr, lutfen !'):
	while True:
        	ok = raw_input(prompt)
        	if ok in ('e', 'evet'): return 1
        	if ok in ('h', 'hayr'): return 0
        	denemeler = denemeler - 1
        	if denemeler < 0: raise IOError, 'kararsz kullanici'
	       	print sikayet

onay_al('Cikacan mi LAYNNNNNNNNNN?')
