for i in 20 35 50
do
  FILES=phase2_inputs/inputs$i/*.in
  for f in $FILES;
  do
    name=${f##*/}
    name2=${name%.in}
	  python solver.py $f answers/$i/$name2.out
  done
done
