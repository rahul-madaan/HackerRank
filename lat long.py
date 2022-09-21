from statistics import mean

br_lat = 28.524763
br_long = 77.574445
tr_lat = 28.524760
tr_long = 77.574990
tl_lat = 28.525251
tl_long = 77.574948
bl_lat = 28.525250
bl_long = 77.574382

print(min(br_long,tr_long,tl_long,bl_long))
print(max(br_long,tr_long,tl_long,bl_long))
print(abs(min(br_long,tr_long,tl_long,bl_long)-max(br_long,tr_long,tl_long,bl_long)))
print(min(br_lat,tr_lat,tl_lat,bl_lat))
print(max(br_lat,tr_lat,tl_lat,bl_lat))
print(abs(min(br_lat,tr_lat,tl_lat,bl_lat)-max(br_lat,tr_lat,tl_lat,bl_lat)))

print(28.52529<max(br_lat,tr_lat,tl_lat,bl_lat))
print(28.52529>min(br_lat,tr_lat,tl_lat,bl_lat))
print(77.574959<max(br_long,tr_long,tl_long,bl_long))
print(77.574959>min(br_long,tr_long,tl_long,bl_long))

print()
print(28.52529>mean([tr_lat,br_lat]))
print(28.52529<mean([tl_lat,bl_lat]))
print(77.574959<mean([tr_long,tl_long]))
print(77.574959>mean([br_long,bl_long]))

print()
print(28.5293238>min(tr_lat,br_lat))
print(28.5293238<max(tl_lat,bl_lat))
print(77.5814639<max(tr_long,tl_long))
print(77.5814639>min(br_long,bl_long))


