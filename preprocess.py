import csv

with open( '2.csv' ) as f:
    x = csv.reader( f, delimiter='\t' )
    #count = 0
    
    data_list = []
    for line in x:
        data_list.append( line )
        #print line
        #count += 1
        #if count == 10:
        #   break
        
    header = data_list[0]
    actual_data = data_list[1:]
    hd = dict( [ (i, idx) for (idx, i) in enumerate( header ) ] )
    
    sdr_idx = hd['sdr_id']
    date_idx = hd['date']
    category_idx = hd['category']
    value_idx = hd['value']
    
    interesting_data = [ ( i[date_idx], i[category_idx], i[value_idx], i[sdr_idx] ) for i in actual_data ]
    
print interesting_data[:10]
print [ i for i in interesting_data if i[1] == 'Cases' ][:10]
