#!bin/bash
#BSUB -q hpc
#BSUB -J HPCPYTHON 
#BSUB -n 10
#BSUB -W 2 
#BSUB -R "select[model == XeonGold6142]"
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "span[hosts=1]"
#BSUB -u s204123@student.dtu.dk
#BSUB -B
#BSUB -N
#BSUB -o %J.out
#BSUB -e %J.out

source /dtu/projects/02613_2024/conda/conda_init.sh
conda activate 02613

time python3 week5parallelpi.py "serial" 10000
time python3 week5parallelpi.py "parallel" 10000 10
time python3 week5parallelpi.py "parallel_chunk" 10000 10