print('dae ae ju traeligt va' if (lambda a, b: a/b)(*((lambda l: (sum(1 for i in l if 'ae' in i), len(l)))(input().split()))) >= 0.4 else 'haer talar vi rikssvenska')
