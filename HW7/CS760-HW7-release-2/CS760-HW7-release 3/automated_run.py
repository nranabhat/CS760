from os import system
alphas = [0.0005, 0.001, 0.002, 0.005, 0.01]
gammas = [0.95]
for alpha in alphas:
  for gamma in gammas:
    system("python run.py -s a2c -t 1000 -d CartPole-v1 -G 200 -e 2000 -a "+str(alpha)+" -g "+str(gamma)+" -l [32] --no-plots")