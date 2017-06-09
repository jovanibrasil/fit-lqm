#!/bin/bash

mkdir c3po-results

python FitLqm.py c3po.pgm 0
python FitLqm.py c3po.pgm 1
python FitLqm.py c3po.pgm 2
python FitLqm.py c3po.pgm 3
python FitLqm.py c3po.pgm 4
python FitLqm.py c3po.pgm 5
python FitLqm.py c3po.pgm 6

python Viz.py c3po-pgm_0_data.txt s
python Viz.py c3po-pgm_1_data.txt s
python Viz.py c3po-pgm_2_data.txt s
python Viz.py c3po-pgm_3_data.txt s
python Viz.py c3po-pgm_4_data.txt s
python Viz.py c3po-pgm_5_data.txt s
python Viz.py c3po-pgm_6_data.txt s

mv c3po-p* c3po-results/
mkdir monalisa-results

python FitLqm.py monalisa.pgm 0
python FitLqm.py monalisa.pgm 1
python FitLqm.py monalisa.pgm 2
python FitLqm.py monalisa.pgm 3
python FitLqm.py monalisa.pgm 4
python FitLqm.py monalisa.pgm 5
python FitLqm.py monalisa.pgm 6

python Viz.py monalisa-pgm_0_data.txt s
python Viz.py monalisa-pgm_1_data.txt s
python Viz.py monalisa-pgm_2_data.txt s
python Viz.py monalisa-pgm_3_data.txt s
python Viz.py monalisa-pgm_4_data.txt s
python Viz.py monalisa-pgm_5_data.txt s
python Viz.py monalisa-pgm_6_data.txt s

mv monalisa-p* monalisa-results/
mkdir adam-results

python FitLqm.py adam.pgm 0
python FitLqm.py adam.pgm 1
python FitLqm.py adam.pgm 2
python FitLqm.py adam.pgm 3
python FitLqm.py adam.pgm 4
python FitLqm.py adam.pgm 5
python FitLqm.py adam.pgm 6
python FitLqm.py adam.pgm 7


python Viz.py adam-pgm_0_data.txt s
python Viz.py adam-pgm_1_data.txt s
python Viz.py adam-pgm_2_data.txt s
python Viz.py adam-pgm_3_data.txt s
python Viz.py adam-pgm_4_data.txt s
python Viz.py adam-pgm_5_data.txt s
python Viz.py adam-pgm_6_data.txt s
python Viz.py adam-pgm_7_data.txt s

mv adam-p* adam-results/


