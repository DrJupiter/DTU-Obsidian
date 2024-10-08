#!bin/bash
#BSUB -q hpc
#BSUB -J HPCPYTHON[1-10] 
#BSUB -n 1
#BSUB -W 3 
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "span[hosts=1]"
#BSUB -u s204123@student.dtu.dk
#BSUB -B
#BSUB -N
#BSUB -o %J_%I.out
#BSUB -e %J_%.out

source /dtu/projects/02613_2024/conda/conda_init.sh
conda activate 02613

time python3 week9gpu.py

#Reduction full
