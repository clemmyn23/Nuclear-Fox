#!/bin/bash

# 1. Save and switch IFS to newline character
SAVEIFS=$IFS
IFS=$'\n'

# 2. List specs
echo "Current java flavour:"
java -version
echo ""

# 2. Parse installed java bins from update-java-alternatives
java_list=(`update-java-alternatives --list | rev | cut -f 1 -d ' ' | rev`)

# 3. Pretty print result to terminal
echo "Select a java flavour to switch to:"
for (( i=0; i<${#java_list[@]}; i++ )); do
    echo "$i: ${java_list[$i]}"
done

read userinput
if [ $userinput -lt ${#java_list[@]} -a $userinput -ge 0 ]; then

    echo ""
    echo "Switching to ${java_list[$userinput]}"
    sudo update-java-alternatives --set ${java_list[$userinput]}

    echo ""
    echo "New java flavour:"
    java -version

    # 6. Restore IFS
    IFS=$SAVEIFS
else
    echo "Invalid input"

	# 6. Restore IFS
    IFS=$SAVEIFS
    exit 1
fi


