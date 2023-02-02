 #!/bin/bash
count=0
until [ "$?" -ne 0 ];
do
  count=$((count+1))
  ./random.sh &> output.txt
done

echo "Repeat: it took $((count)) times for the script to fail"
